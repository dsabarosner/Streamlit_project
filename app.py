import pandas as pd
import streamlit as st
import plotly.express as px

# Leer los datos
car_df = pd.read_csv('vehicles_us.csv')
car_df.info()

# Opciones para los gráficos
st.header('Dataset de los anuncios de venta de autos')

x_data = st.radio('Selecciona los datos para graficar', ['odometer', 'cylinders'],
                  captions=['kilometraje', 'cilindrada'])
st.write('Seleccionaste:', x_data)

# Crear un histograma
st.header('Histograma')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Histograma del conjunto de datos de anuncios de venta de autos')
    if x_data == 'odometer':
        fig = px.histogram(car_df, x='odometer',
                           title='Distribución del kilometraje')
    else:
        fig = px.histogram(car_df, x='cylinders',
                           title='Distribución de los cilindros')
    st.plotly_chart(fig, use_container_width=True)

# Crear scatter plot
st.header('Gráfico de dispersión')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write(
        'Gráfico de dispersión del conjunto de datos de anuncios de venta de autos')
    if x_data == 'odometer':
        fig2 = px.scatter(car_df, x='odometer', y='price',
                          title='Distribución del precio según kilometraje')
    else:
        fig2 = px.scatter(car_df, x='cylinders', y='price',
                          title='Distribución del precio según los cilindros')
    st.plotly_chart(fig2, use_container_width=True)

# Crear distribucion comparando precios segun marca
st.header('Comparación de la distribución de precios según marcas')

marca1 = st.selectbox('Primera marca', car_df['model'].unique())
marca2 = st.selectbox('Segunda marca', car_df['model'].unique())

hist_button_model = st.button('Construir histograma de precios por marca')

if hist_button_model:
    marca1_df = car_df[car_df['model'] == marca1]
    marca2_df = car_df[car_df['model'] == marca2]

    marcas_df = pd.concat([marca1_df, marca2_df])

    fig3 = px.histogram(marcas_df, x='price', color='model',
                        title='Distribución de precios según marca')
    st.plotly_chart(fig3, use_container_width=True)
