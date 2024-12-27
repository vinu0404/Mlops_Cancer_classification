from cnn.constants.constants import *
from cnn.utils.common import read_yaml,make_dir
from cnn.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig
from pathlib import Path


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
    


    def get_base_model_config(self)->PrepareBaseModelConfig:
        config=self.config.prepare_base_model
        print(f"{config}")


        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weight=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
            
        )

        return prepare_base_model_config
    

    
        

    
