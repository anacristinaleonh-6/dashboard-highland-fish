import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



st.set_page_config(
        page_title="Highland Fish",
        page_icon="🐟",
        layout="wide"
)



####################################################
# CSS PREMIUM
####################################################

st.markdown("""
<style>

.stApp{
background-color:#f4f7fa;
}


section[data-testid="stSidebar"]{

background:linear-gradient(180deg,#06244D,#0B4F8C);

}


section[data-testid="stSidebar"] *{

color:white;

}



.hero{

background:linear-gradient(90deg,#06244D,#0B4F8C);

padding:35px;

border-radius:25px;

box-shadow:0px 5px 25px rgba(0,0,0,0.20);

color:white;

margin-bottom:20px;

}



.card{


background:white;


padding:20px;


border-radius:18px;


box-shadow:0px 3px 15px rgba(0,0,0,0.10);


border-left:6px solid #0B4F8C;


}


.small{

font-size:14px;

color:gray;

}


.big{


font-size:35px;


font-weight:bold;


color:#06244D;


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



####################################################
# SIDEBAR
####################################################

st.sidebar.title("🐟 Highland Fish")

st.sidebar.write("---")

menu=st.sidebar.radio(

"Menú",

[

"Dashboard",

"Producción",

"Finanzas",

"Clientes",

"Productos",

"Personal",

"KPIs",

"Planeamiento",

"Proyección"

]

)



st.sidebar.success("Empresa Sostenible")



####################################################
# HERO
####################################################


st.markdown("""

<div class='hero'>

<h1>🐟 Highland Fish S.A.C.</h1>

<h3>Dashboard Estratégico Integral 2026</h3>

Producción sostenible de trucha arcoíris en el Lago Titicaca


</div>

""",unsafe_allow_html=True)




####################################################
# DATOS EJECUTIVOS
####################################################



ventas=9067500

utilidad=2357500

produccion=604500

clientes=46

trabajadores=76

mortalidad=1.98

fcr=1.40





####################################################
# DASHBOARD
####################################################


if menu=="Dashboard":


    st.header("📊 Resumen Ejecutivo")


    c1,c2,c3=st.columns(3)



    with c1:

        st.markdown(f"""

<div class='card'>


<div class='small'>

VENTAS


</div>



<div class='big'>

S/. {ventas:,.0f}


</div>


▲ 8.4%

</div>

""",unsafe_allow_html=True)



    with c2:


        st.markdown(f"""

<div class='card'>


<div class='small'>

UTILIDAD


</div>



<div class='big'>

S/. {utilidad:,.0f}


</div>


▲ 12.2%

</div>

""",unsafe_allow_html=True)




    with c3:


        st.markdown(f"""

<div class='card'>


<div class='small'>

PRODUCCIÓN


</div>



<div class='big'>

{produccion:,.0f}


</div>


kg


</div>

""",unsafe_allow_html=True)




####################################################
# SEGUNDA FILA
####################################################


    c4,c5,c6=st.columns(3)



    with c4:


        st.markdown(f"""

<div class='card'>


<div class='small'>

CLIENTES


</div>



<div class='big'>

{clientes}


</div>



</div>

""",unsafe_allow_html=True)




    with c5:



        st.markdown(f"""

<div class='card'>


<div class='small'>

PERSONAL


</div>



<div class='big'>

{trabajadores}


</div>



</div>

""",unsafe_allow_html=True)




    with c6:


        st.markdown(f"""

<div class='card'>


<div class='small'>

MORTALIDAD


</div>



<div class='big'>

{mortalidad}%


</div>


🟢 Excelente


</div>

""",unsafe_allow_html=True)





####################################################
# GAUGE KPI
####################################################


    st.write("")



    col1,col2=st.columns(2)



    with col1:



        fig=go.Figure(go.Indicator(

        mode="gauge+number",

        value=mortalidad,



        title={'text':"Mortalidad"},



        gauge={


        'axis':{'range':[0,5]},



        'bar':{'color':"#0B4F8C"},



        'steps':[


        {'range':[0,2.5],'color':'lightgreen'},



        {'range':[2.5,5],'color':'lightcoral'}

        ]

        }


        ))



        fig.update_layout(height=350)



        st.plotly_chart(

        fig,

        use_container_width=True

        )





    with col2:



        fig2=go.Figure(go.Indicator(


        mode="gauge+number",



        value=fcr,



        title={'text':"FCR"},



        gauge={



        'axis':{'range':[1,2]},



        'bar':{'color':"#0B4F8C"},



        'steps':[



        {'range':[1,1.4],'color':'lightgreen'},



        {'range':[1.4,2],'color':'orange'}

        ]

        }

        ))



        fig2.update_layout(height=350)



        st.plotly_chart(

        fig2,

        use_container_width=True

        )




####################################################
# ESTADO GENERAL
####################################################


    st.subheader("Estado General")



    a,b,c=st.columns(3)



    a.success("Producción en crecimiento")


    b.success("Rentabilidad positiva")


    c.success("Mortalidad controlada")

####################################################
# PRODUCCION
####################################################


elif menu=="Producción":


    st.header("🐟 Producción")



    df=pd.DataFrame({


    "Mes":[

    "Ene",
    "Feb",
    "Mar",
    "Abr",
    "May",
    "Jun",
    "Jul",
    "Ago",
    "Sep",
    "Oct",
    "Nov",
    "Dic"

    ],



    "Produccion":[


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



###################################################
# KPIs
###################################################


c1,c2,c3,c4=st.columns(4)



with c1:

    st.metric(

    "Producción anual",

    "604,500 kg"

)





with c2:


    st.metric(

    "Meta",

    "600,000 kg"

)



with c3:


    st.metric(

    "Mortalidad",

    "1.98 %"

)




with c4:


    st.metric(

    "FCR",

    "1.40"

)





###################################################
# GRAFICOS
###################################################


col1,col2=st.columns(2)



#######################################
# PRODUCCION
#######################################


with col1:



    fig=px.bar(


    df,


    x="Mes",


    y="Produccion",



    color="Produccion",



    color_continuous_scale="Blues",



    title="Producción Mensual"

)



    fig.update_layout(


    template="plotly_white",


    height=450


)



    st.plotly_chart(


    fig,


    use_container_width=True

)





##########################################
# MORTALIDAD
##########################################



with col2:



    fig2=px.line(


    df,


    x="Mes",


    y="Mortalidad",



    markers=True,



    title="Mortalidad"



)



    fig2.update_traces(


    line_color="#0B4F8C",

    marker_size=10

)



    fig2.update_layout(


    template="plotly_white",


    height=450


)



    st.plotly_chart(


    fig2,


    use_container_width=True

)






####################################################
# ALIMENTO
####################################################


fig3=px.area(


df,


x="Mes",


y="Alimento",



title="Consumo de alimento"



)



fig3.update_layout(


template="plotly_white",


height=450

)



fig3.update_traces(


fillcolor="#4EA5D9",


line_color="#0B4F8C"

)



st.plotly_chart(


fig3,


use_container_width=True

)





####################################################
# META
####################################################


st.subheader("🎯 Cumplimiento de Metas")



meta=pd.DataFrame({


"Indicador":[

"Producción"

],



"Meta":[


600000

],



"Real":[


604500

]

})




fig4=px.bar(


meta,



x="Indicador",



y=["Meta","Real"],



barmode="group",



title="Meta vs Resultado"



)



fig4.update_layout(


template="plotly_white",



height=400

)



st.plotly_chart(


fig4,


use_container_width=True

)






####################################################
# TABLA
####################################################


st.subheader("Detalle Producción")



st.dataframe(


df,



use_container_width=True,



hide_index=True

)


####################################################
# FINANZAS
####################################################

elif menu=="Finanzas":

    st.header("💰 Finanzas")


    costos = pd.DataFrame({

        "Concepto":[

            "Alimento balanceado",
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


    ventas_anuales=9067500
    utilidad=2357500
    costos_totales=6660000
    margen=26


####################################################
# KPIs
####################################################


    k1,k2,k3,k4=st.columns(4)



    with k1:

        st.metric(

            "Ventas",

            "S/ 9.07 M"

        )



    with k2:

        st.metric(

            "Costos",

            "S/ 6.66 M"

        )



    with k3:

        st.metric(

            "Utilidad",

            "S/ 2.36 M"

        )



    with k4:

        st.metric(

            "Margen",

            "26 %"

        )


####################################################
# GRAFICOS
####################################################


    col1,col2=st.columns(2)



#########################################
# DONUT
#########################################


    with col1:



        fig=px.pie(


            costos,


            names="Concepto",


            values="Monto",


            hole=.65


        )



        fig.update_layout(


            title="Distribución de Costos",


            template="plotly_white",


            height=500

        )



        st.plotly_chart(


            fig,


            use_container_width=True

        )




#########################################
# BARRAS
#########################################



    with col2:



        fig2=px.bar(



            costos,



            x="Concepto",



            y="Monto",



            color="Concepto"



        )



        fig2.update_layout(



            title="Costos por Categoría",



            template="plotly_white",



            height=500

        )



        st.plotly_chart(


            fig2,


            use_container_width=True

        )



####################################################
# COMPARACION
####################################################



    comparacion=pd.DataFrame({


        "Concepto":[


            "Ventas",
            "Costos",
            "Utilidad"

        ],



        "Monto":[


            ventas_anuales,
            costos_totales,
            utilidad

        ]

    })





    fig3=px.bar(


        comparacion,


        x="Concepto",


        y="Monto",



        color="Concepto"



    )



    fig3.update_layout(


        title="Ventas vs Costos vs Utilidad",



        template="plotly_white",



        height=450

    )



    st.plotly_chart(


        fig3,


        use_container_width=True

    )





####################################################
# RENTABILIDAD
####################################################



    st.subheader("📈 Rentabilidad")




    fig4=go.Figure(go.Indicator(



        mode="gauge+number",



        value=26,



        title={'text':"Margen (%)"},




        gauge={


            'axis':{'range':[0,40]},



            'bar':{'color':"#0B4F8C"},



            'steps':[



                {'range':[0,15],'color':'lightcoral'},



                {'range':[15,25],'color':'khaki'},



                {'range':[25,40],'color':'lightgreen'}

            ]

        }

    ))



    fig4.update_layout(


        height=400

    )



    st.plotly_chart(


        fig4,


        use_container_width=True

    )




####################################################
# SEMAFORO
####################################################



    st.subheader("Estado Financiero")



    c1,c2,c3=st.columns(3)



    with c1:

        st.success(

            "🟢 Ventas en crecimiento"

        )



    with c2:


        st.success(

            "🟢 Utilidad positiva"

        )



    with c3:


        st.success(

            "🟢 Margen saludable"

        )




####################################################
# TABLA
####################################################


    st.subheader("Detalle de Costos")


    st.dataframe(


        costos,


        use_container_width=True,


        hide_index=True

    )
####################################################
# CLIENTES
####################################################

elif menu=="Clientes":

    st.header("👥 Clientes")

    clientes = pd.DataFrame({

        "Cliente":[
            "Supermercados",
            "Restaurantes",
            "Mayoristas",
            "Hoteles",
            "Exportación"
        ],

        "Participacion":[
            35,
            25,
            20,
            10,
            10
        ]

    })


    c1,c2,c3=st.columns(3)

    with c1:
        st.metric(
            "Clientes activos",
            "46"
        )

    with c2:
        st.metric(
            "Meta",
            "45"
        )

    with c3:
        st.metric(
            "Cumplimiento",
            "102%"
        )



    col1,col2=st.columns(2)


####################################################
# DONUT
####################################################


    with col1:


        fig=px.pie(

            clientes,

            names="Cliente",

            values="Participacion",

            hole=0.65

        )


        fig.update_layout(

            title="Distribución de Clientes",

            template="plotly_white",

            height=500

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



####################################################
# BARRAS
####################################################


    with col2:


        fig2=px.bar(

            clientes,

            x="Participacion",

            y="Cliente",

            orientation="h",

            color="Participacion"

        )


        fig2.update_layout(

            template="plotly_white",

            title="Participación"

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )




####################################################
# PRODUCTOS
####################################################


elif menu=="Productos":

    st.header("🐟 Productos")


    productos=pd.DataFrame({

        "Producto":[

            "Trucha fresca",

            "Congelada",

            "Ahumada",

            "Filete premium"

        ],

        "Participacion":[

            55,
            25,
            15,
            5

        ]

    })



    c1,c2,c3=st.columns(3)


    with c1:
        st.metric(
            "Productos",
            "4"
        )


    with c2:
        st.metric(
            "Principal",
            "Trucha fresca"
        )


    with c3:
        st.metric(
            "Participación",
            "55%"
        )



    fig=px.pie(

        productos,

        names="Producto",

        values="Participacion",

        hole=0.60

    )


    fig.update_layout(

        title="Mix Comercial",

        template="plotly_white",

        height=500

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



####################################################
# PERSONAL
####################################################


elif menu=="Personal":

    st.header("👨🏻‍💼 Personal")



    personal=pd.DataFrame({

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



    c1,c2,c3=st.columns(3)



    with c1:

        st.metric(

            "Trabajadores",

            "76"

        )


    with c2:

        st.metric(

            "Área principal",

            "Producción"

        )


    with c3:

        st.metric(

            "Operativos",

            "57"

        )



####################################################
# BARRAS RRHH
####################################################



    fig=px.bar(

        personal,

        x="Área",

        y="Trabajadores",

        color="Trabajadores"

    )



    fig.update_layout(

        template="plotly_white",

        title="Distribución del Personal",

        height=500

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



####################################################
# SEMAFOROS
####################################################


    st.subheader("Estado RRHH")



    c1,c2,c3=st.columns(3)


    c1.success(

        "🟢 Dotación adecuada"

    )



    c2.success(

        "🟢 Producción cubierta"

    )



    c3.success(

        "🟢 Operaciones estables"

    )




####################################################
# ORGANIGRAMA SIMPLE
####################################################


    st.subheader("Organigrama")



    st.info("""

Gerencia General

⬇

Administración

⬇

Producción

⬇

Operarios


Contador Externo


Logística


Ventas


Calidad


    """)



####################################################
# TABLA
####################################################


    st.dataframe(

        personal,

        use_container_width=True,

        hide_index=True

    )
####################################################
# KPIs ESTRATÉGICOS
####################################################

elif menu=="KPIs":

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
        kpis,
        use_container_width=True
    )



    st.success("🟢 Producción superada")
    st.success("🟢 Rentabilidad positiva")
    st.success("🟢 Clientes por encima de meta")
    st.success("🟢 Mortalidad controlada")



####################################################
# PLANEAMIENTO
####################################################


elif menu=="Planeamiento":



    st.header("🏢 Planeamiento Estratégico")



    pestañas=st.tabs([

        "Misión",
        "Visión",
        "Valores",
        "Stakeholders",
        "PESTEL",
        "FODA",
        "Objetivos"

    ])




########################
# MISION
########################


    with pestañas[0]:

        st.info("""

Highland Fish es una empresa especializada
en la producción y aprovechamiento integral
de recursos hidrobiológicos, orientada a
proveer productos de alta calidad bajo
principios de sostenibilidad ambiental.

        """)



########################
# VISION
########################



    with pestañas[1]:


        st.info("""

Al 2030 ser la empresa acuícola líder
del altiplano peruano, reconocida por
exportar truchas con valor agregado
y certificación internacional.

        """)




########################
# VALORES
########################



    with pestañas[2]:


        valores=pd.DataFrame({

            "Valor":[

                "Innovación",
                "Calidad",
                "Responsabilidad Ambiental",
                "Accesibilidad"

            ]

        })


        st.dataframe(
            valores,
            use_container_width=True
        )





########################
# STAKEHOLDERS
########################



    with pestañas[3]:


        st.write("### Internos")

        st.write("- Dueños")
        st.write("- Operarios")
        st.write("- Administración")



        st.write("### Externos")

        st.write("- Clientes")
        st.write("- Comunidad")
        st.write("- Gobierno")
        st.write("- SANIPES")
        st.write("- Proveedores")





########################
# PESTEL
########################



    with pestañas[4]:


        pestel=pd.DataFrame({

            "Factor":[

                "Político",
                "Económico",
                "Social",
                "Tecnológico",
                "Ecológico",
                "Legal"

            ],



            "Impacto":[

                "Positivo",
                "Negativo",
                "Positivo",
                "Positivo",
                "Amenaza",
                "Obligación"

            ]

        })



        st.dataframe(

            pestel,

            use_container_width=True

        )




########################
# FODA
########################



    with pestañas[5]:


        c1,c2=st.columns(2)



        with c1:


            st.success("""

FORTALEZAS

• Lago Titicaca

• Experiencia

• Costos flexibles


            """)



            st.info("""

OPORTUNIDADES

• Bolivia

• Certificación

• Tecnología


            """)



        with c2:



            st.warning("""

DEBILIDADES

• Excel manual

• Pocas certificaciones


            """)



            st.error("""

AMENAZAS

• Cambio climático

• Enfermedades

• Competidores


            """)





########################
# OBJETIVOS
########################



    with pestañas[6]:


        objetivos=pd.DataFrame({

            "Objetivo":[

                "Reducir mortalidad",

                "Controlar costos",

                "Optimizar FCR",

                "Incrementar clientes"

            ],



            "Meta":[

                "≤2.5%",

                "≤S/6.80",

                "1.22",

                "+2 clientes"

            ]

        })



        st.dataframe(

            objetivos,

            use_container_width=True

        )





####################################################
# PROYECCIÓN
####################################################



elif menu=="Proyección":



    st.header("📈 Proyección 2030")



    proyeccion=pd.DataFrame({

        "Año":[

            2025,
            2026,
            2027,
            2028,
            2029,
            2030

        ],



        "Producción":[

            604500,
            650000,
            700000,
            760000,
            820000,
            900000

        ]

    })



    fig=px.line(

        proyeccion,

        x="Año",

        y="Producción",

        markers=True

    )



    fig.update_layout(

        template="plotly_white",

        height=500,

        title="Proyección Productiva al 2030"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.success("""

Meta 2030:

✔ 900,000 kg

✔ Certificación internacional

✔ Liderazgo acuícola

✔ Expansión comercial


    """)



####################################################
# FOOTER
####################################################


st.markdown("---")

st.caption(
"🐟 Highland Fish S.A.C. | Dashboard Estratégico Integral | Universidad Nacional Agraria La Molina | 2026"
)
