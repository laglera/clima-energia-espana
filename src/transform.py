"""
Limpieza y cruce de los datasets crudos generados por extract.py.
"""
import pandas as pd


def limpiar_temperatura(df: pd.DataFrame) -> pd.DataFrame:

    # Convertimos la columna fecha a un tipo de fecha real
    df["fecha"] = pd.to_datetime(df["fecha"])

    # Eliminamos duplicados
    df = df.drop_duplicates(subset=["fecha", "ciudad"])

    # En caso de valores nulos, calculamos un valor intermedio razonable
    df[["temp_media", "temp_max", "temp_min"]] = df[["temp_media", "temp_max", "temp_min"]].interpolate()

    return df

def limpiar_demanda(df: pd.DataFrame) -> pd.DataFrame:

    # Convertir la columna fecha a un tipo de fecha real
    df["fecha"] = pd.to_datetime(df["fecha"])
    
    # Extraemos la parte del dia de la fecha
    df["fecha"] = df["fecha"].dt.date

    # Agrupamos por ese dia y calculamos la media de demanda
    df = df.groupby("fecha", as_index=False)["demanda_mwh"].mean()

    return df

def cruzar_datasets(df_temp: pd.DataFrame, df_demanda: pd.DataFrame) -> pd.DataFrame:
    """
    Cruza temperatura y demanda por fecha.

    Nota: la demanda eléctrica de ESIOS es nacional, no por ciudad, así que
    el cruce será por fecha únicamente. Si quieres comparar varias ciudades,
    tendrás varias filas de temperatura por cada fila de demanda.
    """
    # TODO: usar pd.merge() con la columna fecha como clave
    raise NotImplementedError("Implementar cruzar_datasets")
