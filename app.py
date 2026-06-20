import streamlit as st
import pandas as pd
import plotly.express as px

# ===================================
# CONFIGURACIÓN
# ===================================

st.set_page_config(
    page_title="Highland Fish Dashboard",
    page_icon="🐟",
    layout="wide"
)

# ===================================
# ESTILOS
# ===================================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    background:#06244d;
}

.kpi-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.15);
    border-left:8px solid #0a2d62;
}

.titulo{
    background:linear-gradient(90deg,#06244d,#1f4f96);
    padding:30px;
    border-radius:20px;
    color:white;
}

.estado{
    background:#0d3b66;
    color:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ===================================
# DATOS
# ===================================

ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7
margen = (ganancia/ventas)*100

# ===================================
# SIDEBAR
# ===================================

st.sidebar.markdown("# 🐟")
st.sidebar.markdown("## Highland Fish")

menu = st.sidebar.radio(
    "Navegación",
    [
        "Resumen Ejecutivo",
        "Producción",
        "Finanzas",
        "Clientes",
        "Personal"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
<div class='estado'>
<h4>Estado Empresa</h4>
<h2>Excelente</h2>
</div>
""", unsafe_allow_html=True)

# ===================================
# ENCABEZADO
# ===================================

st.markdown("""
<div class='titulo'>
<h1>🐟 Highland Fish</h1>
<h2>Panel Ejecutivo de Gestión</h2>
<p>Piscicultura de trucha arcoíris en jaulas flotantes</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ===================================
# RESUMEN EJECUTIVO
# ===================================

if menu == "Resumen Ejecutivo":

    st.subheader("📊 Indicadores Clave")

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        st.markdown(f"""
        <div class='kpi-card'>
        <h5>Ventas</h5>
        <h2>S/ {ventas:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class='kpi-card'>
        <h5>Gastos</h5>
        <h2>S/ {gastos:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class='kpi-card'>
        <h5>Ganancia</h5>
        <h2>S/ {ganancia:,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class='kpi-card'>
        <h5>Clientes</h5>
        <h2>{clientes}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown(f"""
        <div class='kpi-card'>
        <h5>Margen</h5>
        <h2>{margen:.1f}%</h2>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.info(
        "La empresa presenta crecimiento sostenido de producción, disminución de mortalidad y un margen de ganancia del 46%."
    )

# ===================================
# PRODUCCIÓN
# ===================================

elif menu == "Producción":

    st.header("🐟 Producción")

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
        title="Evolución de Producción"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.success(
        "La producción aumentó desde 836 kg hasta casi 20 toneladas durante el periodo evaluado."
    )

# ===================================
# FINANZAS
# ===================================

elif menu == "Finanzas":

    st.header("💰 Finanzas")

    gastos_df = pd.DataFrame({
        "Concepto":["Alimento","Personal","Alevines","Gastos Generales"],
        "Monto":[98902.55,44555,10000,1850]
    })

    col1,col2 = st.columns(2)

    with col1:

        fig2 = px.pie(
            gastos_df,
            names="Concepto",
            values="Monto",
            hole=0.5,
            title="Distribución de Gastos"
        )

        st.plotly_chart(fig2,use_container_width=True)

    with col2:

        fig3 = px.bar(
            gastos_df,
            x="Concepto",
            y="Monto",
            title="Gasto por Concepto"
        )

        st.plotly_chart(fig3,use_container_width=True)

# ===================================
# CLIENTES
# ===================================

elif menu == "Clientes":

    st.header("👥 Clientes")

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

    st.plotly_chart(fig4,use_container_width=True)

# ===================================
# PERSONAL
# ===================================

elif menu == "Personal":

    st.header("👨‍💼 Personal")

    personal = pd.DataFrame({
        "Cargo":["Operarios",
                 "Gerente",
                 "Director de Operaciones",
                 "Contador",
                 "Ingeniero Pesquero"],
        "Sueldo":[8925,13000,11000,4000,7630]
    })

    fig5 = px.bar(
        personal,
        x="Cargo",
        y="Sueldo",
        title="Costo por Cargo"
    )

    st.plotly_chart(fig5,use_container_width=True)

    st.dataframe(personal, use_container_width=True)

# ===================================
# PIE
# ===================================

st.markdown("---")
st.caption("Dashboard Empresarial Highland Fish | Universidad Nacional Agraria La Molina")
