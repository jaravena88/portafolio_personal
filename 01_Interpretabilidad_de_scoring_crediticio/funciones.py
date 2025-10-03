# Se importan librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#----------------------------------------------------------------------------------------------------------------------------------------
# 1. Función para detectar valores atípicos utilizando el rango intercuartílico
#----------------------------------------------------------------------------------------------------------------------------------------

def plot_boxplot_with_outliers(data, column_names, outlier_color, factor, figsize):
    """
    Grafica valores atípicos basados en el rango intercuartílico (IQR).
    
    Args:
        data: DataFrame de pandas que contiene los datos.
        column_names: Lista de nombres de columnas para graficar (string).
        outlier_color: Color para resaltar los valores atípicos (string).
        factor: Factor para calcular los límites de los valores atípicos (generalmente 1.5).
        figsize: Tamaño de la figura (por ejemplo (10, 6)).

    Returns:
        outliers_dict: Devuelve un diccionario con los outliers por variable ingresada.
    
    """
    num_plots = len(column_names)
    fig, axes = plt.subplots(num_plots, 1, figsize = figsize, squeeze = False)
    fig.tight_layout(pad = 4.0)

    outliers_dict = {}  # Diccionario para almacenar los outliers de cada columna

    for i, column_name in enumerate(column_names):
        ax = axes[i, 0]

        # Calcular los estadísticos clave
        Q1 = data[column_name].quantile(0.25)
        Q3 = data[column_name].quantile(0.75)
        IQR = Q3 - Q1

        # Calcular los límites para los valores atípicos
        lower_bound = Q1 - factor * IQR
        upper_bound = Q3 + factor * IQR

        # Crear un gráfico de diagrama de caja (boxplot)
        sns.boxplot(y = data[column_name], ax = ax, showfliers = False)
        ax.set_ylabel(column_name)
        ax.set_xlabel('Datos')

        # Resaltar los valores atípicos en un color diferente
        outliers = data[(data[column_name] < lower_bound) | (data[column_name] > upper_bound)]
        ax.scatter(y = outliers[column_name], x = [0] * len(outliers), color = outlier_color, label = 'Outliers')

        # Anotar los valores de límites y cuartiles en el gráfico
        ax.text(0.35, Q1 - 0.55, f'Q1: {Q1:.2f}', fontsize = 10)
        ax.text(0.35, Q3 + 0.3, f'Q3: {Q3:.2f}', fontsize = 10)
        ax.text(0.205, lower_bound, f'Límite Inferior: {lower_bound:.2f}', fontsize = 10)
        ax.text(0.205, upper_bound, f'Límite Superior: {upper_bound:.2f}', fontsize = 10)

        ax.legend()
        outliers_dict[column_name] = outliers  # Guardar los outliers de esta columna

    plt.show()
    #return outliers_dict

#----------------------------------------------------------------------------------------------------------------------------------------
# 2. Función para eliminar valores atípicos utilizando el rango intercuartílico
#----------------------------------------------------------------------------------------------------------------------------------------

def remove_outliers_iqr(data, variables):
    """
    Elimina valores atípicos basados en el rango intercuartílico (IQR).
    
    Args:
        data: Conjunto de datos (Dataframe).
        variables: Variables del Dataframe que se deben analizar.

    Returns:
        df: Devuelve nuevo dataframe sin valores atípicos para las variables ingresadas.
    
    """
    for col in variables:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
    
    return df

#----------------------------------------------------------------------------------------------------------------------------------------
# 3. Función para analizar la calidad de los datos
#----------------------------------------------------------------------------------------------------------------------------------------

def data_quality_analysis(data):
    """
    Realiza análisis exploratorio para ver la calidad de los datos.
    
    Args:
        data: Conjunto de datos (Dataframe).

    Returns:
        result_df: Devuelve dataframe con el resultado del análisis exploratorio.
    
    """
    # Crear un nuevo dataframe para almacenar los resultados
    result_df = pd.DataFrame(columns = ['Columna', 'Tipo de dato', 'Valores únicos', 'Valores nulos', '% nulos'])

    # Obtener información general del dataframe
    columns = data.columns
    data_types = data.dtypes.to_list()
    unique_values = [data[column].nunique() for column in columns]
    missing_values = [data[column].isnull().sum() for column in columns]
    perc_missing_values = [data[column].isnull().sum() / len(data) * 100 for column in columns]

    # Llenar el nuevo dataframe con los resultados
    result_df['Columna'] = columns
    result_df['Tipo de dato'] = data_types
    result_df['Valores únicos'] = unique_values
    result_df['Valores nulos'] = missing_values
    result_df['% nulos'] = perc_missing_values
    
    return result_df