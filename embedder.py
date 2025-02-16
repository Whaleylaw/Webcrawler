#!/usr/bin/env python3
import os
import sys
import torch
from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams
from transformers import AutoTokenizer, AutoModel


def generate_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1)
    return embedding.squeeze(0).tolist()


def get_file_content(filepath):
    """
    Read the content of a markdown file and use the filename as the URL.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Use the filename as the URL/identifier
        url = os.path.basename(filepath)
        return url, content
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None, None


def embed_files(input_dir):
    # Setup Weaviate client
    connection_params = ConnectionParams.from_url(
        url='http://localhost:8080',
        grpc_port=50051  # Updated to match docker-compose
    )
    client = WeaviateClient(connection_params)
    client.connect()  # Explicitly connect to the client

    try:
        # Load embedding model
        global tokenizer, model
        embedding_model_name = 'Alibaba-NLP/gte-Qwen2-7B-instruct'
        tokenizer = AutoTokenizer.from_pretrained(embedding_model_name)
        model = AutoModel.from_pretrained(embedding_model_name)

        # Get the WebPage collection
        collection = client.collections.get("WebPage")

        # Process markdown files
        if not os.path.exists(input_dir):
            print(f"Directory {input_dir} does not exist.")
            return

        md_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.md')]
        if not md_files:
            print(f"No markdown files found in {input_dir}.")
            return

        print(f"Found {len(md_files)} markdown files to process.")
        for filepath in md_files:
            url, file_content = get_file_content(filepath)
            if not url or not file_content:
                continue
            try:
                print(f"Generating embedding for {url}...")
                embedding = generate_embedding(file_content)
                
                print(f"Inserting {url} into Weaviate...")
                collection.data.insert(
                    properties={"url": url, "content": file_content},
                    vector=embedding
                )
                print(f"Successfully embedded file: {filepath}")
            except Exception as e:
                print(f"Error embedding file {filepath}: {e}")
    except Exception as e:
        print(f"Error during embedding process: {e}")
    finally:
        client.close()  # Properly close the client


if __name__ == '__main__':
    input_dir = sys.argv[1] if len(sys.argv) > 1 else 'crawled_data'
    embed_files(input_dir) 