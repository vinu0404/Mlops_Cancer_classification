from cnn.entity.config_entity import EvaluationConfig
import tensorflow as tf
import mlflow 
import mlflow.keras
from pathlib import Path
from cnn.utils.common import save_json
from urllib.parse import urlparse




class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    



    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    
    '''def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        print(f"Registry URI set to: {mlflow.get_registry_uri()}")

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        print(f"Tracking URL type: {tracking_url_type_store}")

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            print(f"Parameters logged: {self.config.all_params}")

            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            print(f"Metrics logged: Loss={self.score[0]}, Accuracy={self.score[1]}")

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="vin")
                print("Model logged and registered with name 'vin'")
            else:
                mlflow.keras.log_model(self.model, "model")
                print("Model logged without registration (file store)")'''
    def log_into_mlflow(self):
        from dotenv import load_dotenv
        import os

        load_dotenv()

        # Access the environment variables
        mlflow_username = os.getenv('MLFLOW_TRACKING_USERNAME')
        mlflow_pswd = os.getenv('MLFLOW_TRACKING_PASSWORD')

        print(mlflow_username)  # Should print 'vinu0404'
        print(mlflow_pswd)  # Should print the password or None if not set
 

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_registry_uri(self.config.mlflow_uri)
        print(f"Tracking URI set to: {mlflow.get_tracking_uri()}")
        print(f"Registry URI set to: {mlflow.get_registry_uri()}")

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        print(f"Tracking URL type: {tracking_url_type_store}")

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            print(f"Parameters logged: {self.config.all_params}")

            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            print(f"Metrics logged: Loss={self.score[0]}, Accuracy={self.score[1]}")

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="vin_2")
                print("Model logged and registered with name 'vin2'")
            else:
                mlflow.keras.log_model(self.model, "model")
                print("Model logged without registration (file store)")

