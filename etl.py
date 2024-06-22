from typing import List

import fitz

from llama_parse import LlamaParse
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.embeddings.gemini import GeminiEmbedding



from constants import (EMBEDDING_MODEL,
                       GEMINIPRO_API_KEY,
                       LLAMAPARSE_API_KEY,
                       QDRANT_API_KEY,
                       QDRANT_CLUSTER)
                       

def partition_pdf(page_numbers: List[int], new_pdf_name: str, pdf_path: str = "data/raw/Master_Thesis_Aidana_Rakhatbekova.pdf") -> None:
    """
    Partitions a PDF by selecting specific pages and saves the result to a new PDF file.

    Parameters:
        page_numbers (List[int]): A list of page numbers to select from the original PDF.
        new_pdf_name (str): The file path where the new PDF will be saved.
        pdf_path (str, optional): The file path of the original PDF. Defaults to "data/raw/Master_Thesis_Aidana_Rakhatbekova.pdf".

    Returns:
        None
    """
    doc = fitz.open(pdf_path)
    doc.select(page_numbers)
    doc.save(new_pdf_name)


###### ETL PIPELINE ######

def extract_markdown_from_pdf(api_key: str = LLAMAPARSE_API_KEY, file_path: str = "data/Master_Thesis_Aidana.pdf", result_type: str = "markdown"):
    
    parser = LlamaParse(
        api_key = api_key,
        result_type = result_type # "markdown" and "text" are available
        )  

    documents = parser.load_data(file_path)

    print("Total Number of Documents parsed ->", len(documents))

def transform_markdown_to_nodes(docs: List):

    markdown_parser = MarkdownNodeParser()
    nodes = markdown_parser.get_nodes_from_documents(docs, include_metadata=True, include_prev_next_rel=True)
    print("Total Number of Nodes created ->", len(nodes))

def load_to_qdrant():
    pass