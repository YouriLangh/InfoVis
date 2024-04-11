from os import path
from pathlib import Path
from urllib.request import urlretrieve

DATASET_URLS = {
    'Crime_Data_from_2010_to_2019.csv': "https://data.lacity.org/api/views/63jg-8b9z/rows.csv",
    'Crime_Data_from_2020_to_Present.csv': "https://data.lacity.org/api/views/2nrs-mtv8/rows.csv"
}


def fetch_datasets():
    data_path = Path(__file__).resolve().parents[2] / "data"
    for fn, url in DATASET_URLS.items():
        if path.exists(data_path / fn):
            print(f"Dataset {fn} already present")
        else:
            fetch_dataset(data_path, fn, url)
            print(f"Downloading {fn}")
            urlretrieve(url, data_path / fn)
