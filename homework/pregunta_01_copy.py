"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os

def convertir_a_formato_fecha(fecha):
    try:
        return pd.to_datetime(fecha, format = '%d/%m/%Y')
    except:
        return pd.to_datetime(fecha, format = '%Y/%m/%d')


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    
    # Crear la carpeta "output" si no existe
    output_dir = 'files/output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Leer el archivo
    data = pd.read_csv('files/input/solicitudes_de_credito.csv', sep = ';', index_col=0)
    df = data.copy()

    # Analizar dataset:
    df_info = df.info()  # Resumen de columnas, tipos de datos y valores nulos
    df_describe = df.describe().transpose()  # Estadísticas descriptivas para columnas numéricas
    df_head = df.head()  # Primeras filas del dataset
    df_columns = df.columns  # Lista de nombres de columnas

    # Eliminar columnas nulas:
    df = df.dropna()
    #df = df.drop(columns=["Unnamed: 0"])
    df = df.drop_duplicates()

    # Analizar columnas:
    # Columna 'sexo': Género del solicitante
    # Convertir los valores de la columna 'sexo' a minúsculas
    df['sexo'] = df['sexo'].str.lower()

    # Columna 'tipo_de_emprendimiento': Tipo de emprendimiento del solicitante
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()

    # Columna 'idea_negocio': Idea de negocio del solicitante
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.replace('[-_]', ' ')

    # Columna 'barrio': Barrio del solicitante
    df['barrio'] = df['barrio'].str.lower()
    df['barrio'] = df['barrio'].str.replace('[-_]', ' ')

    # Columna 'Linea de negocio': Línea de negocio del solicitante
    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace('[-_]', ' ')

    # Columna 'Comuna ciudadano': Comuna del solicitante
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    # Columna 'Estrato': Estrato del solicitante
    df["estrato"] = df["estrato"].astype(int)

    #  Columna 'fecha_de_beneficio': Fecha de beneficio del solicitante
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(convertir_a_formato_fecha)

    # Guardar dataset limpio:
    df.to_csv('files/output/solicitudes_de_credito.csv', sep = ';', index = False)

    # Columna 'monto_del_credito': Monto del crédito solicitado
    df["monto_del_credito"] = df["monto_del_credito"].str.replace( r"[^\d.]", "", regex=True)
    df["monto_del_credito"] = pd.to_numeric(df["monto_del_credito"], errors="coerce")


if __name__ == '__main__':
    pregunta_01()
