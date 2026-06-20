import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# CONFIGURACIÓN
# =========================

st.set_page_config(
    page_title="Highland Fish Dashboard",
    page_icon="🐟",
    layout="wide"
)

# =========================
# ESTILOS
# =========================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    background-color:#08264d;
}

.main{
    background-color:#f5f7fa;
}

.kpi-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.08);
    border-left:6px solid #08264d;
}

.titulo-principal{
    background:linear-gradient(90deg,#08264d,#1f4e8c);
    color:white;
    padding:30px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# DATOS
# =========================

ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7
margen = (ganancia / ventas) * 100

# Producción

produccion = pd.DataFrame({
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
           "Junio","Julio","Agosto","Setiembre",
           "Octubre","Noviembre"],
    "Produccion":[836.93,1824.78,3520.23,5561.56,
                  8142.31,9624.40,7743.87,10556.66,
                  13956.47,17195.07,19940.27]
})

# Mortalidad

mortalidad = pd.DataFrame({
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
           "Junio","Julio","Agosto","Setiembre",
           "Octubre","Noviembre"],
    "Mortalidad":[16.5,13.6,10.5,9.5,8.0,
                  6.1,3.2,3.2,2.8,2.6,2.1]
})

# Gastos

gastos_df = pd.DataFrame({
    "Concepto":["Alimento","Personal","Alevines","Gastos Generales"],
    "Monto":[98902.55,44555,10000,1850]
})

# Clientes

clientes_df = pd.DataFrame({
    "Cliente":["Nubeluz","Meri","Hotel Monasterio",
               "Nelly Acero","Enrique Barrantes",
               "Diego","Juana","Sonia","Giovana"],
    "Participacion":[20,9,3,7,10,23,12,9,7]
})

# Personal

personal = pd.DataFrame({
    "Cargo":["Operarios","Gerente",
             "Director de Operaciones",
             "Contador",
             "Ingeniero Pesquero"],
    "Sueldo":[8925,13000,11000,4000,7630]
})

# =========================
# SIDEBAR
# =========================

st.sidebar.markdown("""
<div style='text-align:center'>
<h1 style='font-size:70px'>🐟</h1>
<h2 style='color:white'>Highland Fish</h2>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

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

st.sidebar.markdown("---")

st.sidebar.success("Estado de la empresa: Excelente")

# =========================
# ENCABEZADO
# =========================

st.markdown("""
<div class='titulo-principal'>
<h1>🐟 Highland Fish</h1>
<h3>Panel Ejecutivo de Gestión</h3>
<p>Producción • Finanzas • Clientes • Personal</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# RESUMEN EJECUTIVO
# =========================

if menu == "Resumen Ejecutivo":

    st.header("📈 Indicadores Clave")

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.markdown(f"""
    <div class='kpi-card'>
    <small>Ventas Totales</small>
    <h2>S/ {ventas:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

    c2.markdown(f"""
    <div class='kpi-card'>
    <small>Gastos Totales</small>
    <h2>S/ {gastos:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

    c3.markdown(f"""
    <div class='kpi-card'>
    <small>Ganancia</small>
    <h2>S/ {ganancia:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

    c4.markdown(f"""
    <div class='kpi-card'>
    <small>Clientes</small>
    <h2>{clientes}</h2>
    </div>
    """, unsafe_allow_html=True)

    c5.markdown(f"""
    <div class='kpi-card'>
    <small>Margen</small>
    <h2>{margen:.1f}%</h2>
    </div>
    """, unsafe_allow_html=True)

    st.info("📌 La empresa mantiene una reducción constante de mortalidad y un margen de ganancia del 46%.")

    col1,col2 = st.columns(2)

    fig1 = px.line(
        produccion,
        x="Mes",
        y="Produccion",
        markers=True,
        title="Producción Mensual"
    )

    fig2 = px.line(
        mortalidad,
        x="Mes",
        y="Mortalidad",
        markers=True,
        title="Mortalidad (%)"
    )

    with col1:
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.plotly_chart(fig2, use_container_width=True)

# =========================
# PRODUCCIÓN
# =========================

elif menu == "Producción":

    st.header("🐟 Gestión de Producción")

    fig1 = px.line(
        produccion,
        x="Mes",
        y="Produccion",
        markers=True,
        title="Producción Mensual"
    )

    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(
        mortalidad,
        x="Mes",
        y="Mortalidad",
        markers=True,
        title="Mortalidad (%)"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(produccion)

# =========================
# FINANZAS
# =========================

elif menu == "Finanzas":

    st.header("💰 Gestión Financiera")

    col1,col2,col3 = st.columns(3)

    col1.metric("Ventas", f"S/ {ventas:,.0f}")
    col2.metric("Gastos", f"S/ {gastos:,.0f}")
    col3.metric("Ganancia", f"S/ {ganancia:,.0f}")

    fig3 = px.pie(
        gastos_df,
        names="Concepto",
        values="Monto",
        title="Distribución de Gastos"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.dataframe(gastos_df)

# =========================
# CLIENTES
# =========================

elif menu == "Clientes":

    st.header("👥 Gestión de Clientes")

    fig4 = px.pie(
        clientes_df,
        names="Cliente",
        values="Participacion",
        title="Participación de Clientes"
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.dataframe(clientes_df)

# =========================
# PERSONAL
# =========================

elif menu == "Personal":

    st.header("👨‍💼 Gestión de Personal")

    fig5 = px.bar(
        personal,
        x="Cargo",
        y="Sueldo",
        title="Costo por Cargo"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.dataframe(personal)
