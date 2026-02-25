import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import os
# Conexión
# Nombre de la base de datos local en el servidor
DB_NAME = 'olist_database.db'
engine = create_engine(f'sqlite:///{DB_NAME}')

@st.cache_resource # Esto evita que se ingeste cada vez que muevas un filtro
def inicializar_datos():
    if not os.path.exists(DB_NAME):
        files = [f for f in os.listdir('.') if f.endswith('.csv')]
        if files:
            for file in files:
                table_name = file.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
                df = pd.read_csv(file)
                df.to_sql(table_name, con=engine, if_exists='replace', index=False)
            return "Datos cargados"
    return "Base de datos ya existente"

inicializar_datos()

st.set_page_config(page_title="Olist Data Coordinator Dashboard", layout="wide")
st.title("📊 Dashboard de Control - Olist Store")
st.markdown("### Análisis Estratégico para Toma de Decisiones")

# Consulta de Ingresos (lo que ya hicimos)
query = """
SELECT 
    t.product_category_name_english AS categoria,
    SUM(i.price) AS ingresos_totales
FROM order_items i
JOIN products p ON i.product_id = p.product_id
JOIN product_category_name_translation t ON p.product_category_name = t.product_category_name
GROUP BY categoria
ORDER BY ingresos_totales DESC
LIMIT 10;
"""

df = pd.read_sql(query, con=engine)

# Crear Gráfico con Plotly
fig = px.bar(df, x='categoria', y='ingresos_totales', 
             title="Top 10 Categorías por Ingresos",
             labels={'ingresos_totales':'Ingresos ($)', 'categoria':'Categoría'},
             color='ingresos_totales')

st.plotly_chart(fig, use_container_width=True)

# Mostrar tabla de datos maestros
if st.checkbox('Mostrar Datos Maestros de Productos'):
    st.write(pd.read_sql("SELECT * FROM products LIMIT 10", con=engine))
    
st.divider()
st.subheader("🛡️ Reporte de Gobernanza y Calidad")

# Consulta para detectar valores nulos en columnas críticas de pedidos
query_calidad = """
SELECT 
    COUNT(*) as total_pedidos,
    SUM(CASE WHEN order_delivered_customer_date IS NULL THEN 1 ELSE 0 END) as entregas_pendientes,
    SUM(CASE WHEN order_approved_at IS NULL THEN 1 ELSE 0 END) as sin_aprobacion_pago
FROM orders
"""

df_calidad = pd.read_sql(query_calidad, con=engine)

col1, col2, col3 = st.columns(3)
col1.metric("Total Registros", df_calidad['total_pedidos'][0])
col2.metric("Entregas Pendientes (Nulos)", df_calidad['entregas_pendientes'][0])
col3.metric("Sin Aprobación", df_calidad['sin_aprobacion_pago'][0])

st.info("💡 Este panel permite al Coordinador de Datos identificar inconsistencias en el flujo transaccional y aplicar reglas de limpieza (Data Cleansing).")


st.divider()
st.subheader("🌍 Distribución Geográfica por Estado")

# Consulta de ventas por estado
query_geo = """
SELECT 
    customer_state AS estado,
    SUM(i.price) AS ventas
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items i ON o.order_id = i.order_id
GROUP BY estado
ORDER BY ventas DESC
"""

df_geo = pd.read_sql(query_geo, con=engine)

# Gráfico de barras por estado
fig_geo = px.bar(df_geo, x='estado', y='ventas', 
                 title="Ventas Totales por Estado (Brasil)",
                 color='ventas',
                 color_continuous_scale='Viridis')

st.plotly_chart(fig_geo, use_container_width=True)


st.divider()
st.subheader("🔍 Filtro por Estado (Gobernanza de Ventas)")

# Selector de Estado
estados = df_geo['estado'].unique()
estado_seleccionado = st.selectbox("Selecciona un estado para ver el detalle:", estados)

# Consulta detallada para el estado seleccionado
query_detalle = f"""
SELECT 
    c.customer_city as ciudad, 
    COUNT(o.order_id) as pedidos, 
    SUM(i.price) as total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items i ON o.order_id = i.order_id
WHERE c.customer_state = '{estado_seleccionado}'
GROUP BY ciudad
ORDER BY total DESC
LIMIT 10
"""

df_detalle = pd.read_sql(query_detalle, con=engine)
st.write(f"Top ciudades en {estado_seleccionado}:")
st.table(df_detalle)