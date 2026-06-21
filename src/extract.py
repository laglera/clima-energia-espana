"""
Extracción de datos crudos desde las APIs externas:
- Open-Meteo: temperatura diaria por ciudad.
- ESIOS (REE): demanda eléctrica diaria.

Cada función debe devolver un DataFrame de pandas, sin transformar todavía
(eso es responsabilidad de transform.py).
"""
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Coordenadas de las ciudades que vamos a analizar.
# Puedes añadir más ciudades aquí en el formato (nombre, latitud, longitud).
CIUDADES = {
    "Madrid": (40.4168, -3.7038),
    "Sevilla": (37.3891, -5.9845),
    "Barcelona": (41.3874, 2.1686),
}


def obtener_temperatura(ciudad: str, fecha_inicio: str, fecha_fin: str) -> pd.DataFrame:
    """
    Descarga la temperatura diaria de una ciudad entre dos fechas usando
    la API de Open-Meteo (https://open-meteo.com/en/docs/historical-weather-api).

    Parámetros:
        ciudad: debe existir como clave en el diccionario CIUDADES.
        fecha_inicio / fecha_fin: formato "YYYY-MM-DD".

    Devuelve:
        DataFrame con columnas: fecha, ciudad, temp_media, temp_max, temp_min
    """
    lat, lon = CIUDADES[ciudad];
    
    url = "https://archive-api.open-meteo.com/v1/archive"

    parametros = {
    "latitude": lat,
    "longitude": lon,
    "start_date": fecha_inicio,
    "end_date": fecha_fin,
    "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Madrid",
}

    respuesta = requests.get(url, params=parametros)
    respuesta.raise_for_status()

    datos = respuesta.json()
    df = pd.DataFrame(datos["daily"])

    df = df.rename(columns={
    "time": "fecha",
    "temperature_2m_mean": "temp_media",
    "temperature_2m_max": "temp_max",
    "temperature_2m_min": "temp_min",
})
    df["ciudad"] = ciudad

    return df

def obtener_demanda_electrica(fecha_inicio: str, fecha_fin: str) -> pd.DataFrame:
    """
    Descarga la demanda eléctrica diaria de España usando la API de ESIOS.
    Requiere la variable de entorno ESIOS_TOKEN.

    Devuelve:
        DataFrame con columnas: fecha, demanda_mwh
    """
    token = os.getenv("ESIOS_TOKEN")
    # TODO 1: construir los headers de autenticación con el token
    #         (ESIOS usa el header "x-api-key")
    # TODO 2: elegir el indicador correcto en https://api.esios.ree.es/indicators
    #         (busca el indicador de "demanda real" o "demanda programada")
    # TODO 3: hacer la petición GET con el rango de fechas
    # TODO 4: convertir la respuesta JSON en un DataFrame de pandas
    raise NotImplementedError("Implementar obtener_demanda_electrica")


if __name__ == "__main__":
    # Prueba rápida manual mientras desarrollamos.
    df_temp = obtener_temperatura("Madrid", "2024-01-01", "2024-01-31")
    print(df_temp.head())
