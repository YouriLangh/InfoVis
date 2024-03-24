import pandas as pd
from datetime import time as dtime

class DataSchema:
    DATETIME = "DATETIME OCC"
    DATE = "DATE OCC"
    TIME = "TIME OCC"
    AREA = "AREA NAME"
    CRM_CD = "Crm Cd"
    CRM_TYPE = "Crm Cd Desc"
    VICT_AGE = "Vict Age"
    VICT_SEX = "Vict Sex"
    VICT_DES = "Vict Descent"
    PREM = "Premis Desc"
    WEAPON = "Weapon Desc"
    CRM_CD_1 = "Crm Cd 1"
    CRM_CD_2 = "Crm Cd 2"
    LOCATION = "LOCATION"
    LAT = "LAT"
    LON = "LON"

dtype_dict = {
    DataSchema.AREA: 'object',
    DataSchema.CRM_CD: 'float64',
    DataSchema.CRM_TYPE: 'object',
    DataSchema.VICT_AGE: 'float64',
    DataSchema.VICT_SEX: 'object',
    DataSchema.VICT_DES: 'object',
    DataSchema.PREM: 'object',
    DataSchema.WEAPON: 'object',
    DataSchema.CRM_CD_1: 'float64',
    DataSchema.CRM_CD_2: 'float64',
    DataSchema.LOCATION: 'object',  
    DataSchema.LAT: 'float',  
    DataSchema.LON: 'float'  
}


# Define a function to parse time column separately
def parse_time_column(series):
    return pd.to_datetime(series, format='%H:%M:%S', errors='coerce').dt.time

def load_combined_data(path: str) -> pd.DataFrame:
    chunk_size = 100000
    # Read CSV file in chunks
    chunks = pd.read_csv(path, chunksize=chunk_size, dtype=dtype_dict)
    
    # Process each chunk and concatenate
    df_list = []
    for chunk in chunks:
        chunk["DATE OCC"] = pd.to_datetime(chunk["DATE OCC"])
        chunk["DATETIME OCC"] = pd.to_datetime(chunk["DATETIME OCC"])
        chunk["TIME OCC"] = parse_time_column(chunk["TIME OCC"])
        df_list.append(chunk)
    
    # Concatenate all chunks into a single DataFrame
    df = pd.concat(df_list, ignore_index=True)
    return df