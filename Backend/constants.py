from dotenv import dotenv_values

config = dotenv_values(".env")

# Azure OpenAI Endpoint, API Key, and API Version
AZURE_OPENAI_ENDPOINT = config["AZURE_AI_ENDPOINT"]
AZURE_OPENAI_API_KEY = config["OPENAI_API_KEY"]
AZURE_OPENAI_API_VERSION = "2024-02-01"

# Azure Cosmos DB for MongoDB (vCore) Connection String
DB_CONNECTION = config["DB_CONNECTION_STRING"]

# MODEL NAMES
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM = "gpt-4-32k"

# Llamaparse for Parsing PDFs 
LLAMAPARSE_API_KEY = config["LLAMAPARSE_API"]

# LangSmith for Tracing and Monitoring
LANGCHAIN_URL = config["LANGCHAIN_ENDPOINT"]
LANGCHAIN_API_KEY = config["LANGCHAIN_API"]
LANGCHAIN_PROJECT = config["LANGCHAIN_PROJECT"]
