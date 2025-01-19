import os
import sys
import numpy 
import pandas as pd
from src.exception import CustomException
import dill

def save_object(file_path,obj):
    try:
        dirpath = os.path.dirname(file_path)
        os.makedirs(dirpath,exist_ok=True)
        with open(file_path, 'wb') as file:
            dill.dump(obj,file)
    except Exception as e:
        raise CustomException(e,sys)