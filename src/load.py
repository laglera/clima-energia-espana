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

    engine = obtener_engine()
    df.to_sql(nombre_tabla, engine, if_exists="replace", index=False)
    print(f"Datos cargados en la tabla '{nombre_tabla}' ({len(df)} filas).")
