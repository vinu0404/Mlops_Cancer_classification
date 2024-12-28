from cnn.constants.constants import *
from cnn.utils.common import read_yaml,make_dir,save_json
from cnn.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,TrainingConfig,EvaluationConfig
from pathlib import Path
import os 


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
    



    def training_model_config(self)->TrainingConfig:
        con=self.config.training
        updated_model=self.config.prepare_base_model
        make_dir([con.root_dir])
        training_data=os.path.join(self.config.data_ingestion.unzip_dir,"Chest-CT-Scan-data")

        trained_model_config=TrainingConfig(

            root_dir=Path(con.root_dir),
            trained_model_path=Path(con.trained_model_path),
            
            updated_base_model_path=Path(updated_model.updated_base_model_path),
            training_data= Path(training_data),
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE,
            params_augmented=self.params.AUGMENTATION,
            params_image_size=self.params.IMAGE_SIZE

        )
        return trained_model_config
    



    def get_evaluation_config(self) -> EvaluationConfig:
        training_data=os.path.join(self.config.data_ingestion.unzip_dir,"Chest-CT-Scan-data")
        eval_config = EvaluationConfig(
            path_of_model=Path(self.config.training.trained_model_path),
            training_data=Path(training_data),
            mlflow_uri="https://dagshub.com/vinu0404/Mlops_Cancer_classification.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config
            

    
        

    
