import test_data_loader 
import pandas as pd
from data_loader import validate_schema, DataValidationError, load_data
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
     
def test_empty_data(tmp_path):
     file_path = tmp_path/"empty.csv"
     file_path.touch()
     with pytest.raises(pd.errors.EmptyDataError):
          load_data(file_path)
     


def test_invalid_labels():
     data = {
                    "MET":[3,4,5],
                    "Target RPE": [ 2,3,4],
                    "Fitness Goal" :	["Weight Loss", "Fitness Improvement", "General Health"]
               }
     
     label_col = "Fitness Goal"
     allowed_labels = [
    "Weight Loss",
    "Fitness Improvement",
    "Flying"
]
     df = pd.DataFrame(data)

     with pytest.raises(DataValidationError):
          validate_schema(df, ["Target RPE","MET", "Fitness Goal"],label_column=label_col,allowed_labels=allowed_labels)

def test_load_dataset(tmp_path):
     file_path = tmp_path / "valid.csv"

     data = {
        "MET": [3, 4, 5],
        "Target RPE": [2, 3, 4]
    }

    # Create DataFrame
     df = pd.DataFrame(data)

    # Save DataFrame as CSV
     df.to_csv(file_path, index=False)

    # Load CSV using our function
     loaded_df = load_data(file_path)

    # Compare original and loaded DataFrames
     pd.testing.assert_frame_equal(df, loaded_df)