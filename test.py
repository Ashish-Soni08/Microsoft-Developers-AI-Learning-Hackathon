import sys

from openai import AzureOpenAI

from constants import (API_KEY,
                       API_VERSION,
                       ENDPOINT,
                       EMBEDDING_MODEL,
                       LLM)

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020.",
    },
    {"role": "user", "content": "Write a Poem"},
]


try:
    response = client.chat.completions.create(
        model=LLM,
        messages=MESSAGES,
        stream=True
    )

    print(response.model_dump_json(indent=2))

except Exception as error:
    print(error.response.text)
    # sys.exit()

embeddings = client.embeddings.create(
    input = "Hey I am Ashish",
    model= EMBEDDING_MODEL
)



    
