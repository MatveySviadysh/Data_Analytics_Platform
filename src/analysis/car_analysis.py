import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class CarSalesAnalysis:
    """Анализ продаж автомобилей"""
    
    def __init__(self, df):
        self.df = df
        self.setup_plotting()
    
    def setup_plotting(self):
        """Настройка визуализаций"""
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
    
    def basic_info(self):
        """Базовая информация о данных"""
        print("📊 БАЗОВАЯ ИНФОРМАЦИЯ:")
        print(f"Размер данных: {self.df.shape}")
        print(f"Столбцы: {list(self.df.columns)}")
        print(f"\nТипы данных:\n{self.df.dtypes}")
        return self.df.info()
    
    def sales_by_model(self, top_n=10):
        """Анализ продаж по моделям"""
        model_sales = self.df.groupby('Model').agg({
            'Sales_Volume': 'sum',
            'Price_USD': 'mean',
            'Year': 'mean'
        }).sort_values('Sales_Volume', ascending=False)
        
        return model_sales.head(top_n)
    
    def regional_analysis(self):
        """Анализ по регионам"""
        region_analysis = self.df.groupby('Region').agg({
            'Sales_Volume': 'sum',
            'Price_USD': 'mean',
            'Model': 'count'
        }).sort_values('Sales_Volume', ascending=False)
        
        return region_analysis