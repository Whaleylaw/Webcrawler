#!/usr/bin/env python3
from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams

def setup_weaviate():
    # Connect to Weaviate
    connection_params = ConnectionParams.from_url(
        url="http://localhost:8080",
        grpc_port=50051
    )
    client = WeaviateClient(connection_params)
    client.connect()

    try:
        # Create WebPage collection if it doesn't exist
        collection = client.collections.create_from_dict({
            "class": "WebPage",
            "description": "A scraped webpage",
            "vectorizer": None,  # We'll provide vectors manually
            "properties": [
                {
                    "name": "url",
                    "dataType": ["text"],
                    "description": "The URL of the webpage"
                },
                {
                    "name": "content",
                    "dataType": ["text"],
                    "description": "The content of the webpage"
                }
            ]
        })
        print("Successfully created WebPage collection!")
    except Exception as e:
        if "already exists" in str(e):
            print("WebPage collection already exists.")
        else:
            print(f"Error creating collection: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    setup_weaviate() 