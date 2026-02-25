# 📊 E-Commerce Data Governance & Strategic Analytics Pipeline (Olist)

Este proyecto implementa una infraestructura de datos de extremo a extremo (End-to-End) diseñada para centralizar, gobernar y analizar la operación de **Olist**, el ecosistema de e-commerce más grande de Brasil. Se transformaron **1.2 millones de registros** dispersos en archivos CSV en un **Data Warehouse Relacional** para la toma de decisiones gerenciales.



---

## 🛠️ Pilares Técnicos del Proyecto

### 1. Arquitectura e Ingeniería de Datos (ETL)
Se diseñó un pipeline de ingesta automatizado utilizando **Python** y **SQLAlchemy**:
* **Extracción:** Procesamiento masivo de 9 datasets transaccionales complejos.
* **Transformación:** Normalización de esquemas, limpieza de tipos de datos y manejo de nulos.
* **Carga:** Migración estructurada hacia un motor **SQLite**, optimizando la integridad referencial y la velocidad de consulta.

### 2. Gestión de Datos Maestros (MDM) y Gobernanza
Cumpliendo con los estándares de **Coordinación de Datos**, se implementó:
* **Integridad Referencial:** Vinculación estricta entre clientes, pedidos y productos mediante llaves primarias/foráneas.
* **Calidad de Datos:** Identificación de inconsistencias en registros de entrega y aprobación de pagos.
* **Estandarización:** Unificación de catálogos mediante el mapeo de categorías de productos (Portugués a Inglés).

### 3. Business Intelligence & Dashboards
Desarrollo de un panel interactivo con **Streamlit** y **Plotly** enfocado en KPIs estratégicos:
* **Facturación por Categoría:** Análisis de Pareto para identificar productos líderes en ingresos.
* **Inteligencia Geoespacial:** Mapeo de densidad de ventas por Estado y Ciudad para optimización logística.
* **Monitor de Operaciones:** Seguimiento de estados de pedidos en tiempo real.

---

## 📊 Insights Estratégicos Identificados

* **Dominio de Mercado:** El estado de **São Paulo (SP)** genera la mayor facturación (~$1.9M), lo que justifica la priorización de hubs logísticos en esta zona.
* **Rentabilidad:** La categoría *Health & Beauty* presenta un ticket promedio superior, liderando en ingresos totales frente a categorías con mayor volumen de unidades vendidas.



---

## ⚙️ Configuración y Ejecución

Siga estos pasos para replicar el entorno de análisis:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Migfive/proyecto-data-olist.git](https://github.com/Migfive/proyecto-data-olist.git)
   cd proyecto-data-olist

---

## 🚀 Vista Previa del Proyecto
![Dashboard Preview](/dashboard_producto.png)

## 🎈 App desplegada
![https://proyecto-data-olist-cir5zjvmucmhttv3onxhgf.streamlit.app/](https://proyecto-data-olist-cir5zjvmucmhttv3onxhgf.streamlit.app/)