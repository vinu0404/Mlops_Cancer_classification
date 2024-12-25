from cnn.config.configuration import ConfigurationManager
from cnn.components.data_ingestion import DataIngestion
from cnn import logger

stage_name="Data_ingestion_stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()



if __name__=="__main":
    try:
        logger.info(">>>>>>>{stage_name}   started <<<<<<<<<<<<<<<")
        DataIngestionPipeline().main()
        logger.info(f">>>>>>>>>>>>>{stage_name} completed  <<<<<<<<<")

    except Exception as e:
        raise e