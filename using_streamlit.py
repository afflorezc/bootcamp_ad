import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Nombre de la pestaña e icono
st.set_page_config(layout='centered', page_title='Talento Tech', page_icon=':smile:')

# Titulo de la página
t1, t2 = st.columns([0.3, 0.7])
t1.image('lorito.jpg')
t2.title('El lorito matemático')
t2.markdown('**Una función:** $$ \ln(x) + \exp(x^2) $$')

# Secciones
steps = st.tabs(['Seción 1', 'Sección 2', 'Sección 3', '$\sqrt{x^2+\ln(x) -\sin(x)}$', 'Sección 4', 'Sección 5'])
## Seccion 1.
with steps[0]:
    st.write('Los niños amarillos')
    st.image('canarios.jfif')

df = pd.read_csv('db_project.csv', sep=';', encoding='latin-1')
data = {'Nombre':['Fermina Daza', 'Juvenal Urbino', 'Florentino Ariza'],
        'Fecha de nacimiento': ['1997-02-21', '1996-05-03', '1987-04-17']}

table = pd.DataFrame(data)

with steps[1]:
    st.write('Base de datos del proyecto Bootcamp')
    st.dataframe(df)

with steps[2]:
    st.write('Cierta historia de A...')
    st.table(table)
    b1, b2 = st.columns([1, 1])

    text_zone =st.markdown('')

    if b1.button('Leer historia', use_container_width=True):
        text_zone.markdown('Deje el chisme parcero \n\nOk good! Aquí vamos :)\n\n Todo comenzó por alla en una fria noche de Febrero')
    if b2.button('Borrar', use_container_width=True):
        text_zone.markdown('Oh no!')
    
    st.selectbox('Ver los implicados', ['Fermina', 'Juvenal', 'Florentino'])

camp_df = pd.read_csv('Campanhas.csv', sep=';', encoding='latin-1')
met_df = pd.read_csv('Metricas.csv', sep=';', encoding='latin-1')
with steps[3]:
    st.write('Cargando otro csv: Campanhas.csv')
    camp = st.selectbox('Escoge un ID de campaña', camp_df['ID_Campana'], help='muestra campañas existentes')
    
    st.write('Metricas filtradas')
    m1, m2, m3 = st.columns([1,1,1])
    id1 = met_df[(met_df['ID_Campana']==camp) | met_df['ID_Campana'] ==  1]
    id2 = met_df[met_df['ID_Campana']==camp]

    m1.metric(label='Metrica 1', value= sum(id2['Conversiones']), 
              delta=str(sum(id2['Rebotes']))+ ' Número de rebotes',
              delta_color='inverse')
    
    m2.metric(label='Metrica 2', value=np.mean(id2['Clics']), 
              delta =str(np.mean(id2['Impresiones'])) + ' promedios',
              delta_color='inverse')

with steps[4]:
    st.write('Gráficos con Searnborn')
    id_camp = st.selectbox('Escoge ID campaña', met_df['ID_Campana'].unique())
    num_columns =['Clics', 'Impresiones', 'Tasa_Clics', 'Conversiones', 'Tasa_Conversion',
                  'Ingreso_Generado','Rebotes', 'Tasa_rebote']
    column = st.selectbox('Escoge la métrica', num_columns)
    data = met_df[met_df['ID_Campana']==id_camp]
    var_x = data['Fecha_Medicion']
    var_y = data[column]
    fig, ax = plt.subplots()
    ax = sns.lineplot(data=met_df, x=var_x, y=var_y, markers=True)
    st.pyplot(fig)

with steps[5]:
    df = pd.read_csv("https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso1/master/s03/dataVentas2009.csv")
    df.Fecha = pd.to_datetime(df.Fecha, format='%d/%m/%Y')
    df.set_index('Fecha', inplace=True)

    varx = st.selectbox('Escoge la variable x', df.columns)
    fig, ax = plt.subplots()
    ax = sns.histplot(data=df, x=varx, bins=20)
    st.pyplot(fig)