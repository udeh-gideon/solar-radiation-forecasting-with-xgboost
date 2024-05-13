from src.solar_radiation_prediction import logger
from src.solar_radiation_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f'>>>>> {STAGE_NAME} started successfully <<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> {STAGE_NAME} completed successfully <<<<<<\n\nx================x')
except Exception as e:
    logger.exception(e)
    raise e