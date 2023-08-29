from textsummarizer.config.configuration import ConfigurationManager2
from textsummarizer.components.data_validation import DataValidation
from textsummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager2()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
    