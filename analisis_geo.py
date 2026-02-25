import pandas as pd
from sqlalchemy import create_engine

# Conexión
engine = create_engine('sqlite:///olist_database.db')

def reporte_geografico():
    print("🌍 Analizando distribución geográfica de ventas...")
    
    # Query que une Clientes, Pedidos e Ítems
    query = """
    SELECT 
        c.customer_city AS ciudad,
        c.customer_state AS estado,
        SUM(i.price) AS ventas_totales,
        COUNT(DISTINCT c.customer_id) AS clientes_unicos
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items i ON o.order_id = i.order_id
    GROUP BY ciudad, estado
    ORDER BY ventas_totales DESC
    LIMIT 10;
    """
    
    df = pd.read_sql(query, con=engine)
    
    print("\n📍 TOP 10 CIUDADES POR FACTURACIÓN:")
    print("-" * 50)
    # Formateamos los números para que se vean profesionales
    df['ventas_totales'] = df['ventas_totales'].apply(lambda x: f"${x:,.2f}")
    print(df)
    print("-" * 50)

if __name__ == "__main__":
    reporte_geografico()