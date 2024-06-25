"""

"""
import os
import json
from typing import List

import pymongo

from langchain.chat_models import AzureChatOpenAI
from langchain.vectorstores.azure_cosmos_db import AzureCosmosDBVectorSearch
from langchain.schema.document import Document
from langchain.agents import Tool
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.tools import StructuredTool
from langchain_core.messages import SystemMessage

from constants import (AZURE_OPENAI_ENDPOINT,
                       AZURE_OPENAI_API_KEY,
                       AZURE_OPENAI_API_VERSION,
                       DB_CONNECTION,
                       EMBEDDING_MODEL,
                       LLM,
                       LLAMAPARSE_API_KEY,
                       LANGCHAIN_URL,
                       LANGCHAIN_API_KEY,
                       LANGCHAIN_PROJECT)
db = pymongo.MongoClient(DB_CONNECTION).thesis_vectordb

class ThesisRagAIAgent:
    """
    Thesis RAG AI Agent.
    """
    pass