import pandas as pd

def load_data():
    """
    Carrega datasets fictícios de solo, clima e cultura.
    Retorna três DataFrames: soil, weather e crops.
    """
    soil = pd.read_csv('data/soil_data.csv')
    weather = pd.read_csv('data/wheater_data.csv')
    crops = pd.read_csv('data/crop_data.csv')
    return soil, weather, crops
