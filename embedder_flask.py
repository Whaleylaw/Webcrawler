#!/usr/bin/env python3
from flask import Flask, request, jsonify, Response
import os
import time
import threading
from queue import Queue
from embedder import embed_files  # Import the embed_files function from embedder.py

app = Flask(__name__)
progress_queue = Queue()
active_embedders = {}
is_embedding = False

@app.route('/start_embedding', methods=['POST'])
def start_embedding():
    global is_embedding
    if is_embedding:
        return jsonify({'status': 'error', 'message': 'Embedding process already running'}), 400

    data = request.get_json()
    if not data or 'input_dir' not in data:
        return jsonify({'error': 'Input directory is required'}), 400

    input_dir = data['input_dir']
    if not os.path.exists(input_dir):
        return jsonify({'error': f'Directory {input_dir} does not exist'}), 400

    # Clear progress queue
    while not progress_queue.empty():
        progress_queue.get()

    def run_embedding():
        global is_embedding
        is_embedding = True
        try:
            # Redirect print statements to our progress queue
            import sys
            from io import StringIO
            old_stdout = sys.stdout
            string_io = StringIO()
            sys.stdout = string_io

            # Run the embedding process
            embed_files(input_dir)

            # Get any remaining output
            output = string_io.getvalue()
            if output:
                for line in output.split('\n'):
                    if line.strip():
                        progress_queue.put(line.strip())

            # Restore stdout
            sys.stdout = old_stdout
            progress_queue.put("Embedding complete.")
            progress_queue.put("DONE")

        except Exception as e:
            progress_queue.put(f"Error during embedding: {str(e)}")
            progress_queue.put("DONE")
        finally:
            is_embedding = False

    threading.Thread(target=run_embedding).start()
    return jsonify({'status': 'success', 'message': 'Embedding process started'})

@app.route('/stream_progress')
def stream_progress():
    def generate():
        while True:
            if not progress_queue.empty():
                message = progress_queue.get()
                yield f"data: {message}\n\n"
                if message == "DONE":
                    break
            else:
                time.sleep(0.1)
    return Response(generate(), mimetype='text/event-stream')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
      <head>
          <title>Embedder Interface</title>
          <style>
              body {
                  font-family: Arial, sans-serif;
                  max-width: 800px;
                  margin: auto;
                  padding: 20px;
              }
              input[type=text] {
                  width: 100%;
                  padding: 8px;
                  margin-bottom: 10px;
              }
              button {
                  padding: 10px;
                  margin: 5px;
                  background-color: #4CAF50;
                  color: white;
                  border: none;
                  border-radius: 4px;
                  cursor: pointer;
              }
              button:disabled {
                  background-color: #cccccc;
                  cursor: not-allowed;
              }
              #progress {
                  background: #f0f0f0;
                  padding: 10px;
                  border: 1px solid #ccc;
                  height: 300px;
                  overflow-y: auto;
                  font-family: monospace;
                  white-space: pre-wrap;
              }
              .error {
                  color: red;
              }
          </style>
      </head>
      <body>
          <h1>Embedder Interface</h1>
          <div>
              <input type="text" id="input_dir" placeholder="Input directory path (e.g., crawled_data)" value="crawled_data">
              <button onclick="startEmbedding()" id="startButton">Start Embedding</button>
          </div>
          <div id="progress"></div>

          <script>
            var eventSource = null;
            var isEmbedding = false;

            function startEmbedding() {
                var input_dir = document.getElementById('input_dir').value;
                if (!input_dir) {
                    alert('Input directory is required');
                    return;
                }

                const startButton = document.getElementById('startButton');
                startButton.disabled = true;
                document.getElementById('progress').innerHTML = '';

                if (eventSource) {
                    eventSource.close();
                }

                eventSource = new EventSource('/stream_progress');
                eventSource.onmessage = function(event) {
                    var progressDiv = document.getElementById('progress');
                    if (event.data.includes('Error')) {
                        progressDiv.innerHTML += '<span class="error">' + event.data + '</span><br>';
                    } else {
                        progressDiv.innerHTML += event.data + '<br>';
                    }
                    progressDiv.scrollTop = progressDiv.scrollHeight;

                    if (event.data === "DONE") {
                        eventSource.close();
                        startButton.disabled = false;
                    }
                };

                fetch('/start_embedding', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({input_dir: input_dir})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'error') {
                        document.getElementById('progress').innerHTML += 
                            '<span class="error">' + data.message + '</span><br>';
                        startButton.disabled = false;
                        if (eventSource) {
                            eventSource.close();
                        }
                    }
                })
                .catch(error => {
                    document.getElementById('progress').innerHTML += 
                        '<span class="error">Error: ' + error.message + '</span><br>';
                    startButton.disabled = false;
                    if (eventSource) {
                        eventSource.close();
                    }
                });
            }
          </script>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Using port 5001 to avoid conflict with scraper 