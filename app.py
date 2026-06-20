import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


# =====================================
# CONFIGURACION
# =====================================

st.set_page_config(
    page_title="Highland Fish",
    page_icon="🐟",
    layout="wide"
)


# =====================================
# CSS POWER BI
# =====================================

st.markdown("""

<style>

.stApp{
background:#F3F5F7;
}


section[data-testid="stSidebar"]{
background:#06244D;
}


section[data-testid="stSidebar"] *{
color:white;
}


.hero{

padding:35px;

border-radius:20px;

background:linear-gradient(90deg,#06244D,#0B4F8C);

color:white;

margin-bottom:25px;

}


.card{

background:white;

padding:25px;

border-radius:15px;

box-shadow:0px 3px 10px rgba(0,0,0,0.10);

text-align:center;

}



.big{

font-size:28px;

font-weight:bold;

color:#06244D;

}



.small{

font-size:14px;

color:gray;

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



# =====================================
# SIDEBAR
# =====================================


with st.sidebar:


    menu = option_menu(

        "Highland Fish",

        [

        "Dashboard",

        "Producción",

        "Finanzas",

        "Clientes",

        "Productos",

        "RRHH",

        "KPIs",

        "Planeamiento",

        "Proyección"

        ],




        icons=[

        "speedometer2",

        "water",

        "cash",

        "people",

        "basket",

        "person-badge",

        "bullseye",

        "building",

        "graph-up"

        ],

        default_index=0

    )



st.sidebar.success("Empresa sostenible")



# =====================================
# HERO
# =====================================


st.markdown("""

<div class='hero'>


<h1>🐟 Highland Fish SAC</h1>

<h3>Dashboard Ejecutivo 2026</h3>

Piscicultura de Trucha Arcoíris


Lago Titicaca • Perú


</div>

""",unsafe_allow_html=True)




# =====================================
# DATOS
# =====================================


ventas=9067500

utilidad=2357500

produccion=604500

clientes=46

trabajadores=76

mortalidad=1.98

fcr=1.40




# =====================================
# DASHBOARD
# =====================================



if menu=="Dashboard":



    st.header("📊 Resumen Ejecutivo")



    c1,c2,c3,c4=st.columns(4)




    with c1:


        st.markdown(f"""

<div class='card'>

<div class='small'>VENTAS</div>

<div class='big'>

S/ {ventas:,.0f}

</div>

</div>

""",unsafe_allow_html=True)




    with c2:


        st.markdown(f"""

<div class='card'>

<div class='small'>UTILIDAD</div>

<div class='big'>

S/ {utilidad:,.0f}

</div>

</div>

""",unsafe_allow_html=True)





    with c3:



        st.markdown(f"""

<div class='card'>

<div class='small'>PRODUCCIÓN</div>

<div class='big'>

{produccion:,.0f}

</div>

</div>

""",unsafe_allow_html=True)






    with c4:


        st.markdown(f"""

<div class='card'>

<div class='small'>CLIENTES</div>

<div class='big'>

{clientes}

</div>

</div>

""",unsafe_allow_html=True)




    st.write("")


    st.subheader("Indicadores Operativos")



    g1,g2=st.columns(2)




    with g1:


        fig=go.Figure(go.Indicator(

        mode="gauge+number",

        value=mortalidad,

        title={'text':'Mortalidad %'},


        gauge={

        'axis':{'range':[0,5]},

        'bar':{'color':'#0B4F8C'},


        'steps':[

        {'range':[0,2.5],'color':'lightgreen'},

        {'range':[2.5,5],'color':'lightcoral'}

        ]

        }

        ))



        fig.update_layout(

        height=350

        )


        st.plotly_chart(

        fig,

        use_container_width=True

        )





    with g2:



        fig2=go.Figure(go.Indicator(

        mode="gauge+number",

        value=fcr,


        title={'text':'FCR'},



        gauge={

        'axis':{'range':[0,2]},


        'bar':{'color':'#0B4F8C'},



        'steps':[


        {'range':[0,1.4],'color':'lightgreen'},


        {'range':[1.4,2],'color':'khaki'}

        ]

        }

        ))



        fig2.update_layout(

        height=350

        )



        st.plotly_chart(

        fig2,

        use_container_width=True

        )
        # ==========================================================
# PRODUCCIÓN
# ==========================================================

elif menu=="Producción":

    st.header("🐟 Producción Anual")

    produccion = pd.DataFrame({

        'Mes':[
        'Enero','Febrero','Marzo','Abril',
        'Mayo','Junio','Julio','Agosto',
        'Septiembre','Octubre','Noviembre','Diciembre'
        ],

        'Produccion':[

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

        'Mortalidad':[

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

        ],

        'Alimento':[

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

        ]

    })


    col1,col2=st.columns(2)


    with col1:


        fig=px.area(

            produccion,

            x='Mes',

            y='Produccion',

            title='Producción Mensual (kg)',

            color_discrete_sequence=['#0B4F8C']

        )


        fig.update_layout(

            template='plotly_white',

            height=450

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )


    with col2:


        fig2=px.line(

            produccion,

            x='Mes',

            y='Mortalidad',

            markers=True,

            title='Mortalidad (%)'

        )


        fig2.update_layout(

            template='plotly_white',

            height=450

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )



    st.write("")


    fig3=px.bar(

        produccion,

        x='Mes',

        y='Alimento',

        title='Consumo de Alimento (kg)',

        color='Alimento',

        color_continuous_scale='Blues'

    )


    fig3.update_layout(

        template='plotly_white',

        height=500

    )


    st.plotly_chart(

        fig3,

        use_container_width=True

    )



    st.subheader("📋 Tabla Operativa")


    st.dataframe(

        produccion,

        use_container_width=True

    )
    # ==========================================================
# FINANZAS
# ==========================================================

elif menu=="Finanzas":

    st.header("💰 Finanzas")

    costos = pd.DataFrame({

        'Concepto':[

            'Alimento balanceado',
            'Sueldos',
            'Energía',
            'Transporte',
            'Mantenimiento',
            'Otros'

        ],

        'Monto':[

            3840000,
            1680000,
            420000,
            300000,
            240000,
            180000

        ]

    })



    mensual = pd.DataFrame({

        'Mes':[

            'Enero','Febrero','Marzo','Abril',
            'Mayo','Junio','Julio','Agosto',
            'Septiembre','Octubre','Noviembre','Diciembre'

        ],

        'Ventas':[

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

        'Utilidad':[

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



    k1,k2,k3 = st.columns(3)



    with k1:

        st.metric(

            "Ventas Anuales",

            "S/ 9,067,500"

        )



    with k2:

        st.metric(

            "Utilidad",

            "S/ 2,357,500"

        )



    with k3:

        st.metric(

            "Margen",

            "26 %"

        )



    col1,col2 = st.columns(2)



    with col1:



        fig = px.pie(

            costos,

            names='Concepto',

            values='Monto',

            hole=0.55,

            title='Distribución de Costos'

        )



        fig.update_layout(

            height=500

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )




    with col2:



        fig2 = px.line(

            mensual,

            x='Mes',

            y='Utilidad',

            markers=True,

            title='Utilidad Mensual'

        )



        fig2.update_layout(

            height=500,

            template='plotly_white'

        )



        st.plotly_chart(

            fig2,

            use_container_width=True

        )




    st.subheader("Detalle de Costos")



    st.dataframe(

        costos,

        use_container_width=True

    )



    st.success("""

✅ Principal gasto: alimento balanceado

✅ Utilidad creciente durante todo el año

✅ Rentabilidad positiva

✅ Empresa financieramente estable

""")
    # ==========================================================
# CLIENTES
# ==========================================================

elif menu=="Clientes":

    st.header("👥 Clientes")

    clientes = pd.DataFrame({

        'Tipo':[

            'Supermercados',
            'Restaurantes',
            'Mayoristas',
            'Hoteles',
            'Exportación'

        ],

        'Participacion':[

            35,
            25,
            20,
            10,
            10

        ]

    })


    col1,col2 = st.columns(2)


    with col1:

        fig = px.pie(

            clientes,

            names='Tipo',
            values='Participacion',

            hole=.55,

            title='Participación de Clientes'

        )

        fig.update_layout(height=450)

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    with col2:


        fig2=px.bar(

            clientes,

            x='Tipo',

            y='Participacion',

            color='Participacion',

            color_continuous_scale='Blues'

        )


        fig2.update_layout(

            height=450,

            template='plotly_white'

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )


    st.dataframe(

        clientes,

        use_container_width=True

    )



# ==========================================================
# PRODUCTOS
# ==========================================================


elif menu=="Productos":


    st.header("🐟 Productos")


    productos = pd.DataFrame({

        'Producto':[

            'Trucha fresca',

            'Trucha congelada',

            'Trucha ahumada',

            'Filete premium'

        ],

        'Participacion':[

            55,

            25,

            15,

            5

        ]

    })


    col1,col2 = st.columns(2)



    with col1:


        fig=px.pie(

            productos,

            names='Producto',

            values='Participacion',

            hole=.5,

            title='Mix de Productos'

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )




    with col2:


        fig2=px.bar(

            productos,

            x='Producto',

            y='Participacion',

            color='Participacion',

            color_continuous_scale='Blues'

        )


        fig2.update_layout(

            template='plotly_white',

            height=450

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )



    st.dataframe(

        productos,

        use_container_width=True

    )



# ==========================================================
# RRHH
# ==========================================================


elif menu=="RRHH":


    st.header("👨‍💼 Recursos Humanos")


    rrhh = pd.DataFrame({

        'Area':[

            'Producción',

            'Alimentación',

            'Procesamiento',

            'Calidad',

            'Logística',

            'Ventas',

            'Administración',

            'Gerencia'

        ],

        'Trabajadores':[

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



    col1,col2=st.columns(2)



    with col1:


        fig=px.bar(

            rrhh,

            x='Area',

            y='Trabajadores',

            color='Trabajadores',

            color_continuous_scale='Blues'

        )


        fig.update_layout(

            height=500,

            template='plotly_white'

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )




    with col2:


        fig2=px.pie(

            rrhh,

            names='Area',

            values='Trabajadores',

            hole=.55,

            title='Distribución del Personal'

        )


        fig2.update_layout(

            height=500

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )



    st.metric(

        "Total de Trabajadores",

        76

    )



    st.dataframe(

        rrhh,

        use_container_width=True

    )
    # ==========================================================
# KPIs ESTRATÉGICOS
# ==========================================================

elif menu=="KPIs":

    st.header("🎯 KPIs Estratégicos")

    indicadores = pd.DataFrame({

        "Indicador":[

        "Producción anual",
        "Ventas anuales",
        "Utilidad anual",
        "Clientes activos",
        "Mortalidad",
        "FCR"

        ],

        "Meta":[

        600000,
        9000000,
        2300000,
        45,
        2.5,
        1.4

        ],

        "Resultado":[

        604500,
        9067500,
        2357500,
        46,
        1.98,
        1.40

        ]

    })


    st.dataframe(
        indicadores,
        use_container_width=True
    )


    fig = px.bar(

        indicadores,

        x="Indicador",

        y=["Meta","Resultado"],

        barmode="group",

        title="Cumplimiento de KPIs"

    )

    fig.update_layout(
        height=500,
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.success("""

✅ Meta de producción alcanzada

✅ Clientes por encima del objetivo

✅ Mortalidad bajo control

✅ Empresa rentable

""")


# ==========================================================
# PLANEAMIENTO
# ==========================================================

elif menu=="Planeamiento":

    st.header("🏢 Planeamiento Estratégico")


    col1,col2=st.columns(2)


    with col1:


        st.subheader("PESTEL")


        st.info("""

Político
• PRODUCE
• SANIPES


Económico
• Tipo de cambio


Social
• Mayor consumo saludable


Tecnológico
• Sensores


Ecológico
• Cambio climático


Legal
• Normas sanitarias

""")


    with col2:


        st.subheader("FODA")


        st.success("""

Fortalezas

✔ Lago Titicaca

✔ Experiencia


✔ Costos flexibles

""")


        st.warning("""

Debilidades


Excel manual


Sin certificación


Dependencia compradores

""")


        st.info("""

Oportunidades


Bolivia


Certificación


Apps

""")


        st.error("""

Amenazas


Sequías


Competidores


Enfermedades

""")


# ==========================================================
# PROYECCIÓN
# ==========================================================


elif menu=="Proyección":


    st.header("📈 Proyección 2030")


    proyeccion = pd.DataFrame({


        'Año':[


        2025,
        2026,
        2027,
        2028,
        2029,
        2030


        ],



        'Producción':[


        604500,
        650000,
        700000,
        760000,
        820000,
        900000


        ]

    })



    fig = px.line(

        proyeccion,

        x='Año',

        y='Producción',

        markers=True,

        title='Proyección de Producción'

    )



    fig.update_layout(

        height=550,

        template='plotly_white'

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.info("""

La empresa proyecta:


• Mayor capacidad instalada


• Certificación internacional


• Exportaciones


• Nuevos mercados


• Liderazgo en el altiplano peruano


""")


# ==========================================================
# FOOTER
# ==========================================================


st.markdown("---")


st.caption(

"Highland Fish SAC | Dashboard Ejecutivo 2026 | Universidad Nacional Agraria La Molina"

)
