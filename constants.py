from dotenv import dotenv_values

config = dotenv_values(".env")

API_KEY = config["OPENAI_API_KEY"]

API_VERSION = "2024-02-01"

ENDPOINT = config["AZURE_AI_ENDPOINT"]

EMBEDDING_MODEL = "text-embedding-ada-002"

LLM = "gpt-4-32k"