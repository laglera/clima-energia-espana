import pandas as pd

from src.extract import obtener_temperatura, obtener_demanda_electrica, CIUDADES
from src.transform import limpiar_temperatura, limpiar_demanda, cruzar_datasets
from src.load import cargar_datos

FECHA_INICIO = "2024-01-01"
FECHA_FIN = "2024-12-31"


def ejecutar_pipeline():

    print("1/5 Extrayendo temperaturas...")
    dfs_temperatura = []
    for ciudad in CIUDADES:
        df_ciudad = obtener_temperatura(ciudad, FECHA_INICIO, FECHA_FIN)
        dfs_temperatura.append(df_ciudad)

    df_temp = pd.concat(dfs_temperatura)

    print("2/5 Extrayendo demanda eléctrica...")
    df_demanda = obtener_demanda_electrica(FECHA_INICIO, FECHA_FIN)

    print("3/5 Limpiando datos...")
    df_temp = limpiar_temperatura(df_temp)
    df_demanda = limpiar_demanda(df_demanda)

    print("4/5 Cruzando datasets...")
    df_final = cruzar_datasets(df_temp, df_demanda)

    print("5/5 Cargando en PostgreSQL...")
    print(df_final.head())
    print(f"Total de filas: {len(df_final)}")

    print("Pipeline completado.")


if __name__ == "__main__":
    ejecutar_pipeline()
