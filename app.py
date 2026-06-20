import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(
    page_title="Highland Fish Dashboard",
    page_icon="🐟",
    layout="wide"
)

# ==========================================
# ESTILO
# ==========================================

st.markdown("""
<style>

.main{
    background-color:#f4f7fc;
}

[data-testid="stMetric"]{
    background-color:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 3px 8px rgba(0,0,0,0.1);
    border-left:8px solid #0A2342;
}

section[data-testid="stSidebar"]{
    background-color:#0A2342;
}

section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/1998/1998610.png",
    width=140
)

st.sidebar.title("Highland Fish")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📊 Navegación

🏠 Resumen Ejecutivo

🐟 Producción

💰 Finanzas

👥 Clientes

👨‍💼 Personal
""")

st.sidebar.markdown("---")

st.sidebar.success("Estado de la empresa: Excelente")

# ==========================================
# ENCABEZADO
# ==========================================

st.markdown("""
<div style="
background: linear-gradient(90deg,#0A2342,#1E4E8C);
padding:25px;
border-radius:15px;
margin-bottom:20px;
">

<h1 style="color:white;">
🐟 Highland Fish
</h1>

<h3 style="color:white;">
Panel Ejecutivo de Gestión
</h3>

<p style="color:white;">
Producción • Finanzas • Clientes • Personal
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# KPIS
# ==========================================

ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7
margen = ganancia / ventas * 100

st.header("📈 Indicadores Clave")

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric("Ventas Totales", f"S/ {ventas:,.0f}")
c2.metric("Gastos Totales", f"S/ {gastos:,.0f}")
c3.metric("Ganancia", f"S/ {ganancia:,.0f}")
c4.metric("Clientes", clientes)
c5.metric("Margen", f"{margen:.1f}%")

st.info(
    "📌 La empresa mantiene una reducción constante de mortalidad y un margen de ganancia de 46%."
)

st.divider()

# ==========================================
# PRODUCCIÓN Y MORTALIDAD
# ==========================================

produccion = pd.DataFrame({
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
           "Junio","Julio","Agosto","Setiembre",
           "Octubre","Noviembre"],
    "Producción":[
        836.93,
        1824.78,
        3520.23,
        5561.56,
        8142.31,
        9624.40,
        7743.87,
        10556.66,
        13956.47,
        17195.07,
        19940.27
    ]
})

mortalidad = pd.DataFrame({
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
           "Junio","Julio","Agosto","Setiembre",
           "Octubre","Noviembre"],
    "Mortalidad":[
        16.5,
        13.6,
        10.5,
        9.5,
        8.0,
        6.1,
        3.2,
        3.2,
        2.8,
        2.6,
        2.1
    ]
})

col1,col2 = st.columns(2)

with col1:

    fig1 = px.line(
        produccion,
        x="Mes",
        y="Producción",
        markers=True,
        title="Producción Mensual"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:

    fig2 = px.line(
        mortalidad,
        x="Mes",
        y="Mortalidad",
        markers=True,
        title="Mortalidad (%)"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ==========================================
# FINANZAS
# ==========================================

st.header("💰 Finanzas")

gastos_df = pd.DataFrame({
    "Concepto":[
        "Alimento",
        "Personal",
        "Alevines",
        "Gastos Generales"
    ],
    "Monto":[
        98902.55,
        44555,
        10000,
        1850
    ]
})

ventas_producto = pd.DataFrame({
    "Producto":[
        "Tres por Kg",
        "Retacos",
        "Dos kilos"
    ],
    "Ventas":[
        24461,
        6006,
        257062
    ]
})

col3,col4 = st.columns(2)

with col3:

    fig3 = px.pie(
        gastos_df,
        names="Concepto",
        values="Monto",
        hole=0.5,
        title="Distribución de Gastos"
    )

    st.plotly_chart(fig3, use_container_width=True)

with col4:

    fig4 = px.bar(
        ventas_producto,
        x="Producto",
        y="Ventas",
        title="Ventas por Producto"
    )

    st.plotly_chart(fig4, use_container_width=True)

# ==========================================
# CLIENTES Y PERSONAL
# ==========================================

st.header("👥 Clientes y Personal")

clientes_df = pd.DataFrame({
    "Cliente":[
        "Nubeluz",
        "Meri",
        "Hotel Monasterio",
        "Nelly Acero",
        "Enrique Barrantes",
        "Diego",
        "Juana",
        "Sonia",
        "Giovana"
    ],
    "Participación":[20,9,3,7,10,23,12,9,7]
})

personal = pd.DataFrame({
    "Cargo":[
        "Operarios",
        "Gerente",
        "Director Operaciones",
        "Contador",
        "Ingeniero Pesquero"
    ],
    "Costo":[
        8925,
        13000,
        11000,
        4000,
        7630
    ]
})

col5,col6 = st.columns(2)

with col5:

    fig5 = px.bar(
        clientes_df,
        x="Cliente",
        y="Participación",
        color="Participación",
        title="Participación de Clientes (%)"
    )

    st.plotly_chart(fig5, use_container_width=True)

with col6:

    fig6 = px.bar(
        personal,
        x="Cargo",
        y="Costo",
        color="Costo",
        title="Costo por Cargo"
    )

    st.plotly_chart(fig6, use_container_width=True)

# ==========================================
# TABLA EJECUTIVA
# ==========================================

st.header("📋 Resumen Ejecutivo")

resumen = pd.DataFrame({
    "Indicador":[
        "Ventas Totales",
        "Gastos Totales",
        "Ganancia",
        "Clientes",
        "Trabajadores",
        "Margen",
        "Mortalidad Final"
    ],
    "Valor":[
        "S/ 287,529",
        "S/ 155,308",
        "S/ 132,221",
        "9",
        "7",
        "46%",
        "2.1%"
    ]
})

st.dataframe(
    resumen,
    use_container_width=True
)

st.success("🐟 Dashboard Highland Fish actualizado correctamente")
