from cnn.config.configuration import ConfigurationManager
from cnn.components.eval_mlflowui import Evaluation
from cnn import logger
from dotenv import load_dotenv
import os

load_dotenv()

# Access the environment variables




stage_name="Evaluation & Experiment Tracking"
class eval_mlflow:
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(config=eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()

        except Exception as e:
            raise e
        




if __name__ == '__main__':
        try:
            logger.info(f"*******************")
            logger.info(f">>>>>> stage {stage_name} started <<<<<<")
            obj = eval_mlflow()
            obj.main()
            logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e