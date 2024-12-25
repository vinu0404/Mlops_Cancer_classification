from cnn.constants.constants import *
from cnn.utils.common import read_yaml,make_dir
from cnn.entity.config_entity import DataIngestionConfig



class ConfigurationManager:
    def __init__(
            self,
            params_file= PARAMS_FILE_PATH,
            config_file= CONFIG_FILE_PATH):
            
        self.config=read_yaml(config_file)
        self.params=read_yaml(params_file)

        make_dir([self.config.artifacts_root])

    

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion

        make_dir([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_urls=config.source_urls,
            local_data=config.local_data,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
        

    
