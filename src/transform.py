"""
Limpieza y cruce de los datasets crudos generados por extract.py.
"""
import pandas as pd


def limpiar_temperatura(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el DataFrame de temperatura: tipos de datos correctos,
    valores nulos, posibles duplicados por fecha/ciudad.
    """
    # TODO: convertir columna fecha a datetime
    # TODO: eliminar duplicados (mismo día y ciudad)
    # TODO: decidir qué hacer con valores nulos (imputar o descartar)
    raise NotImplementedError("Implementar limpiar_temperatura")


def limpiar_demanda(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el DataFrame de demanda eléctrica.
    """
    # TODO: convertir columna fecha a datetime
    # TODO: revisar outliers (picos imposibles de demanda)
    raise NotImplementedError("Implementar limpiar_demanda")


def cruzar_datasets(df_temp: pd.DataFrame, df_demanda: pd.DataFrame) -> pd.DataFrame:
    """
    Cruza temperatura y demanda por fecha.

    Nota: la demanda eléctrica de ESIOS es nacional, no por ciudad, así que
    el cruce será por fecha únicamente. Si quieres comparar varias ciudades,
    tendrás varias filas de temperatura por cada fila de demanda.
    """
    # TODO: usar pd.merge() con la columna fecha como clave
    raise NotImplementedError("Implementar cruzar_datasets")
