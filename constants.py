from dotenv import dotenv_values

config = dotenv_values(".env")

AZURE_OPENAI_ENDPOINT = config["AZURE_AI_ENDPOINT"]
AZURE_OPENAI_API_KEY = config["OPENAI_API_KEY"]


AZURE_OPENAI_API_VERSION = "2024-02-01"

AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = "chat"
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME = "embeddings"

DB_CONNECTION = config["DB_CONNECTION_STRING"]

EMBEDDING_MODEL = "text-embedding-ada-002"

LLM = "gpt-4-32k"