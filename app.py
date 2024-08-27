conda to install openpyxl

import pandas as pd
import streamlit as st
import plotly.express as px


# Cargar los datos (reemplaza 'ruta/a/tu/archivo.xlsx' con la ruta real)
IDATA = pd.read_excel('IPY_Encuesta Diagnóstica sobre Inclusión y Discapacidad.xlsx')

# Reemplazar valores numéricos por etiquetas de texto
for column in IDATA.columns:
    if IDATA[column].dtype == 'int64':
        IDATA[column] = IDATA[column].replace({1: 'Muy en desacuerdo',
                                               2: 'En desacuerdo',
                                               3: 'Ni de acuerdo ni en desacuerdo',
                                               4: 'De acuerdo',
                                               5: 'Muy de acuerdo'})

# Variables para el dashboard
variables_dashboard = ['Grupo_etario', 'Género.', 'Cargo ',
                       'Promueve_inclusion', 'Empresa_preparada_incluir',
                       'Cultura_organizacional_facilitaria', 'Infraestructura_adecuada',
                       'Liderazgo_Inclusivo ', 'Equipo', 'Capacitaciones_inclusion']

# Título del dashboard
st.title("Dashboard de Inclusión y Discapacidad")

# Crear un gráfico para cada variable
for variable in variables_dashboard:
    st.subheader(f"Análisis de {variable}")
    
    # Contar las respuestas
    conteo = IDATA[variable].value_counts()
    
    # Crear un gráfico de barras interactivo con Plotly
    fig = px.bar(conteo, x=conteo.index, y=conteo.values, 
                 labels={'x': variable, 'y': 'Cantidad de Respuestas'})
    st.plotly_chart(fig)

