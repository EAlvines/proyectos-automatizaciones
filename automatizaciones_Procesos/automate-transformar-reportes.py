import pandas as pd

ruta_archivo=r'C:\Users\user\OneDrive\Desktop\Practica\PYTHON\Automatizaciones\Prueba_Transformar_Excel.xlsx'
ruta_destino=r'C:\Users\user\OneDrive\Desktop\Practica\PYTHON\Automatizaciones'

df=pd.read_excel(ruta_archivo)

df[['CUENTA', 'GLOSA']].fillna(method='ffill')

df_transformado= df.melt(
    id_vars=['CUENTA', 'GLOSA', 'DESCRIPCION'],
    var_name='MES',
    value_name= 'MONTO'
)

df_transformado.to_excel(f"{ruta_destino}\Excel_transformado.xlsx", index=False)

print("Excel_Transformado OK")