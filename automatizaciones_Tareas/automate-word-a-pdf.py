from docx2pdf import convert
#aquí en r seleccionar la carpeta donde están los archivos word 
origen = r"C:\Users\user\OneDrive\Desktop\Pruebas"
destino = r"C:\Users\user\OneDrive\Desktop\Pruebas\Resultado"

convert(origen, destino)
print("¡Conversión completada y guardada en la carpeta de destino!")

