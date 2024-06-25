from typing import List
import time

from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import MarkdownNodeParser

from langchain_community.vectorstores import AzureCosmosDBVectorSearch

from openai import AzureOpenAI

import pymongo

from tenacity import retry, wait_random_exponential, stop_after_attempt

from constants import (AZURE_OPENAI_ENDPOINT,
                       AZURE_OPENAI_API_KEY,
                       AZURE_OPENAI_API_VERSION,
                       DB_CONNECTION,
                       EMBEDDING_MODEL,
                       LLAMAPARSE_API_KEY
                       )



vector_store = AzureCosmosDBVectorSearch.from_connection_string(
    connection_string = DB_CONNECTION,
    namespace = "test",
    embedding = embedding_model,
    index_name = "test_index",
    embedding_key = "content_vector"

)

def extract_markdown_from_pdf(api_key: str = LLAMAPARSE_API_KEY, folder_path: str = "data/processed"):
    
    parser = LlamaParse(
    api_key=LLAMAPARSE_API_KEY,
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,
    language="en")

    file_extractor = {".pdf": parser}
    
    documents = SimpleDirectoryReader(folder_path, file_extractor=file_extractor).load_data()

    print("Total Number of Documents parsed ->", len(documents))

def transform_markdown_to_nodes(docs: List):

    markdown_parser = MarkdownNodeParser()
    nodes = markdown_parser.get_nodes_from_documents(docs, include_metadata=True, include_prev_next_rel=True)
    print("Total Number of Nodes created ->", len(nodes))

def load_to_qdrant():
    
    client = AzureOpenAI(azure_endpoint=AZURE_OPENAI_ENDPOINT,
                         api_key=AZURE_OPENAI_API_KEY,
                         api_version=AZURE_OPENAI_API_VERSION)
    
    db_client = pymongo.MongoClient(DB_CONNECTION)


    
    embeddings = client.embeddings.create(
    
    
    
    input = "<markdown text of every chunk>",
    model= EMBEDDING_MODEL
    )
    vector_store = AzureCosmosDBVectorSearch.from_connection_string(
    connection_string = DB_CONNECTION,
    namespace = "test",
    embedding = embedding_model,
    index_name = "test_index",
    embedding_key = "content_vector")

@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(3))
def generate_embeddings(text: str):
    '''
    Generate embeddings from string of text using the deployed Azure OpenAI API embeddings model.
    This will be used to vectorize document data and incoming user messages for a similarity search with
    the vector index.

    Parameters: 
    text (str): The input text from which to generate embeddings.

    Returns:
    list: A list of embeddings generated from the input text.

    Reference:
    https://github.com/AzureCosmosDB/Azure-OpenAI-Python-Developer-Guide/blob/main/Labs/lab_3_mongodb_vector_search.ipynb
    '''
    response = ai_client.embeddings.create(input=text, model=EMBEDDING_MODEL)
    embeddings = response.data[0].embedding
    time.sleep(0.5) # rest period to avoid rate limiting on AOAI
    return embeddings



if __name__ == "__main__":
    ai_client = AzureOpenAI(azure_endpoint=AZURE_OPENAI_ENDPOINT,
                         api_key=AZURE_OPENAI_API_KEY,
                         api_version=AZURE_OPENAI_API_VERSION)
