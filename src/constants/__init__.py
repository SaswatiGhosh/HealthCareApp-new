import os 
from datetime import date

#Where you store your data


#Pipeline
PIPELINE_NAME: str=""
ARTIFACT_DIR: str="artifact"
MODEL_FILE_NAME="model.pkl"

TARGET_COLUMN= "Response"
CURRENT_YEAR=date.today().year
PREPROCESSING_OBJECT_FILENAME="preprocessing.pkl"

FILE_NAME:str="data.csv"
TRAIN_FILE_NAME:str ="train.csv"
TEST_FILE_NAME:str="test.csv"
SCHEMA_FILE_PATH=os.path.join("config", "schema.yaml")



#Data ingestion related constant start with DATA_INGESTION VAR NAME

DATA_INGESTION_COLLECTION_NAME:str="Proj1-Data"
DATA_INGESTION_DIR_NAME:str= "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str= "feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float=0.2



