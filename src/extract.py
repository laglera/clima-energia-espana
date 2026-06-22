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
