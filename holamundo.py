# holamundo.py
import pandas as pd

def obtener_mensaje():
    # Crear un DataFrame con una sola columna que contenga el mensaje
    data = {'Mensaje': ['Hello, World!']}
    df = pd.DataFrame(data)
    return df
