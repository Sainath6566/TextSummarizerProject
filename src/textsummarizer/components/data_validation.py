from textsummarizer.entity import DataValidationConfig
import os
from textsummarizer.logging import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            print("All Files:", all_files)

            
            valid_files = [file for file in all_files if file.split('.')[0] in self.config.ALL_REQUIRED_FILES]
            print("Valid Files:", valid_files)

            validation_status = len(valid_files) == len(self.config.ALL_REQUIRED_FILES)

            print("Validation Status:", validation_status)

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            raise e