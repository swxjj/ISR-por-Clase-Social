import pandas as pd
import matplotlib.pyplot as plt
import requests
import yfinance as yf
import streamlit as st

@st.cache_data
def pond():
  df_pond = pd.read_excel('ponderaciones.xlsx')
  df_pond.set_index("Rubro", inplace=True)
  return df_pond

def load_all():
  api=f"https://apis.datos.gob.ar/series/api/series/?ids=150.1_CSTA_BATAL_0_D_20&format=json&limit=5000&start_date=2023-11-01"
  api_all = f"https://apis.datos.gob.ar/series/api/series/?ids=145.3_INGNACNAL_DICI_M_15,149.1_TL_INDIIOS_OCTU_0_21,150.1_CSTA_BATAL_0_D_20,146.3_IALIMENNAL_DICI_M_45,146.3_IBEBIDANAL_DICI_M_39,146.3_IPRENDANAL_DICI_M_35,146.3_IVIVIENNAL_DICI_M_52,146.3_IEQUIPANAL_DICI_M_46,146.3_ISALUDNAL_DICI_M_18,146.3_ITRANSPNAL_DICI_M_23,146.3_ICOMUNINAL_DICI_M_27,146.3_IRECREANAL_DICI_M_31,146.3_IEDUCACNAL_DICI_M_22,146.3_IRESTAUNAL_DICI_M_33,146.3_IBIENESNAL_DICI_M_36&limit=5000&start_date=2016-12-01&format=json"
  resp_all = requests.get(api_all)
  datos_all = resp_all.json()
  columnas_all = [
    'fecha',
    'Indice_IPC',
    'Indice_Salarial',
    'Costo_Canasta',
    'Alimentos y bebidas no alcohólicas', # [cite: 149]
    'Bebidas alcohólicas y tabaco',       # [cite: 150]
    'Prendas de vestir y calzado',        # [cite: 149]
    'Vivienda, agua, electricidad, gas y otros combustibles',
    'Equipamiento y mantenimiento del hogar',
    'Salud',                              # [cite: 169]
    'Transporte',                         # [cite: 172]
    'Comunicaciones',                     # [cite: 174]
    'Recreación y cultura',
    'Educación',                          # [cite: 170]
    'Restaurantes y hoteles',             # [cite: 173]
    'Bienes y servicios varios'           # [cite: 175]
  ]
  df_all = pd.DataFrame(datos_all['data'], columns=columnas_all)
  df_all.set_index('fecha', inplace=True)
  df_all.index = pd.to_datetime(df_all.index)
  df_all.astype(float)
  return df_all

with st.spinner("Descargando datos oficiales del INDEC..."):
    df_all = load_all()
    df_pond = pond()
st.title("Análisis del Poder Adquisitivo según Clase Social")
# input "asigned" social class
clase_s = st.selectbox("¿Con qué clase social se identifica?", ['Alta', 'Media', 'Baja', 'No sé'], index=None, placeholder="Elija una opción")
# creo variable vacía que guarde la elección
clase_final = ""
# display the selected class
if clase_s is None:
    st.write("Debe elegir una clase social")
elif clase_s != 'No sé':
    clase_final = clase_s
else:
    salario = st.number_input("Ingrese su salario familiar estimado", min_value=100000, value=500000, step=100000)
    personas = st.number_input("Ingrese la cantidad de personas en su hogar", min_value=1, value=1, step=1)
    if salario/personas > df_all['Costo_Canasta'].max()*1.5:
        st.write(f"Su clase es Alta")
        clase_final = "Alta"
    elif salario/personas < df_all['Costo_Canasta'].max():
        st.write(f"Su clase es Baja")
        clase_final = "Baja"
    else:
        st.write(f"Su clase es Media")
        clase_final = "Media"

if clase_final != "":
    
    st.divider()
    st.subheader(f"📈 Análisis de Poder Adquisitivo: Clase {clase_final}")
    fecha_minima = df_all.index.min().date()

    fecha_inicio = st.date_input(
        "Selecciona el mes de inicio del análisis (Base 100):",
        min_value=fecha_minima,
        value=fecha_minima
    )
    fecha_str = fecha_inicio.strftime('%Y-%m-%d')

    df_rubros = df_all.drop(columns=['Indice_IPC', 'Indice_Salarial', 'Costo_Canasta'])
    df_rubros.index = pd.to_datetime(df_rubros.index)
    df_base = df_rubros[df_rubros.index >= fecha_str]
    df_clase = df_pond[clase_final]
    df_isr= df_base.dot(df_clase).to_frame('IPC Clase')
    df_isr['IPC Clase'] = df_isr['IPC Clase'] / df_isr.loc[fecha_str, 'IPC Clase'] * 100
    df_isr['ISAL'] = df_all.loc[fecha_str:, 'Indice_Salarial'] / df_all.loc[fecha_str, 'Indice_Salarial'] * 100
    df_isr['ISR'] = df_isr['ISAL'] / df_isr['IPC Clase'] * 100
    fig, ax = plt.subplots(figsize=(10, 6))

    # 2. Dibujamos las 3 líneas usando el índice (las fechas) en el eje X
    ax.plot(df_isr.index, df_isr['ISR'], label='Salario Real (Poder de Compra)', color='#1f77b4', linewidth=3) # Azul más grueso

    # 3. Agregamos tu línea horizontal mágica en 100
    ax.axhline(100, color='red', linestyle='--', linewidth=1.5, label='Base 100')

    # 4. Ajustes estéticos para que parezca de nivel profesional
    ax.set_title(f"Salarios vs. Inflación desde {fecha_inicio.strftime('%b %Y')}", fontsize=14)
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Índice (Base 100)", fontsize=12)
    
    # Ponemos la leyenda que habías pedido
    ax.legend(loc='best')
    
    # Le agregamos una cuadrícula suave de fondo para que los valores sean fáciles de leer
    ax.grid(True, linestyle='--', alpha=0.5)

    # 5. ¡Lo disparamos a la pantalla de Streamlit!
    st.pyplot(fig)
