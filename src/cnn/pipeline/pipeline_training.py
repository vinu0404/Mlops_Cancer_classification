from cnn.config.configuration import ConfigurationManager
from cnn.components.training import Training
from cnn import logger

stage_name="Training"
class Training_model:
    def __init__(self):
        pass


    def main(self):
     try:
        config=ConfigurationManager()
        training_config=config.training_model_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

     except Exception as e:
        logger.info(f"e")
        raise e
     


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>  {stage_name}   started <<<<<<<<<<<<<<<")
        Training_model().main()
        logger.info(f">>>>>>>>>>>>>  {stage_name} completed  <<<<<<<<<")

    except Exception as e:
        raise e
        

 
