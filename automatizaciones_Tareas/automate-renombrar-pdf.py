#SCRIPT PARA RENOMBRAR ARCHIVOS PDF - SE GUARDA EN LA MISMA CARPETA DONDE SE UBICA EL ARCHIVO.

import os
import re
import PyPDF2

# Función para extraer un número del contenido de un PDF
def extraer_numero_del_pdf(pdf_path):
    with open(pdf_path, 'rb') as archivo_pdf:
        lector = PyPDF2.PdfReader(archivo_pdf)
        texto_completo = ""
        for pagina in lector.pages:
            texto_completo += pagina.extract_text()
        
        # Usar expresiones regulares para encontrar el número en el texto
        numero_encontrado = re.search(r'L\.E\s*/\s*DNI\s*-\s*(\d+)', texto_completo)
        
        if numero_encontrado:
            return numero_encontrado.group(1)
        else:
            return None

# Función para renombrar archivos
def renombrar_archivos_pdf(carpeta):
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".pdf"):
            archivo_path = os.path.join(carpeta, archivo)
            numero = extraer_numero_del_pdf(archivo_path)
            
            if numero:
                nuevo_nombre = f"{numero}.pdf"
                nuevo_path = os.path.join(carpeta, nuevo_nombre)
                os.rename(archivo_path, nuevo_path)
                print(f"Archivo renombrado: {archivo} -> {nuevo_nombre}")
            else:
                print(f"No se encontró número en: {archivo}")

# Carpeta donde se encuentran los archivos PDF
carpeta_pdf= r"C:\Users\user\OneDrive\Desktop\Pruebas"

# Ejecutar la función para renombrar los archivos
renombrar_archivos_pdf(carpeta_pdf)
