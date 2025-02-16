#!/usr/bin/env python3
from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams

def check_weaviate_contents():
    # Connect to Weaviate
    connection_params = ConnectionParams.from_url(
        url="http://localhost:8080",
        grpc_port=50051
    )
    client = WeaviateClient(connection_params)
    client.connect()

    try:
        # Get the WebPage collection
        collection = client.collections.get("WebPage")
        
        # Get objects (up to 5)
        query = collection.query.fetch_objects()
        results = query.objects
        count = len(results) if results else 0
        
        print(f"\nTotal objects found in WebPage collection: {count}")

        if count > 0:
            print("\nSample entries:")
            for obj in list(results)[:5]:
                print(f"\nProperties: {obj.properties}")
                print("-" * 80)
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    check_weaviate_contents() 