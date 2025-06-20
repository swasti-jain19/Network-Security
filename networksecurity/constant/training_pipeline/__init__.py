import os
import sys
import numpy as np
import pandas as pd


'''
defining common constants variables for training pipeline

'''
TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "NetworkSecurityPipeline"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phishingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

'''
data ingestion related constants starts with DATA_INGESTION var name

'''
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "NetworkSecurity"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" 
DATA_INGESTION_INGESTED_DIR: str = "ingested_data"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2         