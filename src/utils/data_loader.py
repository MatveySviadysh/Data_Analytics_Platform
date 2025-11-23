import pandas as pd
import numpy as np
from pathlib import Path
import requests
from io import StringIO

class DataLoader:
    @staticmethod
    def load_data(file_path):
        """Загрузка данных BMW"""
        file_path = Path(file_path)
        print(f"📁 Загружаем данные из: {file_path}")
        return pd.read_csv(file_path)
    
    @staticmethod
    def load_from_url(url):
        """Загрузка CSV по URL"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return pd.read_csv(StringIO(response.text))
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return None
    
    
    @staticmethod
    def clean_data(df):
        """Базовая очистка данных"""
        df = df.drop_duplicates()
        
        # Заполнение пропущенных значений(средним занчением)
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
        
        return df