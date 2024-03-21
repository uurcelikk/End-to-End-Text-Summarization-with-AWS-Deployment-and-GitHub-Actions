from src.TextSummarization.config.configuration import ConfigurationManager
from src.TextSummarization.components.data_ingestion import DataValidation  
from src.TextSummarization.logging import logger    



class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.download_file()
        data_validation.extract_zip_file()