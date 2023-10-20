import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Crear una función para generar y guardar el archivo PDF
def generar_pdf():
    c = canvas.Canvas("reporte.pdf", pagesize=letter)
    datos = ["Dato 1", "Dato 2", "Dato 3", "Dato 4"]
    x, y = 100, 750
    for dato in datos:
        c.drawString(x, y, dato)
        y -= 20
    c.save()

# Configurar la página de Streamlit
st.title("Generador de PDF")

# Agregar un botón para generar el PDF
if st.button("Generar PDF"):
    generar_pdf()
    st.success("PDF generado correctamente")

# Agregar un botón para descargar el PDF
if st.button("Descargar PDF"):
    with open("reporte.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    st.download_button(
        label="Haz clic para descargar el PDF",
        data=pdf_bytes,
        key="descargar_pdf",
        file_name="reporte.pdf",
    )
