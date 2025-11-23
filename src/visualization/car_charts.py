import matplotlib.pyplot as plt
import seaborn as sns

class CarCharts:
    """Визуализации для автомобильных данных"""
    
    def __init__(self, df):
        self.df = df
        self.setup_style()
    
    def setup_style(self):
        """Настройка стиля графиков"""
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
    
    def plot_sales_by_model(self, top_n=10):
        """График продаж по моделям"""
        model_sales = self.df.groupby('Model')['Sales_Volume'].sum().sort_values(ascending=False).head(top_n)
        
        plt.figure(figsize=(12, 6))
        model_sales.plot(kind='bar')
        plt.title(f'Топ-{top_n} моделей по объему продаж')
        plt.xlabel('Модель')
        plt.ylabel('Объем продаж')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_price_distribution(self):
        """Распределение цен"""
        plt.figure(figsize=(10, 6))
        plt.hist(self.df['Price_USD'], bins=30, alpha=0.7, edgecolor='black')
        plt.title('Распределение цен на BMW')
        plt.xlabel('Цена ($)')
        plt.ylabel('Количество')
        plt.show()
    
    def plot_regional_sales(self):
        """Продажи по регионам"""
        region_sales = self.df.groupby('Region')['Sales_Volume'].sum().sort_values(ascending=False)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Столбчатая диаграмма
        region_sales.plot(kind='bar', ax=ax1)
        ax1.set_title('Продажи по регионам')
        ax1.set_ylabel('Объем продаж')
        ax1.tick_params(axis='x', rotation=45)
        
        # Круговая диаграмма
        region_sales.plot(kind='pie', ax=ax2, autopct='%1.1f%%')
        ax2.set_title('Доля продаж по регионам')
        
        plt.tight_layout()
        plt.show()