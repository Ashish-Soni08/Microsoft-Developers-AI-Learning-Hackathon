from typing import List

import fitz

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

if __name__ == "__main__":
    partition_pdf([1, 2, 3, 4, 5], "data/processed/Introduction.pdf")
    partition_pdf([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], "data/processed/State_of_the_Art.pdf")
    partition_pdf([18, 19, 20, 21], "data/processed/Theoretical_Framework.pdf")
    partition_pdf([21, 22, 23, 24, 25, 26], "data/processed/Methodology.pdf")
    partition_pdf([27, 28, 29, 30, 
               31, 32, 33, 34, 35, 
               36, 37, 38, 39, 40,
               41, 42, 43, 44, 45, 
               46, 47, 48, 49, 50, 
               51, 52, 53, 54, 55, 
               56, 57, 58, 59], "data/processed/Analysis_and_Presentation_of_Findings.pdf")
    partition_pdf([59, 60, 61, 62, 63], "data/processed/Conclusion.pdf")
    partition_pdf([64, 65, 66, 67, 68, 69, 70], "data/processed/References.pdf")
    partition_pdf([71, 72], "data/processed/Appendix_A.pdf")
    partition_pdf([75], "data/processed/Appendix_B.pdf")
    print("Master_Thesis_Aidana_Rakhatbekova PDF partitioned into 9 PDfs successfully!")
