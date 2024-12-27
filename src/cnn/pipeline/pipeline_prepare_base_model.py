from cnn.config.configuration import ConfigurationManager
from cnn.components.prepare_base_model import PrepareBaseModel
from cnn import logger


stage_name="Preparing base model"

class PrepareModel:
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>  {stage_name}   started <<<<<<<<<<<<<<<")
        PrepareModel().main()
        logger.info(f">>>>>>>>>>>>>  {stage_name} completed  <<<<<<<<<")

    except Exception as e:
        raise e