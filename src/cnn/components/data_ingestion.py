import os
import zipfile
import gdown
from cnn import logger
from cnn.utils.common import get_size
from cnn.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config



    def download_file(self)->str:

        try:
            dataset_url=self.config.source_urls
            zip_download_dir=self.config.local_data
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"downloading data from {dataset_url} into directory {zip_download_dir}")

            file_id=dataset_url.split("/")[-2]
            prefix="https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id,zip_download_dir)
            logger.info(f"downloaded data from {dataset_url} into directory {zip_download_dir}")

        except Exception as e:
            raise e
        

    def extract_zip(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data,'r') as zip:
            zip.extractall(unzip_path)


