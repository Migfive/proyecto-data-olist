import pandas as pd
from sqlalchemy import create_engine
import os

# Configuración de la Base de Datos SQLite (se creará este archivo)
engine = create_engine('sqlite:///olist_database.db')

def cargar_datos():
    # Listar solo archivos CSV en la carpeta actual
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    
    if not files:
        print("❌ No se encontraron archivos CSV. Asegúrate de estar en la carpeta correcta.")
        return

    print("🚀 Iniciando proceso de ingesta de datos...")
    print("-" * 50)

    for file in files:
        # Limpiamos el nombre del archivo para que la tabla sea legible
        table_name = file.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
        
        try:
            print(f"📦 Procesando: {file}...")
            
            # Cargamos el CSV a un DataFrame de Pandas
            df = pd.read_csv(file)
            
            # Enviamos el DataFrame a SQL
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)
            
            print(f"✅ Tabla '{table_name}' creada con {len(df)} registros.")
            
        except Exception as e:
            print(f"⚠️ Error al procesar {file}: {e}")

    print("-" * 50)
    print("✨ ¡Proceso completado! La base de datos 'olist_database.db' está lista.")

if __name__ == "__main__":
    cargar_datos()