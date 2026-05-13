import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.header('Análisis de Anuncios de Venta de Vehículos')
st.write('Explora el dataset de anuncios de venta de coches en EE.UU.')

# --- HISTOGRAMA ---
st.subheader('Distribución del Odómetro')

hist_check = st.checkbox('Construir histograma')

if hist_check:
    st.write('Distribución del kilometraje de los vehículos en venta')
    fig_hist = px.histogram(car_data, x='odometer',
                            title='Distribución del Odómetro',
                            labels={'odometer': 'Odómetro (millas)'},
                            color_discrete_sequence=['steelblue'])
    st.plotly_chart(fig_hist, use_container_width=True)

# --- GRÁFICO DE DISPERSIÓN ---
st.subheader('Precio vs Odómetro')

scatter_check = st.checkbox('Construir gráfico de dispersión')

if scatter_check:
    st.write('Relación entre el kilometraje y el precio de venta')
    fig_scatter = px.scatter(car_data, x='odometer', y='price',
                             title='Precio vs Odómetro',
                             labels={'odometer': 'Odómetro (millas)',
                                     'price': 'Precio (USD)'},
                             opacity=0.4,
                             color_discrete_sequence=['tomato'])
    st.plotly_chart(fig_scatter, use_container_width=True)