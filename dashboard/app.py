"""
Dashboard interactivo: relación entre temperatura y demanda eléctrica.

Ejecutar con: streamlit run dashboard/app.py
"""
import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Clima y energía en España", layout="wide")
st.title("Clima y energía en España")


@st.cache_data
def cargar_datos() -> pd.DataFrame:
    engine = create_engine(os.getenv("DATABASE_URL"))
    # TODO: leer la tabla clima_demanda con pd.read_sql()
    raise NotImplementedError("Implementar cargar_datos en el dashboard")


# TODO: cargar los datos
# df = cargar_datos()

# TODO: selector de ciudad en la barra lateral (st.sidebar.selectbox)

# TODO: gráfica de evolución temporal de temperatura y demanda
#       (dos ejes Y, o dos gráficas apiladas con st.line_chart / plotly)

# TODO: KPI destacados arriba (st.metric): demanda media, temperatura media,
#       correlación entre ambas variables

st.info("Dashboard en construcción.")
