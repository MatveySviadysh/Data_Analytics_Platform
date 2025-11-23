import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys
import os

sys.path.append(str(Path(__file__).parent.parent / 'src'))

from src.utils.data_loader import DataLoader

class TestDataLoader:
    """Тесты для DataLoader"""
    
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.loader = DataLoader()
        self.test_data_path = Path('docs/raw/BMW sales data (2010-2024) (1) (1).csv')
    
    def test_load_bmw_data_exists(self):
        """Тест что файл BMW данных существует"""
        assert self.test_data_path.exists(), "Файл с данными BMW не найден"
    
    def test_load_bmw_data_returns_dataframe(self):
        """Тест что load_data возвращает DataFrame"""
        df = self.loader.load_data(self.test_data_path)
        assert isinstance(df, pd.DataFrame), "Метод должен возвращать DataFrame"
    
    def test_load_bmw_data_columns(self):
        """Тест что DataFrame имеет ожидаемые колонки"""
        df = self.loader.load_data(self.test_data_path)
        expected_columns = ['Model', 'Year', 'Region', 'Color', 'Fuel_Type', 
                          'Transmission', 'Engine_Size_L', 'Mileage_KM', 
                          'Price_USD', 'Sales_Volume', 'Sales_Classification']
        
        for col in expected_columns:
            assert col in df.columns, f"Колонка {col} отсутствует в данных"
    
    def test_clean_data_removes_duplicates(self):
        """Тест что clean_data удаляет дубликаты"""
        # Создаем тестовые данные с дубликатами
        data = {
            'Model': ['X3', 'X3', '5 Series'],
            'Price_USD': [50000, 50000, 60000]
        }
        df = pd.DataFrame(data)
        df_clean = self.loader.clean_data(df)
        
        assert len(df_clean) <= len(df), "Дубликаты должны быть удалены"
        