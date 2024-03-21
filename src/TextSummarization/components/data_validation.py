import os 
from src.TextSummarization.logging import logger
from src.TextSummarization.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):

        self.config = config



    def validate_all_files_exist(self) -> bool:
        """
        Validate if all files exist in the directory
        :return: True if all files exist, False otherwise
        """

        try:
            validation_status = None

            all_files =os.listdir(os.path.join("artifact", "data_ingestion", "data"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write("Validation Failed")

                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write("Validation Passed")

            return validation_status
        except Exception as e:
            logger.error(f"An error occurred during file validation: {str(e)}")
            return False
