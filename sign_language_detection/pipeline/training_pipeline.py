import sys, os
from sign_language_detection.logger import logging
from sign_language_detection.exception import SignException
from sign_language_detection.components.data_ingestion import DataIngestion

from sign_language_detection.entity.config_entity import DataIngestionConfig
from sign_language_detection.entity.artifacts_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        # self.data_validation_config = DataValidationConfig()
        # self.model_trainer_config = ModelTrainerConfig()
        # self.model_pusher_config = ModelPusherConfig()
        # self.s3_operations = S3Operation()

    

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)