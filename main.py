from src.cnn import logger
from src.cnn.pipeline.pipeline_dataingestion import DataIngestionPipeline



stage_name="Data_ingestion_stage"
try:
    logger.info(">>>>>>> Data Ingestion stage started <<<<<<<<<<<<<<<")
    DataIngestionPipeline().main()
    logger.info(f">>>>>>>>>>>>>{stage_name} completed  <<<<<<<<<")

except Exception as e:
    raise e