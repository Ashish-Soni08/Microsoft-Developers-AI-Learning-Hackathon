from dotenv import dotenv_values

config = dotenv_values(".env")

ENDPOINT = config["AZURE_AI_ENDPOINT"]
API_KEY = config["OPENAI_API_KEY"]