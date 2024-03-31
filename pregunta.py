"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def space_remove(text):
    pattern = re.compile(r'\s+')
    text = re.sub(pattern = pattern, repl= ' ',string = text)
    text = re.sub(r'\.', repl= '',string = text)
    return text


def percentage_remove(text):
    pattern = re.compile(r'(\d+),(\d+)\s%')
    text = re.sub(pattern=pattern, repl=r'\1.\2', string=text)
    text = float(text)
    return text


def ingest_data():

    df = pd.read_fwf("clusters_report.txt", skiprows=4, header = None)
    
    df.columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    
    df['principales_palabras_clave']=df.ffill().groupby('cluster')['principales_palabras_clave'].transform(lambda x: ' '.join(x))
    
    df=df.dropna().reset_index(drop=True)
    
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(space_remove)
    
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].apply(percentage_remove)

    return df
