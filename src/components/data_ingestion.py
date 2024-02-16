import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    artifact_dir = '/Users/kushagragahlaut/Gitdemo/MLProject'
    
    train_data_path : str=os.path.join(artifact_dir,'artifact','train.csv')
    test_data_path : str=os.path.join(artifact_dir,'artifact','test.csv')   
    raw_data_path : str=os.path.join(artifact_dir,'artifact','data.csv')   
       
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('/Users/kushagragahlaut/Gitdemo/MLProject/Notebook/Data/StudentsPerformance.csv')
            logging.info('Read dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)
            
            logging.info('Train/Test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            
            logging.info('Ingestion of data is completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
                
        except Exception as e:
            raise CustomException(e,sys)
            
            
if __name__ == '__main__':
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    
    
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)
    
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
    
    
    
    
    
    
    

    
# import os
# import sys
# from src.exception import CustomException
# from src.logger import logging

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig


# @dataclass
# class DataIngestionConfig:
#     current_dir = os.getcwd()

# # Define relative paths
#     relative_train_path = '../artifact/train.csv'
#     relative_test_path = '../artifact/test.csv'
#     relative_raw_path = '../artifact/data.csv'

# # Convert relative paths to absolute paths
#     train_data_path = os.path.abspath(os.path.join(current_dir, relative_train_path))
#     test_data_path = os.path.abspath(os.path.join(current_dir, relative_test_path))
#     raw_data_path = os.path.abspath(os.path.join(current_dir, relative_raw_path))

# #     train_data_path: str = '../../artifact/train.csv'
# #     test_data_path: str = '../../artifact/test.csv'
# #     raw_data_path: str = '../../artifact/data.csv'

# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config = DataIngestionConfig()

#     def create_artifact_folder(self):
#     # Specify the path to the MLProject directory
#         mlproject_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
#     # Define the path to the artifact directory
#         artifact_dir = os.path.join(mlproject_dir, "artifact")
#     # Create the artifact directory if it doesn't exist
#         os.makedirs(artifact_dir, exist_ok=True)
#         print(f"Artifact directory created: {artifact_dir}")
#         return artifact_dir


#     def initiate_data_ingestion(self):
#         logging.info("Entered the data ingestion method or component")
#         try:
#             df = pd.read_csv('/Users/kushagragahlaut/Gitdemo/MLProject/Notebook/Data/StudentsPerformance.csv')
#             logging.info('Read dataset as dataframe')

#             # Create the artifact folder
#             artifact_dir = self.create_artifact_folder()

#             # Save data
#             df.to_csv(os.path.join(artifact_dir, 'data.csv'), index=False, header=True)
#             logging.info('Raw Data saved successfully')

#             # Split data and save train and test sets
#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
#             train_set.to_csv(os.path.join(artifact_dir, 'train.csv'), index=False, header=True)
#             test_set.to_csv(os.path.join(artifact_dir, 'test.csv'), index=False, header=True)
#             logging.info('Train and test data split and saved successfully')

#             return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

#         except Exception as e:
#             raise CustomException(e, sys)

# if __name__ == '__main__':
#     obj = DataIngestion()
#     train_data,test_data = obj.initiate_data_ingestion()
    
    
#     data_transformation = DataTransformation()
#     data_transformation.initiate_data_transformation(train_data,test_data)





            


        
        
        