import OOP.data_Validation.test_data_loader as test_data_loader 
import pandas as pd
from OOP.data_Validation.data_loader import validate_schema, DataValidationError, load_data
import pytest
import numpy as np
def test_valid_schema():
    data = {
        "Target RPE": [4,5,6],
        "MET":[4.5,6.8,8.0]
    }
    df = pd.DataFrame(data)
    validate_schema(df,["Target RPE", "MET"])



def test_missing_col():
    
    
    data = {
        "MET":[4,5,6]

    }
    df = pd.DataFrame(data)
    with pytest.raises(DataValidationError):
            validate_schema(df, ["Target RPE","MET"])

def test_incorrect_dtype():

     data = {
          "MET":["5",4,5],
          "Target RPE": [ 2,3,4]
     }
     df = pd.DataFrame(data)
     with pytest.raises(DataValidationError):
          validate_schema(df, ["Target RPE","MET"])

def test_missing_values():
     data = {
               "MET":[3,4,np.nan],
               "Target RPE": [ 2,3,4]
          }
     df = pd.DataFrame(data)
     with pytest.raises(DataValidationError):
          validate_schema(df, ["Target RPE","MET"])

def test_load_data(tmp_path):
     pass