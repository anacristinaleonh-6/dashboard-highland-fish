import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# ==========================
# CONFIGURACIÓN
# ==========================

st.set_page_config(
    page_title="Highland Fish Dashboard",
    page_icon="🐟",
    layout="wide"
)

# ==========================
# LOGO
# ==========================

logo = Image.open("imagenes/logo.png")

# ==========================
# ESTILOS
# ==========================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    background-color:#06244d;
}

.main{
    background-color:#f5f7fa;
}

.kpi{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
    border-left:8px solid #06244d;
}

.header-box{
    background:linear-gradient(90deg,#06244d,#1f4f96);
    padding:25px;
    border-radius:20px;
    color:white;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# DATOS
# ==========================

ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7

margen = (ganancia / ventas) * 100

# ==========================
# SIDEBAR
# ==========================

st.sidebar.image(logo, use_container_width=True)

menu = st.sidebar.radio(
    "📊 Navegación",
    [
        "Resumen Ejecutivo",
        "Producción",
        "Finanzas",
        "Clientes",
        "Personal"
    ]
)

st.sidebar.success("🟢 Empresa saludable")

# ==========================
# HEADER
# ==========================

c1, c2 = st.columns([1,5])

with c1:
    st.image(logo, width=140)

with c2:

    st.markdown("""
    <div class='header-box'>
        <h1>Highland Fish</h1>
        <h3>Dashboard Ejecutivo Empresarial</h3>
        <p>Producción de trucha arcoíris en jaulas flotantes</p>
    </div>
    """, unsafe_allow_html=True)
    # ==========================
# PRODUCCIÓN
# ==========================

produccion = pd.DataFrame({
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
           "Junio","Julio","Agosto","Setiembre",
           "Octubre","Noviembre"],
    "Produccion":[836.93,1824.78,3520.23,5561.56,
                  8142.31,9624.40,7743.87,10556.66,
                  13956.47,17195.07,19940.27]
})

mortalidad = pd.DataFrame({
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
           "Junio","Julio","Agosto","Setiembre",
           "Octubre","Noviembre"],
    "Mortalidad":[16.5,13.6,10.5,9.5,8.0,
                  6.1,3.2,3.2,2.8,2.6,2.1]
})
if menu == "Resumen Ejecutivo":

    st.header("📊 Indicadores Estratégicos")

    k1,k2,k3,k4,k5 = st.columns(5)

    with k1:
        st.markdown(f"""
        <div class='kpi'>
        <h5>Ventas</h5>
        <h2>S/ {ventas:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class='kpi'>
        <h5>Gastos</h5>
        <h2>S/ {gastos:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class='kpi'>
        <h5>Ganancia</h5>
        <h2>S/ {ganancia:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class='kpi'>
        <h5>Clientes</h5>
        <h2>{clientes}</h2>
        </div>
        """, unsafe_allow_html=True)

    with k5:
        st.markdown(f"""
        <div class='kpi'>
        <h5>Margen</h5>
        <h2>{margen:.1f}%</h2>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    c1,c2 = st.columns(2)

    with c1:

        fig1 = px.area(
            produccion,
            x="Mes",
            y="Produccion",
            title="Producción Mensual"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with c2:

        fig2 = px.line(
            mortalidad,
            x="Mes",
            y="Mortalidad",
            markers=True,
            title="Mortalidad (%)"
        )

        st.plotly_chart(fig2, use_container_width=True)

    st.success("""
    ✅ Producción creciente.

    ✅ Mortalidad controlada.

    ✅ Margen superior al 40%.

    ✅ Empresa rentable.
    """)
    elif menu == "Producción":

    st.header("🐟 Producción")

    fig = px.line(
        produccion,
        x="Mes",
        y="Produccion",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(produccion, use_container_width=True)

elif menu == "Finanzas":

    st.header("💰 Finanzas")

    gastos_df = pd.DataFrame({
        "Concepto":["Alimento","Personal",
                    "Alevines","Gastos Generales"],
        "Monto":[98902.55,44555,10000,1850]
    })

    c1,c2 = st.columns(2)

    with c1:

        fig = px.pie(
            gastos_df,
            names="Concepto",
            values="Monto",
            hole=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    with c2:

        fig = px.bar(
            gastos_df,
            x="Concepto",
            y="Monto"
        )

        st.plotly_chart(fig, use_container_width=True)

elif menu == "Clientes":

    st.header("👥 Clientes")

    clientes_df = pd.DataFrame({
        "Cliente":["Diego","Nubeluz","Juana",
                   "Enrique Barrantes","Meri",
                   "Sonia","Giovana",
                   "Nelly Acero",
                   "Hotel Monasterio"],
        "Participacion":[23,20,12,10,9,9,7,7,3]
    })

    fig = px.bar(
        clientes_df,
        x="Cliente",
        y="Participacion",
        color="Participacion"
    )

    st.plotly_chart(fig, use_container_width=True)

elif menu == "Personal":

    st.header("👨‍💼 Personal")

    personal = pd.DataFrame({
        "Cargo":["Gerente",
                 "Director de Operaciones",
                 "Operarios",
                 "Ingeniero Pesquero",
                 "Contador"],
        "Sueldo":[13000,11000,8925,7630,4000]
    })

    fig = px.bar(
        personal,
        x="Cargo",
        y="Sueldo",
        color="Sueldo"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.markdown("""
<div class='footer'>
Highland Fish © 2025<br>
Dashboard Ejecutivo Empresarial<br>
Universidad Nacional Agraria La Molina
</div>
""", unsafe_allow_html=True)
