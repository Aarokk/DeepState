import logging
import os
import shutil
from typing import List

from Microservices.PdfExtraction import PDFExtractionInterfaces

# Logger setup
logging.basicConfig(level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

# Define a route for temporal folder (this one is for ease of testing)
# TO-DO: Establish a new route within the application files
TEMP_FOLDER_ROUTE = "C:\\temporal_pdf_files"


class PDFExtractionService(PDFExtractionInterfaces):
    # Class builder receives the parameters specified in PDFExtractionInterfaces
    # Information about expected contents is to be found inside the class
    def __init__(self,
                 search_fields_content: List[str],
                 sections_content: List[bool],
                 logic_selectors_content: List[str],
                 date_content: List[str],
                 results_per_page: str,
                 date_order_by: str
                 ):
        self.search_fields_content = search_fields_content
        self.sections_content = sections_content
        self.logic_selectors_content = logic_selectors_content
        self.date_content = date_content
        self.results_per_page = results_per_page
        self.date_order_by = date_order_by

    # Implementation of an abstract method
    def create_temp_folder(self):
        try:
            os.makedirs(TEMP_FOLDER_ROUTE, exist_ok=True)
        except OSError:
            logging.error("Creation of the directory %s failed" % TEMP_FOLDER_ROUTE)

    # Implementation of an abstract method
    def extract(self):
        pass

    # Implementation of an abstract method
    def cleanup(self):
        try:
            shutil.rmtree(TEMP_FOLDER_ROUTE)
        except FileNotFoundError:
            logging.error("Folder %s doesn't exist." % TEMP_FOLDER_ROUTE)
        except PermissionError:
            print("User does not have permission to delete the folder.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    # Implementation of an abstract method
    def write_search_params(self):
        pass
