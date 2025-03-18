from abc import ABC, abstractmethod


class PDFExtractionInterfaces(ABC):
    """
        The class that implements the following methods should receive the following parameters from the GUI:
        search_fields_content[] -> Array composed of four strings
        sections_content[] -> Array composed of six booleans
        logic_selectors_content[] -> Array composed of four strings representing the logic operators
        date_content[] -> Array composed of two strings representing the start and end dates
        results_per_page -> String representing the number of results per page desired
        date_order_by -> String representing the order desired by date
    """

    @abstractmethod
    def create_temp_folder(self):
        """
             Creates a temporary folder to store the extracted PDFs
             the folder must be failsafe, if an exception occurs during extraction
             e.g. BOE not online, search without results, etc., the exception will
             call cleanup()
        """
        pass

    @abstractmethod
    def extract(self):
        """
            receives parameters from GUI and extracts PDFs from BOE based on them
            if the search fails, the exception will call cleanup(),
            should send some type of signal to the GUI when extraction finishes
        """
        pass

    @abstractmethod
    def cleanup(self):
        """
            deletes the temporary folder created by create_temp_folder() and all its contents
        """
        pass

    @abstractmethod
    def write_search_params(self):
        """
            writes the search parameters to a json file in the temporary folder
            must check if the folder exists first
            should be called after extract(), if the search succeeds
        """
        pass
