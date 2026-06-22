import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Coordenadas de las ciudades que vamos a analizar.
CIUDADES = {
    "Madrid": (40.4168, -3.7038),
    "Sevilla": (37.3891, -5.9845),
    "Barcelona": (41.3874, 2.1686),
}

# La funcion recibe tres parametros, ciudad, fecha de inicio y fecha de fin
def obtener_temperatura(ciudad: str, fecha_inicio: str, fecha_fin: str) -> pd.DataFrame:

    # Buscamos en el diccionario CIUDADES la tupla de coordenadas correspondiente al nombre de la ciudad
    lat, lon = CIUDADES[ciudad];
    
    # Guardamos en una variable (url) la direccion de la API
    url = "https://archive-api.open-meteo.com/v1/archive"

    # Creamos un diccionario con todos los paramentros que la API va a recibir
    parametros = {
    "latitude": lat,
    "longitude": lon,
    "start_date": fecha_inicio,
    "end_date": fecha_fin,
    "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Madrid",
}
    # requests crea la URL uniendo url con parametros, y guarda el resultados de la peticion en (respuesta)
    respuesta = requests.get(url, params=parametros)
    respuesta.raise_for_status()

    # Convertimos el texto de la respuesta (formato JSON) en estructura Python (Diccionario)
    datos = respuesta.json()
    # Del diccionario datos solo nos interesa la parte "daily"
    df = pd.DataFrame(datos["daily"])

    # Renombramos las columnas que vienen con los nombres tecnicos de la API
    df = df.rename(columns={
    "time": "fecha",
    "temperature_2m_mean": "temp_media",
    "temperature_2m_max": "temp_max",
    "temperature_2m_min": "temp_min",
})
    # Añadimos una columna ciudad
    df["ciudad"] = ciudad

    # Devolvemos el DataFrame ya limpio
    return df

# La funcion recibe dos parametros, fecha de inicio y fecha de fin
def obtener_demanda_electrica(fecha_inicio: str, fecha_fin: str) -> pd.DataFrame:

    token = os.getenv("ESIOS_TOKEN")

    headers = {
        "Accept": "application/json; application/vnd.esios-api-v1+json",
        "Content-Type": "application/json",
        "x-api-key": token,
    }

    url = "https://api.esios.ree.es/indicators/1293"

    rangos = pd.date_range(start=fecha_inicio, end=fecha_fin, freq="MS")

    dfs = []
    for inicio_mes in rangos:
        fin_mes = inicio_mes + pd.offsets.MonthEnd(0)
        # No nos pasamos del fecha_fin real que pidió el usuario.
        fin_mes = min(fin_mes, pd.to_datetime(fecha_fin))

        parametros = {
            "start_date": inicio_mes.strftime("%Y-%m-%d"),
            "end_date": fin_mes.strftime("%Y-%m-%d"),
        }

        respuesta = requests.get(url, headers=headers, params=parametros)
        respuesta.raise_for_status()

        datos = respuesta.json()
        df_mes = pd.DataFrame(datos["indicator"]["values"])
        dfs.append(df_mes)

    df = pd.concat(dfs, ignore_index=True)

    df = df.rename(columns={
        "datetime": "fecha",
        "value": "demanda_mwh",
    })
    df = df[["fecha", "demanda_mwh"]]

    return df
if __name__ == "__main__":
    # Prueba rápida manual mientras desarrollamos.
    df_temp = obtener_temperatura("Madrid", "2024-01-01", "2024-01-31")
    print(df_temp.head())
