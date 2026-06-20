import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACIÓN
st.set_page_config(
    page_title="Highland Fish Dashboard",
    page_icon="🐟",
    layout="wide"
)

# -----------------------------
# DATOS PRINCIPALES
# -----------------------------

ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7
margen = (ganancia / ventas) * 100

# -----------------------------
# MENÚ LATERAL
# -----------------------------

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3075/3075977.png",
    width=120
)

st.sidebar.title("Highland Fish")

pagina = st.sidebar.radio(
    "Navegación",
    [
        "🏠 Resumen Ejecutivo",
        "🐟 Producción",
        "💰 Finanzas",
        "👥 Clientes",
        "👨‍💼 Personal"
    ]
)

# =====================================================
# RESUMEN
# =====================================================

if pagina == "🏠 Resumen Ejecutivo":

    st.title("🐟 Highland Fish")
    st.subheader("Panel Ejecutivo de Gestión")

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric("Ventas", f"S/ {ventas:,.0f}")
    c2.metric("Gastos", f"S/ {gastos:,.0f}")
    c3.metric("Ganancia", f"S/ {ganancia:,.0f}")
    c4.metric("Clientes", clientes)
    c5.metric("Margen", f"{margen:.1f}%")

    st.divider()

    col1,col2 = st.columns(2)

    produccion = pd.DataFrame({
        "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
               "Junio","Julio","Agosto","Setiembre",
               "Octubre","Noviembre"],
        "Produccion":[836.93,1824.78,3520.23,5561.56,
                      8142.31,9624.40,7743.87,
                      10556.66,13956.47,
                      17195.07,19940.27]
    })

    mortalidad = pd.DataFrame({
        "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
               "Junio","Julio","Agosto","Setiembre",
               "Octubre","Noviembre"],
        "Mortalidad":[16.5,13.6,10.5,9.5,8.0,
                      6.1,3.2,3.2,2.8,2.6,2.1]
    })

    with col1:
        fig1 = px.line(
            produccion,
            x="Mes",
            y="Produccion",
            title="Producción Mensual",
            markers=True
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.line(
            mortalidad,
            x="Mes",
            y="Mortalidad",
            title="Mortalidad (%)",
            markers=True
        )
        st.plotly_chart(fig2, use_container_width=True)

# =====================================================
# PRODUCCIÓN
# =====================================================

elif pagina == "🐟 Producción":

    st.header("🐟 Producción")

    produccion = pd.DataFrame({
        "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
               "Junio","Julio","Agosto","Setiembre",
               "Octubre","Noviembre"],
        "Produccion":[836.93,1824.78,3520.23,5561.56,
                      8142.31,9624.40,7743.87,
                      10556.66,13956.47,
                      17195.07,19940.27]
    })

    fig = px.line(
        produccion,
        x="Mes",
        y="Produccion",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# FINANZAS
# =====================================================

elif pagina == "💰 Finanzas":

    st.header("💰 Finanzas")

    gastos_df = pd.DataFrame({
        "Concepto":["Alimento","Personal",
                    "Alevines","Gastos Generales"],
        "Monto":[98902.55,44555,10000,1850]
    })

    fig = px.pie(
        gastos_df,
        names="Concepto",
        values="Monto"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# CLIENTES
# =====================================================

elif pagina == "👥 Clientes":

    st.header("👥 Clientes")

    clientes_df = pd.DataFrame({
        "Cliente":["Diego","Nubeluz","Juana",
                   "Enrique Barrantes",
                   "Meri","Sonia",
                   "Nelly Acero",
                   "Giovana",
                   "Hotel Monasterio"],
        "Participacion":[23,20,12,10,9,9,7,7,3]
    })

    fig = px.bar(
        clientes_df,
        x="Participacion",
        y="Cliente",
        orientation="h"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# PERSONAL
# =====================================================

elif pagina == "👨‍💼 Personal":

    st.header("👨‍💼 Personal")

    personal = pd.DataFrame({
        "Cargo":["Operarios",
                 "Gerente",
                 "Director de Operaciones",
                 "Contador",
                 "Ingeniero Pesquero"],
        "Costo":[8925,13000,11000,4000,7630]
    })

    st.dataframe(personal)

    fig = px.bar(
        personal,
        x="Cargo",
        y="Costo"
    )

    st.plotly_chart(fig, use_container_width=True)
