import pandas as pd
from sqlalchemy import create_engine

# Conexión a nuestra nueva base de datos
engine = create_engine('sqlite:///olist_database.db')

def generar_reporte_ingresos():
    print("📊 Generando reporte de ingresos por categoría...")
    
    # Esta consulta une 3 tablas: items, productos y la traducción de nombres
    query = """
    SELECT 
        t.product_category_name_english AS categoria,
        SUM(i.price) AS ingresos_totales,
        COUNT(i.order_id) AS cantidad_vendida
    FROM order_items i
    JOIN products p ON i.product_id = p.product_id
    JOIN product_category_name_translation t ON p.product_category_name = t.product_category_name
    GROUP BY categoria
    ORDER BY ingresos_totales DESC
    LIMIT 5;
    """
    
    df = pd.read_sql(query, con=engine)
    
    print("\n🏆 TOP 5 CATEGORÍAS POR INGRESOS:")
    print("-" * 40)
    print(df)
    print("-" * 40)

if __name__ == "__main__":
    generar_reporte_ingresos()