from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarizer.pipeline.stage04_model_training import ModelTraninerTrainingPipeline
from textsummarizer.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline
from textsummarizer.logging import logger
import os
import sys


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



STAGE_NANME="Data Transformation stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NANME} started <<<<<<<<<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>> stage {STAGE_NANME} completed <<<<<<<<<\n]nx============x")
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NANME=" Model Training stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NANME} started <<<<<<<<<<")
    model_trainer=ModelTraninerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>> stage {STAGE_NANME} completed <<<<<<<<<\n]nx============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NANME=" Model evaluation stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NANME} started <<<<<<<<<<")
    model_evaluation=ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>> stage {STAGE_NANME} completed <<<<<<<<<\n]nx============x")
except Exception as e:
    logger.exception(e)
    raise e