"""
Orquesta el pipeline completo: extracción -> transformación -> carga.

Ejecutar con: python -m src.pipeline
"""
import pandas as pd

from src.extract import obtener_temperatura, obtener_demanda_electrica, CIUDADES
from src.transform import limpiar_temperatura, limpiar_demanda, cruzar_datasets
from src.load import cargar_datos

FECHA_INICIO = "2024-01-01"
FECHA_FIN = "2024-12-31"


def ejecutar_pipeline():
    print("1/5 Extrayendo temperaturas...")
    # TODO: llamar a obtener_temperatura() para cada ciudad en CIUDADES
    #       y concatenar los resultados en un único DataFrame con pd.concat()

    print("2/5 Extrayendo demanda eléctrica...")
    # TODO: llamar a obtener_demanda_electrica()

    print("3/5 Limpiando datos...")
    # TODO: llamar a limpiar_temperatura() y limpiar_demanda()

    print("4/5 Cruzando datasets...")
    # TODO: llamar a cruzar_datasets()

    print("5/5 Cargando en PostgreSQL...")
    # TODO: llamar a cargar_datos()

    print("Pipeline completado.")


if __name__ == "__main__":
    ejecutar_pipeline()
