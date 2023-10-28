import  streamlit as st
import  etl as e

# Configurar la página de Streamlit
st.title("Informe de calidad de datos: ")

st.title("Ingreso de credenciales")

# Pide al usuario que ingrese las credenciales
usuario     = st.text_input("Usuario")
contraseña  = st.text_input("Contraseña", type="password")
servidor    = st.text_input("Servidor")
basededatos = st.text_input("Nombre de la Base de Datos")
tabla       = st.text_input("Nombre de la Tabla")

# Agregar un botón para generar el PDF
if st.button("Conectar DB"):
    resultado = e.cargaDatos(usuario, contraseña, servidor, basededatos, tabla)
    print(resultado)
