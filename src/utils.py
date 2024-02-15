import os
import sys
import numpy as np
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        pkl_dir = '/Users/kushagragahlaut/Gitdemo/MLProject/'
        file_abs_path = os.path.join(pkl_dir, file_path)

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_abs_path), exist_ok=True)

        with open(file_abs_path, "wb") as file_obj:
            
#         dir_path = os.path.dirname(file_path)

#         os.makedirs(dir_path, exist_ok=True)

#         with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)