import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar los datos
@st.cache
def load_data():
    return pd.read_excel('IPY_Encuesta Diagnóstica sobre Inclusión y Discapacidad.xlsx')

IDATA = load_data()

# Reemplazar valores numéricos por etiquetas de texto
for column in IDATA.columns:
    if IDATA[column].dtype == 'int64':
        IDATA[column] = IDATA[column].replace({
            1: 'Muy en desacuerdo',
            2: 'En desacuerdo',
            3: 'Ni de acuerdo ni en desacuerdo',
            4: 'De acuerdo',
            5: 'Muy de acuerdo'
        })

# Variables para el dashboard
var_in = ['Grupo_etario', 'Género.', 'Cargo ']
variables_dashboard = ['Promueve_inclusion', 'Empresa_preparada_incluir',
                       'Cultura_organizacional_facilitaria', 'Infraestructura_adecuada',
                       'Liderazgo_Inclusivo ', 'Equipo', 'Capacitaciones_inclusion']

# Definir el orden de las categorías
orden_respuestas = ["Muy de acuerdo", "De acuerdo", "Ni de acuerdo ni en desacuerdo", "En desacuerdo", "Muy en desacuerdo"]

# Configuración del dashboard
st.title("Dashboard de Inclusión y Discapacidad")

# Seleccionar la variable independiente
var_select = st.selectbox('Selecciona una variable para analizar:', var_in)

# Crear gráficos para cada variable del dashboard
for variable in variables_dashboard:
    st.subheader(f"Análisis de {variable} según {var_select}")

    # Contar las respuestas agrupadas por la variable seleccionada
    conteo = IDATA.groupby([var_select, variable]).size().unstack().fillna(0)
    conteo = conteo[orden_respuestas].apply(lambda x: x / x.sum() * 100, axis=1)  # Convertir a porcentaje

    # Crear gráfico de barras apiladas
    fig = px.bar(conteo, x=conteo.index, y=orden_respuestas, 
                 title=f'Porcentaje de Respuestas para {variable} según {var_select}',
                 labels={'value': 'Porcentaje', 'index': var_select},
                 text_auto=True)
    fig.update_layout(yaxis=dict(tickformat='%'))
    st.plotly_chart(fig)

