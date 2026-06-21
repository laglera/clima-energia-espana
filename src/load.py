"""
Carga del DataFrame final (limpio y cruzado) en PostgreSQL.
"""
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


def obtener_engine():
    """Crea el engine de SQLAlchemy a partir de DATABASE_URL en .env."""
    url = os.getenv("DATABASE_URL")
    return create_engine(url)


def cargar_datos(df: pd.DataFrame, nombre_tabla: str = "clima_demanda") -> None:
    """
    Carga el DataFrame en la tabla indicada. Si la tabla ya existe,
    la reemplaza (válido para este proyecto, no para producción real).
    """
    engine = obtener_engine()
    # TODO: usar df.to_sql(nombre_tabla, engine, if_exists="replace", index=False)
    raise NotImplementedError("Implementar cargar_datos")
