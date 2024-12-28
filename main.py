from src.cnn import logger
from src.cnn.pipeline.pipeline_dataingestion import DataIngestionPipeline
from src.cnn.pipeline.pipeline_prepare_base_model import PrepareModel
from cnn.pipeline.pipeline_training import Training_model


stage_name1="Data_ingestion_stage"
try:
    logger.info(f">>>>>>>   {stage_name1} started <<<<<<<<<<<<<<<")
    DataIngestionPipeline().main()
    logger.info(f">>>>>>>>>>>>>   {stage_name1} completed  <<<<<<<<<")

except Exception as e:
    logger.info(f"{e}")
    raise e


stage_name2="Preparing_Base_Model_stage"

try:
    logger.info(f">>>>>>>  {stage_name2}   started <<<<<<<<<<<<<<<")
    PrepareModel().main()
    logger.info(f">>>>>>>>>>>>>  {stage_name2} completed  <<<<<<<<<")

except Exception as e:
    logger.info(f"{e}")
    raise e




stage_name3="Training"

try:
    logger.info(f">>>>>>>  {stage_name3}   started <<<<<<<<<<<<<<<")
    Training_model().main()
    logger.info(f">>>>>>>>>>>>>  {stage_name3} completed  <<<<<<<<<")

except Exception as e:
    raise e
