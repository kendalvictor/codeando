#calculo
import numpy as np
import pandas as pd

#grafico
import matplotlib.pyplot as plt

set_parameter_csv = {
    'sep': ',',
    'encoding': 'ISO-8859-1',
    'low_memory': False
}

def get_memory_usage(data, deep=True):
    return '{} MB'.format(data.memory_usage(deep=deep).sum() / 1024 ** 2)

def null_verificator(data):        
    if data.isnull().any().any():
        view_info = pd.DataFrame(
            pd.concat(
                [data.isnull().any(), 
                 data.isnull().sum(),
                 data.dtypes], 
                axis=1)
        )
        view_info.columns = ['Nulos', 'Cantidad', 'Tipo Col']
        return view_info
    else:
        return "DATA LIMPIA DE NULOS"

def reduce_size_data(df):
    for col in df.select_dtypes(include=['int']).columns:
        df[col] = df[col].apply(pd.to_numeric, downcast='integer')
 
    for col in df.select_dtypes(include=['float']).columns:
        df[col] = df[col].apply(pd.to_numeric, downcast='float')

    for col in df.select_dtypes(include=['object']).columns:
        if len(df[col].unique()) / len(df[col]) < 0.5:
            df[col] = df[col].astype('category')

