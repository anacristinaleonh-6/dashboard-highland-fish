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
# ESTILOS
# ==========================================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    background-color:#06244d;
}

.kpi {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.15);
    text-align:center;
}

.titulo {
    background:linear-gradient(90deg,#06244d,#1f4f96);
    padding:25px;
    border-radius:15px;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# DATOS GENERALES
# ==========================================

ventas = 287529
gastos = 155307.55
ganancia = 132221
clientes = 9
trabajadores = 7

margen = (ganancia / ventas) * 100

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🐟 Highland Fish")

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

st.sidebar.success("Empresa Saludable")

# ==========================================
# CABECERA
# ==========================================

st.markdown("""
<div class='titulo'>
<h1>🐟 Highland Fish</h1>
<h3>Dashboard Ejecutivo Empresarial</h3>
<p>Piscicultura de Trucha Arcoíris</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================
# RESUMEN EJECUTIVO
# ==========================================

if menu == "Resumen Ejecutivo":

    st.header("📊 Indicadores Estratégicos")

    c1,c2,c3,c4,c5,c6 = st.columns(6)

    c1.metric("Ventas", f"S/ {ventas:,.0f}")
    c2.metric("Gastos", f"S/ {gastos:,.0f}")
    c3.metric("Ganancia", f"S/ {ganancia:,.0f}")
    c4.metric("Clientes", clientes)
    c5.metric("Trabajadores", trabajadores)
    c6.metric("Margen", f"{margen:.1f}%")

    st.markdown("---")

    metas = pd.DataFrame({
        "Indicador":["Producción","Margen"],
        "Meta":[20000,40],
        "Resultado":[19940,46]
    })

    fig_meta = px.bar(
        metas,
        x="Indicador",
        y=["Meta","Resultado"],
        barmode="group",
        title="Metas vs Resultados"
    )

    st.plotly_chart(
        fig_meta,
        use_container_width=True
    )

    st.success("""
    ✅ Producción creciente.

    ✅ Mortalidad reducida.

    ✅ Margen superior al 40%.

    ✅ Empresa rentable.

    ✅ Principal gasto: Alimentación.
    """)

# ==========================================
# PRODUCCIÓN
# ==========================================

elif menu == "Producción":

    st.header("🐟 Producción")

    produccion = pd.DataFrame({
        "Mes":["Enero","Febrero","Marzo","Abril","Mayo",
               "Junio","Julio","Agosto","Setiembre",
               "Octubre","Noviembre"],

        "Produccion":[
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

        fig1 = px.area(
            produccion,
            x="Mes",
            y="Produccion",
            title="Producción Mensual (kg)"
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

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.dataframe(
        produccion,
        use_container_width=True
    )

# ==========================================
# FINANZAS
# ==========================================

elif menu == "Finanzas":

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

    col1,col2 = st.columns(2)

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

# ==========================================
# CLIENTES
# ==========================================

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

# ==========================================
# PERSONAL
# ==========================================

elif menu == "Personal":

    st.header("👨‍💼 Personal")

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

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Highland Fish | Dashboard Ejecutivo 2025 | Universidad Nacional Agraria La Molina"
)
