import tensorflow as tf
from cnn.entity.config_entity import TrainingConfig
from pathlib import Path
import shutil
import os





class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):           # updated base model 
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
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

        if self.config.params_augmented:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    @staticmethod
    def copy_model(source_path: str, destination_path: str):
        try:
            # Ensure the destination directory exists
            os.makedirs(destination_path, exist_ok=True)
            
            # Copy the model file
            shutil.copy(source_path, destination_path)
            return f"Model copied successfully to {destination_path}"
        except Exception as e:
            raise Exception(f"Error while copying model: {str(e)}")
 



    # Example usage:
    # copy_model('path/to/source/model.h5', 'path/to/destination/folder/')




    
    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model)

        self.copy_model("artifacts/training/trained_model.h5","models")


        
        