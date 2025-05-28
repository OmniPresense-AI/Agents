from openai import OpenAI
client = OpenAI()

def file_search(query: str):
    response = client.responses.create(
    model="gpt-4o-mini",
    input=query,
    tools=[{
        "type": "file_search",
        "vector_store_ids": os.getenv("VECTOR_STORE_ID")
    }]
    )
    return response