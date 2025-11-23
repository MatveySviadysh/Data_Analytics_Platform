import pytest
import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'src'))

from visualization.car_charts import CarCharts

class TestCarCharts:
    """Тесты для CarCharts"""
    
    def setup_method(self):
        """Создаем тестовые данные"""
        self.sample_data = pd.DataFrame({
            'Model': ['X3', '5 Series', '3 Series'],
            'Price_USD': [50000, 60000, 45000],
            'Sales_Volume': [100, 150, 200],
            'Region': ['Europe', 'Asia', 'North America']
        })
        
        self.charts = CarCharts(self.sample_data)
    
    def test_plot_sales_by_model_creates_plot(self):
        """Тест что plot_sales_by_model создает график"""
        try:
            self.charts.plot_sales_by_model(2)
            # Если не было исключения - тест пройден
            assert True
        except Exception as e:
            pytest.fail(f"Метод вызвал исключение: {e}")
    
    def test_plot_price_distribution_creates_plot(self):
        """Тест что plot_price_distribution создает график"""
        try:
            self.charts.plot_price_distribution()
            assert True
        except Exception as e:
            pytest.fail(f"Метод вызвал исключение: {e}")
    
    def test_plot_regional_sales_creates_plot(self):
        """Тест что plot_regional_sales создает график"""
        try:
            self.charts.plot_regional_sales()
            assert True
        except Exception as e:
            pytest.fail(f"Метод вызвал исключение: {e}")