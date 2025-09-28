import pandas as pd
import os

# Ruta de la carpeta que contiene los archivos de Excel
folder_path = r'C:\Users\user\OneDrive\Desktop\Pruebas\Consolidar_excels'

# Crear un diccionario para almacenar los DataFrames por hoja
consolidado = {}

# Iterar sobre cada archivo en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        
        # Leer todas las hojas del archivo de Excel
        xls = pd.ExcelFile(file_path)
        for sheet_name in xls.sheet_names:
            # Leer la hoja en un DataFrame
            df = pd.read_excel(xls, sheet_name)
            
            # Agregar los datos al diccionario, creando una nueva entrada si la hoja no existe
            if sheet_name not in consolidado:
                consolidado[sheet_name] = df
            else:
                consolidado[sheet_name] = pd.concat([consolidado[sheet_name], df], ignore_index=True)

# Crear un archivo de Excel para el resultado consolidado
with pd.ExcelWriter(r'C:\Users\user\OneDrive\Desktop\Pruebas\Consolidar_excels\Reportes_consolidado.xlsx') as writer:
    for sheet_name, df in consolidado.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Consolidación completada.")
