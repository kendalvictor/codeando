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

def reduce_size_data(df, category=False, default=''):
    print("Tamaño de uso actual : ", get_memory_usage(df))
    print("-> Int 64 Detected")
    for col in df.select_dtypes(include=['int']).columns:
        print(" "*4, col)
        df[col] = pd.to_numeric(arg=df[col], downcast=default or'integer')
    
    print("-> Float 64 Detected")
    for col in df.select_dtypes(include=['float']).columns:
        print(" "*4, col)
        df[col] = pd.to_numeric(arg=df[col], downcast=default or'float')
    
    if category:
        for col in df.select_dtypes(include=['object']).columns:
            if len(df[col].unique()) / len(df[col]) < 0.5:
                df[col] = df[col].astype('category')
                
    print("Tamaño de uso final : ", get_memory_usage(df))                
    return df


def  add_col_dates(data, col, format_match="%d-%b-%y", month=True, day=True, month_day=True,year=True,
                   weekday=True, replace_str=False, format_str_replace='%Y/%m/%d', replicate_in_test=False):
    """
        por optimizar en casos separados para data y test_data
    """
    data['date'] = pd.to_datetime(data[col], format=format_match)

    if month:
        data['month'] = pd.to_numeric(data['date'].dt.strftime('%m'), errors='coerce')
        data['month'].fillna(-99)  
    if day:
        data['day'] = pd.to_numeric(data['date'].dt.strftime('%d'), errors='coerce')
        data['day'].fillna(-99)
    if year:
        data['year'] = pd.to_numeric(data['date'].dt.strftime('%Y'), errors='coerce')
        data['year'].fillna(-99)
    if month_day:
        data['month_day'] = pd.to_numeric(data['date'].dt.strftime('%m%d'), errors='coerce')
        data['month_day'].fillna(-99)
    if weekday:
        data['weekday'] = pd.to_numeric(data['date'].dt.strftime('%w'), errors='coerce')
        data['weekday'].fillna(-99)
    if replace_str:
        data['date'] = data['date'].dt.strftime(format_str_replace)
        
    return(data.head(10))
