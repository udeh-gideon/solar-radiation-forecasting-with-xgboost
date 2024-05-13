import os
import urllib.request as request
import zipfile
from src.solar_radiation_prediction import logger
from src.solar_radiation_prediction.utils.common import get_size
from pathlib import Path
from src.solar_radiation_prediction.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"Successfully downloaded file: {filename} with the following info: {headers}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file} with filesize of: {get_size(self.config.local_data_file)}")
    
    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extracts the zip file to the specified data directory
        Function returns None
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)