
#SCRIPT PARA RENOMBRAR ARCHIVOS PDF y SE GUARDA EN OTRA CARPETA.

import os
import re
import PyPDF2
 
# Function to extract L.E / DNI number
def extract_dni_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
 
        # Regular expression to find 'L.E / DNI - XXXXXXXX'
        match = re.search(r'L\.E\s*/\s*DNI\s*-\s*(\d+)', text)
        if match:
            return match.group(1)  # Extracted DNI number
        return None
 
# Directory containing PDFs (current directory)
#directory = os.getcwd()

# Carpeta de origen (donde están los PDFs)
source_directory = r"C:\Users\user\OneDrive\Desktop\Pruebas"
# Carpeta de destino (donde se guardarán los PDFs renombrados)
destination_directory = r"C:\Users\user\OneDrive\Desktop\Pruebas\Resultado"
 
# Loop through all PDFs in the directory
for filename in os.listdir(source_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(source_directory, filename)
        dni_number = extract_dni_from_pdf(pdf_path)
 
        if dni_number:
            # New name based on the extracted DNI
            new_filename = f"{dni_number}.pdf"
            new_path = os.path.join(destination_directory, new_filename)
 
            # Rename the file
            os.rename(pdf_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}' y movido a la carpeta de destino.")
        else:
            print(f"DNI number not found in '{filename}'")
 

