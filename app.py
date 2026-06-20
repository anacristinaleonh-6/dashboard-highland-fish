import streamlit as st
import pandas as pd
import plotly.express as px


# =====================================================
# CONFIGURACION
# =====================================================

st.set_page_config(
    page_title="Highland Fish",
    page_icon="🐟",
    layout="wide"
)



# =====================================================
# CSS
# =====================================================

st.markdown("""

<style>

[data-testid="stSidebar"]{
background:#06244d;
}

[data-testid="stSidebar"] *{
color:white !important;
}


.hero{

background:linear-gradient(90deg,#06244d,#1f4f96);

padding:30px;

border-radius:20px;

color:white;

margin-bottom:20px;

}


[data-testid="metric-container"]{

background:white;

padding:15px;

border-radius:15px;

box-shadow:0px 4px 12px rgba(0,0,0,0.12);

border-left:5px solid #1f4f96;

}


#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}


header{
visibility:hidden;
}

</style>

""",unsafe_allow_html=True)



# =====================================================
# DATOS GENERALES
# =====================================================


ventas=9067500

utilidad=2357500

clientes=46

trabajadores=76

produccion=604500

mortalidad=1.98

fcr=1.40




# =====================================================
# SIDEBAR
# =====================================================


st.sidebar.markdown("# 🐟 Highland Fish")

st.sidebar.markdown("### Dashboard 2026")


menu = st.sidebar.radio(

"Navegación",

[

"Resumen Ejecutivo",

"Producción",

"Finanzas",

"Clientes",

"Productos",

"Personal",

"KPIs Estratégicos",

"Planeamiento Estratégico",

"Proyección"

]

)


st.sidebar.success("Empresa Sostenible")




# =====================================================
# CABECERA
# =====================================================



st.markdown("""

<div class='hero'>


<h1>🐟 Highland Fish S.A.C.</h1>


<h3>Dashboard Estratégico Integral 2026</h3>


<p>Producción sostenible de trucha arcoíris en el Lago Titicaca</p>


</div>

""",unsafe_allow_html=True)




# =====================================================
# RESUMEN EJECUTIVO
# =====================================================


if menu=="Resumen Ejecutivo":



    st.header("📊 Indicadores Estratégicos")



    c1,c2,c3=st.columns(3)



    with c1:
        st.metric(

        "Ventas",

        "S/9,067,500"

        )



    with c2:

        st.metric(

        "Producción",

        "604,500 kg"

        )



    with c3:

        st.metric(

        "Utilidad",

        "S/2,357,500"

        )



    c4,c5,c6=st.columns(3)



    with c4:

        st.metric(

        "Clientes",

        "46"

        )



    with c5:

        st.metric(

        "Trabajadores",

        "76"

        )



    with c6:

        st.metric(

        "FCR",

        "1.40"

        )



    st.write("")


    st.subheader("📌 Estado General")



    a,b,c=st.columns(3)



    with a:

        st.success(

        "Producción en crecimiento"

        )




    with b:


        st.success(

        "Mortalidad controlada"

        )




    with c:


        st.success(

        "Rentabilidad positiva"

        )



    st.info("""

    Highland Fish cumple sus objetivos estratégicos.


    ✔ Producción superior a 600 mil kg


    ✔ Mortalidad menor al 2.5%


    ✔ Crecimiento comercial


    ✔ Rentabilidad positiva


    """)





# =====================================================
# PRODUCCION
# =====================================================



elif menu=="Producción":



    st.header("🐟 Producción")



    df=pd.DataFrame({


"Mes":[

"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"

],




"Producción":[


42000,
43500,
45000,
46500,
48000,
49500,
51000,
52500,
54000,
55500,
57000,
60000

],




"Alimento":[


58800,
60900,
63000,
65100,
67200,
69300,
71400,
73500,
75600,
77700,
79800,
84000

],




"Mortalidad":[


2.5,
2.4,
2.3,
2.2,
2.1,
2.0,
1.9,
1.8,
1.8,
1.7,
1.6,
1.5

]

})



    col1,col2=st.columns(2)



    with col1:



        fig=px.bar(

            df,

            x="Mes",

            y="Producción",

            color="Producción",

            title="Producción Mensual"

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )




    with col2:



        fig2=px.line(

            df,

            x="Mes",

            y="Mortalidad",

            markers=True,

            title="Mortalidad"

        )



        st.plotly_chart(

            fig2,

            use_container_width=True

        )




    fig3=px.area(

        df,

        x="Mes",

        y="Alimento",

        title="Consumo de Alimento"

    )



    st.plotly_chart(

        fig3,

        use_container_width=True

    )




    st.dataframe(

        df,

        use_container_width=True

    )
# =====================================================
# FINANZAS
# =====================================================

elif menu=="Finanzas":

    st.header("💰 Finanzas")



    finanzas = pd.DataFrame({

        "Mes":[
            "Enero","Febrero","Marzo","Abril",
            "Mayo","Junio","Julio","Agosto",
            "Septiembre","Octubre","Noviembre","Diciembre"
        ],

        "Ventas":[
            630000,
            652500,
            675000,
            697500,
            720000,
            742500,
            765000,
            787500,
            810000,
            832500,
            855000,
            900000
        ],


        "Costos":[
            520000,
            528000,
            535000,
            542000,
            548000,
            555000,
            562000,
            568000,
            575000,
            582000,
            590000,
            605000
        ],


        "Utilidad":[

            110000,
            124500,
            140000,
            155500,
            172000,
            187500,
            203000,
            219500,
            235000,
            250500,
            265000,
            295000
        ]

    })



    c1,c2,c3 = st.columns(3)



    with c1:
        st.metric(
            "Ventas",
            "S/ 9,067,500"
        )



    with c2:
        st.metric(
            "Utilidad",
            "S/2,357,500"
        )



    with c3:
        st.metric(
            "Margen",
            "26%"
        )



    fig = px.line(

        finanzas,

        x="Mes",

        y=["Ventas","Costos"],

        markers=True,

        title="Ventas vs Costos"

    )



    st.plotly_chart(
        fig,
        use_container_width=True
    )



    fig2 = px.bar(

        finanzas,

        x="Mes",

        y="Utilidad",

        color="Utilidad",

        title="Utilidad Mensual"

    )



    st.plotly_chart(
        fig2,
        use_container_width=True
    )




    costos = pd.DataFrame({

        "Concepto":[

            "Alimento",

            "Sueldos",

            "Energía",

            "Transporte",

            "Mantenimiento",

            "Otros"

        ],



        "Monto":[

            3840000,

            1680000,

            420000,

            300000,

            240000,

            180000

        ]

    })



    fig3 = px.pie(

        costos,

        names="Concepto",

        values="Monto",

        hole=.5,

        title="Estructura de Costos"

    )



    st.plotly_chart(
        fig3,
        use_container_width=True
    )





# =====================================================
# CLIENTES
# =====================================================



elif menu=="Clientes":



    st.header("🛒 Clientes")



    clientes_df = pd.DataFrame({


        "Cliente":[

            "Supermercados",

            "Restaurantes",

            "Mayoristas",

            "Hoteles",

            "Exportación"

        ],



        "Participación":[

            35,

            25,

            20,

            10,

            10

        ]

    })




    fig = px.pie(

        clientes_df,

        names="Cliente",

        values="Participación",

        hole=.5,

        title="Participación por Cliente"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.dataframe(

        clientes_df,

        use_container_width=True

    )





# =====================================================
# PRODUCTOS
# =====================================================



elif menu=="Productos":



    st.header("🐠 Productos")




    productos = pd.DataFrame({



        "Producto":[


            "Trucha fresca",

            "Congelada",

            "Ahumada",

            "Filete Premium"


        ],



        "Participación":[


            55,

            25,

            15,

            5

        ]

    })



    fig = px.pie(


        productos,


        names="Producto",


        values="Participación",


        hole=.5,


        title="Mix de Productos"


    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.dataframe(

        productos,

        use_container_width=True

    )





# =====================================================
# PERSONAL
# =====================================================



elif menu=="Personal":



    st.header("👥 Personal")



    personal = pd.DataFrame({



        "Área":[

            "Producción",

            "Alimentación",

            "Procesamiento",

            "Calidad",

            "Logística",

            "Ventas",

            "Administración",

            "Gerencia"

        ],



        "Trabajadores":[

            45,

            12,

            8,

            4,

            3,

            2,

            1,

            1

        ]

    })




    fig = px.bar(

        personal,

        x="Área",

        y="Trabajadores",

        color="Trabajadores",

        title="Distribución del Personal"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.metric(

        "Total Trabajadores",

        "76"

    )



    st.dataframe(

        personal,

        use_container_width=True

    )
# =====================================================
# KPIs ESTRATÉGICOS
# =====================================================

elif menu=="KPIs Estratégicos":


    st.header("🎯 KPIs Estratégicos")


    kpis=pd.DataFrame({

        "Indicador":[

            "Producción",

            "Ventas",

            "Utilidad",

            "Clientes",

            "Mortalidad",

            "FCR"

        ],



        "Meta":[

            "600,000 kg",

            "S/9,000,000",

            "S/2,300,000",

            "45",

            "≤2.5%",

            "1.40"

        ],



        "Resultado":[

            "604,500 kg",

            "S/9,067,500",

            "S/2,357,500",

            "46",

            "1.98%",

            "1.40"

        ],



        "Estado":[

            "🟢",

            "🟢",

            "🟢",

            "🟢",

            "🟢",

            "🟢"

        ]

    })


    st.dataframe(

        kpis,

        use_container_width=True,

        hide_index=True

    )



    c1,c2,c3=st.columns(3)



    with c1:
        st.metric(
            "Producción",
            "604,500 kg"
        )


    with c2:
        st.metric(
            "Ventas",
            "S/9.07 M"
        )


    with c3:
        st.metric(
            "Utilidad",
            "S/2.36 M"
        )



    st.success("""

    ✅ Todas las metas estratégicas fueron cumplidas.

    ✅ Mortalidad por debajo del máximo permitido.

    ✅ Empresa rentable y sostenible.

    """)





# =====================================================
# PLANEAMIENTO ESTRATÉGICO
# =====================================================


elif menu=="Planeamiento Estratégico":


    st.header("🏢 Planeamiento Estratégico")


    tab1,tab2,tab3,tab4 = st.tabs(

        [

        "Misión",

        "Visión",

        "FODA",

        "Objetivos"

        ]

    )


    with tab1:

        st.info("""

Highland Fish es una empresa especializada en la producción,
crianza y aprovechamiento integral de recursos hidrobiológicos,
orientada a proveer productos de alta calidad bajo principios
de sostenibilidad ambiental.

        """)


    with tab2:


        st.info("""

Al 2030 ser la empresa acuícola líder del altiplano peruano,
reconocida por exportar truchas con valor agregado y
certificación internacional.

        """)



    with tab3:


        st.markdown("""

### Fortalezas

- Ubicación privilegiada
- Experiencia en producción
- Costos flexibles


### Debilidades

- Registro manual
- Sin certificación sostenible



### Oportunidades

- Mercado boliviano
- Certificación internacional



### Amenazas

- Cambio climático
- Enfermedades
- Competidores

        """)



    with tab4:


        objetivos=pd.DataFrame({

            "Objetivo":[

                "Reducir mortalidad",

                "Controlar costos",

                "Optimizar FCR",

                "Incrementar clientes"

            ],



            "Meta":[

                "≤28%",

                "≤S/6.80",

                "1.22",

                "2 clientes"

            ]

        })


        st.dataframe(

            objetivos,

            use_container_width=True

        )






# =====================================================
# PROYECCIÓN
# =====================================================


elif menu=="Proyección":



    st.header("📈 Proyección 2027")


    proyeccion=pd.DataFrame({


        "Año":[

            2025,

            2026,

            2027

        ],



        "Producción":[

            604500,

            650000,

            700000

        ]

    })



    fig=px.line(

        proyeccion,

        x="Año",

        y="Producción",

        markers=True,

        title="Proyección de Producción"

    )



    fig.update_layout(

        height=500

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.info("""

Se proyecta un crecimiento debido a:


• Reducción de mortalidad


• Mayor cartera de clientes


• Certificaciones sostenibles


• Tecnología acuícola


• Mejor alimentación


    """)




# =====================================================
# FOOTER
# =====================================================


st.markdown("---")


st.caption(

"🐟 Highland Fish S.A.C. | Dashboard Estratégico Integral 2026 | Universidad Nacional Agraria La Molina"

)
