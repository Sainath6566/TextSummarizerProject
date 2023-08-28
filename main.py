from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.logging import logger

STAGE_NANME="Data Ingestion stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NANME} started <<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> stage {STAGE_NANME} completed <<<<<<<<<\n]nx============x")
except Exception as e:
    logger.exception(e)
    raise e