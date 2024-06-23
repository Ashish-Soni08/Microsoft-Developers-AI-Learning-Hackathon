import sys

from langchain_community.vectorstores import AzureCosmosDBVectorSearch
from langchain_openai import (AzureChatOpenAI, AzureOpenAIEmbeddings)

from constants import (AZURE_OPENAI_ENDPOINT,
                       AZURE_OPENAI_API_KEY,
                       AZURE_OPENAI_API_VERSION,
                       AZURE_OPENAI_CHAT_DEPLOYMENT_NAME,
                       AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME,
                       DB_CONNECTION,
                       EMBEDDING_MODEL,
                       LLM)

llm_client = AzureOpenAI(
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
    llm_response = llm_client.chat.completions.create(
        model=LLM,
        messages=MESSAGES,
        stream=True
    )

    print(llm_response.model_dump_json(indent=2))

except Exception as error:
    print(error.response.text)
    # sys.exit()

embeddings = llm_client.embeddings.create(
    input = "Hey I am Ashish",
    model= EMBEDDING_MODEL
)



    
