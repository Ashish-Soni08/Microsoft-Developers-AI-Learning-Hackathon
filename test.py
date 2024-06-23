import sys

from langchain_community.vectorstores import AzureCosmosDBVectorSearch
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage

from openai import AzureOpenAI

import pymongo

from constants import (AZURE_OPENAI_ENDPOINT,
                       AZURE_OPENAI_API_KEY,
                       AZURE_OPENAI_API_VERSION,
                       AZURE_OPENAI_CHAT_DEPLOYMENT_NAME,
                       AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME,
                       DB_CONNECTION,
                       EMBEDDING_MODEL,
                       LLM)


# LLM
llm = AzureChatOpenAI(            
        temperature = 0.2,
        openai_api_version = AZURE_OPENAI_API_VERSION,
        azure_endpoint = AZURE_OPENAI_ENDPOINT,
        openai_api_key = AZURE_OPENAI_API_KEY,         
        model_name = LLM
        )

# Embeddings
client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)

embeddings = client.embeddings.create(
    input = "Hey I am Ashish",
    model= EMBEDDING_MODEL
)


# Connect to the database
client = pymongo.MongoClient(DB_CONNECTION)