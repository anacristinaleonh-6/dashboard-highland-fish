import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# =====================================
# CONFIGURACIÓN DE PÁGINA
# =====================================

st.set_page_config(
    page_title="Highland Fish Dashboard",
    page_icon="🐟",
    layout="wide"
)

# =====================================
# CARGAR LOGO
# =====================================

logo = Image.open("imagenes/logo.png")

# =====================================
# ESTILOS POWER BI
# =====================================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    background-color:#06244d;
}

.main{
    background-color:#f5f7fa;
}

.titulo-box{
    background: linear-gradient(90deg,#06244d,#1f4f96);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:20px;
}

.kpi{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.15);
    border-left:8px solid #06244d;
}

.estado{
    background:#0d3b66;
    padding:15px;
    border-radius:15px;
    color:white;
    text-align:center;
}

.conclusion{
    background:#e8f4ff;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #1f4f96;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# DATOS REALES
# =====================================

ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7
margen = (ganancia / ventas) * 100

# =====================================
# SIDEBAR
# =====================================

st.sidebar.image(logo, use_container_width=True)

st.sidebar.markdown("## Highland Fish")

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

st.sidebar.markdown("""
<div class='estado'>
<h4>Estado de la Empresa</h4>
<h2>Excelente</h2>
</div>
""", unsafe_allow_html=True)

# =====================================
# ENCABEZADO PRINCIPAL
# =====================================

col_logo, col_titulo = st.columns([1,4])

with col_logo:
    st.image(logo, width=140)

with col_titulo:

    st.markdown("""
    <div class='titulo-box'>
    <h1>Highland Fish</h1>
    <h3>Panel Ejecutivo de Gestión</h3>
    <p>Piscicultura de trucha arcoíris en jaulas flotantes</p>
    </div>
    """, unsafe_allow_html=True)
    # =========================
# DATOS REALES HIGHLAND FISH
# =========================

ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7
margen = (ganancia / ventas) * 100

# =========================
# TARJETAS KPI
# =========================

st.markdown("## 📊 Indicadores Estratégicos")

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <h4>Ventas Totales</h4>
        <h2>S/ {ventas:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-card">
        <h4>Gastos Totales</h4>
        <h2>S/ {gastos:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-card">
        <h4>Ganancia Neta</h4>
        <h2>S/ {ganancia:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi-card">
        <h4>Clientes</h4>
        <h2>{clientes}</h2>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
    <div class="kpi-card">
        <h4>Margen</h4>
        <h2>{margen:.1f}%</h2>
    </div>
    """, unsafe_allow_html=True)

st.info(
    "📌 Highland Fish mantiene una tendencia positiva de crecimiento productivo y una reducción sostenida de mortalidad."
)

st.markdown("---")

# =========================
# DATOS DE PRODUCCIÓN
# =========================

produccion = pd.DataFrame({
    "Mes":[
        "Enero","Febrero","Marzo","Abril","Mayo",
        "Junio","Julio","Agosto","Setiembre",
        "Octubre","Noviembre"
    ],
    "Produccion":[
        836.93,1824.78,3520.23,5561.56,
        8142.31,9624.40,7743.87,10556.66,
        13956.47,17195.07,19940.27
    ]
})

mortalidad = pd.DataFrame({
    "Mes":[
        "Enero","Febrero","Marzo","Abril","Mayo",
        "Junio","Julio","Agosto","Setiembre",
        "Octubre","Noviembre"
    ],
    "Mortalidad":[
        16.5,13.6,10.5,9.5,8.0,
        6.1,3.2,3.2,2.8,2.6,2.1
    ]
})

# =========================
# GRÁFICOS PRINCIPALES
# =========================

st.markdown("## 🐟 Producción y Mortalidad")

col1, col2 = st.columns(2)

with col1:

    fig1 = px.area(
        produccion,
        x="Mes",
        y="Produccion",
        title="Producción Mensual (kg)"
    )

    fig1.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=450
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = px.line(
        mortalidad,
        x="Mes",
        y="Mortalidad",
        markers=True,
        title="Mortalidad (%)"
    )

    fig2.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=450
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")
# =====================================
# FINANZAS
# =====================================

if menu == "Finanzas":

    st.header("💰 Gestión Financiera")

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

    col1, col2 = st.columns(2)

    with col1:

        fig3 = px.pie(
            gastos_df,
            names="Concepto",
            values="Monto",
            hole=0.5,
            title="Distribución de Gastos"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    with col2:

        fig4 = px.bar(
            gastos_df,
            x="Concepto",
            y="Monto",
            color="Concepto",
            title="Comparación de Gastos"
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

    st.dataframe(
        gastos_df,
        use_container_width=True
    )

# =====================================
# CLIENTES
# =====================================

elif menu == "Clientes":

    st.header("👥 Clientes")

    clientes_df = pd.DataFrame({

        "Cliente":[
            "Diego",
            "Nubeluz",
            "Juana",
            "Enrique Barrantes",
            "Meri",
            "Sonia",
            "Giovana",
            "Nelly Acero",
            "Hotel Monasterio"
        ],

        "Participación":[
            23,
            20,
            12,
            10,
            9,
            9,
            7,
            7,
            3
        ]

    })

    fig5 = px.bar(
        clientes_df,
        x="Cliente",
        y="Participación",
        color="Participación",
        title="Participación de Clientes (%)"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    st.dataframe(
        clientes_df,
        use_container_width=True
    )

# =====================================
# PERSONAL
# =====================================

elif menu == "Personal":

    st.header("👨‍💼 Gestión de Personal")

    personal = pd.DataFrame({

        "Cargo":[
            "Gerente",
            "Director de Operaciones",
            "Operarios",
            "Ingeniero Pesquero",
            "Contador"
        ],

        "Sueldo":[
            13000,
            11000,
            8925,
            7630,
            4000
        ]

    })

    fig6 = px.bar(
        personal,
        x="Cargo",
        y="Sueldo",
        color="Sueldo",
        title="Costo por Cargo"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

    st.dataframe(
        personal,
        use_container_width=True
    )

# =====================================
# RESUMEN EJECUTIVO
# =====================================

elif menu == "Resumen Ejecutivo":

    st.header("📋 Resumen General")

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

    st.subheader("🎯 Objetivos Estratégicos")

    objetivos = pd.DataFrame({

        "Indicador":[
            "Producción",
            "Mortalidad",
            "Margen"
        ],

        "Meta":[
            20000,
            5,
            40
        ],

        "Actual":[
            19940,
            2.1,
            46
        ]

    })

    st.dataframe(
        objetivos,
        use_container_width=True
    )

    st.subheader("📌 Conclusiones Ejecutivas")

    st.success("""
    ✅ La producción aumentó desde 836 kg hasta 19 940 kg.

    ✅ La mortalidad disminuyó de 16.5% a 2.1%.

    ✅ El margen de ganancia alcanzó 46%.

    ✅ El principal gasto corresponde a alimentación.

    ✅ La empresa mantiene rentabilidad positiva.

    ✅ El cliente con mayor participación es Diego (23%).
    """)

# =====================================
# PIE DE PÁGINA
# =====================================

st.markdown("---")

st.markdown("""
<div style='text-align:center;color:gray'>

Highland Fish © 2025

Dashboard Ejecutivo Empresarial

Universidad Nacional Agraria La Molina

</div>
""", unsafe_allow_html=True)
