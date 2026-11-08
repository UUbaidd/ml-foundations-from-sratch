import pandas as pd
import numpy as np
#Load data
def load_data(path):
    return pd.read_csv(path)


#validate data, Custom Validation
class DataValidationError(Exception):
    pass

def validate_schema(data,required_col, label_column = None, allowed_labels = None):
    if not isinstance(data,pd.DataFrame):
        raise ValueError("Data not in proper format")

    if allowed_labels is not None:
        for col in data[label_column]:
            if col not in allowed_labels:
                raise DataValidationError(f"{col} not allowed")
    
    col = data.columns

    for column in required_col:
        if column not in col:
            raise DataValidationError(f"Required column {column } is missing")
    

        if column != label_column and not pd.api.types.is_numeric_dtype(data[column]):
            raise DataValidationError(f"Column {column} dtype is not correct")

        if data[column].isna().any():
            raise DataValidationError(f"Column {column} has missing value")
        

# df = load_data("Fitness_data.csv")
data = {
    "Target RPE":[4,5,6],
    "MET": [3,2.3,4]
}
df = pd.DataFrame(data)

validate_schema(df, ["Target RPE","MET"])
