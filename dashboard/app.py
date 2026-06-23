import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import plotly.graph_objects as go

load_dotenv()

st.set_page_config(page_title="Clima y energía en España", layout="wide")
st.title("Clima y energía en España")


@st.cache_data
def cargar_datos() -> pd.DataFrame:
    engine = create_engine(os.getenv("DATABASE_URL"))
    df = pd.read_sql("SELECT * FROM clima_demanda", engine)
    return df

df = cargar_datos()

ciudades_disponibles = df["ciudad"].unique()
ciudad_seleccionada = st.sidebar.selectbox("Selecciona una ciduad", ciudades_disponibles)

df_filtrado = df[df["ciudad"] == ciudad_seleccionada]

df_filtrado = df_filtrado.sort_values("fecha")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_filtrado["fecha"], y=df_filtrado["temp_media"],
    name="Temperatura media (°C)", yaxis="y1"
))

fig.add_trace(go.Scatter(
    x=df_filtrado["fecha"], y=df_filtrado["demanda_mwh"],
    name="Demanda eléctrica (MWh)", yaxis="y2"
))

fig.update_layout(
    title=f"Temperatura vs Demanda eléctrica — {ciudad_seleccionada}",
    yaxis=dict(title="Temperatura (°C)"),
    yaxis2=dict(title="Demanda (MWh)", overlaying="y", side="right"),
)

st.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Temperatura media", f"{df_filtrado['temp_media'].mean():.1f} °C")

with col2:
    st.metric("Demanda media", f"{df_filtrado['demanda_mwh'].mean():,.0f} MWh")

with col3:
    correlacion = df_filtrado["temp_media"].corr(df_filtrado["demanda_mwh"])
    st.metric("Correlación temp-demanda", f"{correlacion:.2f}")



st.info("Dashboard en construcción.")
