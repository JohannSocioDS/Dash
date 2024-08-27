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
variables_dashboard = ['Promueve_inclusion', 'Empresa_preparada_incluir',
                       'Cultura_organizacional_facilitaria', 'Infraestructura_adecuada',
                       'Liderazgo_Inclusivo ', 'Equipo', 'Capacitaciones_inclusion']

# Definir el orden de las categorías
orden_respuestas = ["Muy de acuerdo", "De acuerdo", "Ni de acuerdo ni en desacuerdo", "En desacuerdo", "Muy en desacuerdo"]

# Configuración del dashboard
st.title("Dashboard de Inclusión y Discapacidad")

#filtros
with st.sidebar:
    # Filtro de años
    parGenero = st.selectbox('Género.',options=IDATA['Género.'].unique(),index=0)
    # Filtro de Mes    
    parCargo = st.selectbox('Cargo ',options=IDATA['Cargo '].unique(),index=0)
    # Filtro de País
    parGrupoEtario = st.selectbox('Grupo_etario',options=IDATA['Grupo_etario'].unique())


c1,c2 = st.columns([60,40])
with c1:
     EmpresaCategoria = IDATA.groupby('Liderazgo_Inclusivo').agg({'Total':'sum'}).reset_index().sort_values(by='Total',ascending=False)
    fig = px.bar(IDATA, x='Liderazgo_Inclusivo',y='Porcentaje', title=f'Liderazgo inclusivo: {parGenero, parCargo, parGrupoEtario}', color='orden_respuesta',text_auto=',.0f')
    fig.update_layout(showlegend=False) #Determina si se muestra o no la leyenda
    st.plotly_chart(fig,use_container_width=True)
 
with c2:
    EmpresaCategoria = IDATA.groupby('Liderazgo_Inclusivo').agg({'Total':'sum'}).reset_index().sort_values(by='Total',ascending=False)
    fig = px.bar(IDATA, x='Liderazgo_Inclusivo',y='Porcentaje', title=f'Liderazgo inclusivo: {parGenero, parCargo, parGrupoEtario}', color='orden_respuesta',text_auto=',.0f')
    fig.update_layout(showlegend=False) #Determina si se muestra o no la leyenda
    st.plotly_chart(fig,use_container_width=True)
