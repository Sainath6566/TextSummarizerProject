from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textsummarizer.logging import logger

STAGE_NANME="Data ingestion stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NANME} started <<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> stage {STAGE_NANME} completed <<<<<<<<<\n]nx============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NANME="Data Validation stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NANME} started <<<<<<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> stage {STAGE_NANME} completed <<<<<<<<<\n]nx============x")
except Exception as e:
    logger.exception(e)
    raise e