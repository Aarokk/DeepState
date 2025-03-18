import logging
import os
import shutil

from Microservices.PdfExtraction import PDFExtractionInterfaces

logging.basicConfig(level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

TEMP_FOLDER_ROUTE = "C:\\temporal_pdf_files"


class PDFExtractionService(PDFExtractionInterfaces):
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
