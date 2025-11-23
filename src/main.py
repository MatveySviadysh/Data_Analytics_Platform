import pandas as pd
from utils.data_loader import DataLoader
from analysis.car_analysis import CarSalesAnalysis
from visualization.car_charts import CarCharts

def bmv():
    print("🚗 ЗАПУСК АНАЛИЗА ПРОДАЖ BMW...")
    
    loader = DataLoader()
    df = loader.load_data('docs/raw/BMW sales data (2010-2024) (1) (1).csv')
    
    print(f"✅ Загружено {len(df)} записей")
    
    analyzer = CarSalesAnalysis(df)
    analyzer.basic_info()
    
    print("\n🏆 ТОП МОДЕЛИ ПО ПРОДАЖАМ:")
    top_models = analyzer.sales_by_model(10)
    print(top_models)
    
    print("\n🌍 АНАЛИЗ ПО РЕГИОНАМ:")
    regions = analyzer.regional_analysis()
    print(regions)
    
    print("\n📈 СОЗДАЕМ ВИЗУАЛИЗАЦИИ...")
    charts = CarCharts(df)
    charts.plot_sales_by_model(10)
    charts.plot_price_distribution()
    charts.plot_regional_sales()
    
    print("✅ АНАЛИЗ ЗАВЕРШЕН!")

if __name__ == "__main__":
    bmv()