import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Highland Fish Dashboard",
    page_icon="🐟",
    layout="wide"
)

st.title("🐟 Highland Fish Dashboard")

# KPIs
ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7
margen = (ganancia / ventas) * 100

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Ventas", f"S/ {ventas:,.0f}")
c2.metric("Gastos", f"S/ {gastos:,.0f}")
c3.metric("Ganancia", f"S/ {ganancia:,.0f}")
c4.metric("Clientes", clientes)
c5.metric("Margen", f"{margen:.1f}%")

st.divider()

# Producción
produccion = pd.DataFrame({
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
           "Junio","Julio","Agosto","Setiembre",
           "Octubre","Noviembre"],
    "Produccion":[836.93,1824.78,3520.23,5561.56,
                  8142.31,9624.40,7743.87,10556.66,
                  13956.47,17195.07,19940.27]
})

fig1 = px.line(
    produccion,
    x="Mes",
    y="Produccion",
    markers=True,
    title="Producción Mensual"
)

st.plotly_chart(fig1, use_container_width=True)

# Mortalidad
mortalidad = pd.DataFrame({
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
           "Junio","Julio","Agosto","Setiembre",
           "Octubre","Noviembre"],
    "Mortalidad":[16.5,13.6,10.5,9.5,8.0,
                  6.1,3.2,3.2,2.8,2.6,2.1]
})

fig2 = px.line(
    mortalidad,
    x="Mes",
    y="Mortalidad",
    markers=True,
    title="Mortalidad (%)"
)

st.plotly_chart(fig2, use_container_width=True)

# Gastos
gastos_df = pd.DataFrame({
    "Concepto":["Alimento","Personal","Alevines","Gastos Generales"],
    "Monto":[98902.55,44555,10000,1850]
})

fig3 = px.pie(
    gastos_df,
    names="Concepto",
    values="Monto",
    title="Distribución de Gastos"
)

st.plotly_chart(fig3, use_container_width=True)

# Clientes
clientes_df = pd.DataFrame({
    "Cliente":["Nubeluz","Meri","Hotel Monasterio",
               "Nelly Acero","Enrique Barrantes",
               "Diego","Juana","Sonia","Giovana"],
    "Participacion":[20,9,3,7,10,23,12,9,7]
})

fig4 = px.pie(
    clientes_df,
    names="Cliente",
    values="Participacion",
    title="Participación de Clientes"
)

st.plotly_chart(fig4, use_container_width=True)

# Personal
personal = pd.DataFrame({
    "Cargo":["Operarios","Gerente",
             "Director de Operaciones",
             "Contador","Ingeniero Pesquero"],
    "Sueldo":[8925,13000,11000,4000,7630]
})

fig5 = px.bar(
    personal,
    x="Cargo",
    y="Sueldo",
    title="Costo por Cargo"
)

st.plotly_chart(fig5, use_container_width=True)
