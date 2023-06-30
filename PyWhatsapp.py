import pandas

import pywhatkit


###################################################################
#funcion para listar los numeros ya verificados que tiene whatsapp
def listar_numeros():
    df = pandas.read_excel("D:/NewTool/REPORTE_NUMEROS_ACTIVOS.xlsx",sheet_name="REGISTRADOS EN WHATSAPP")
    #convierto el dataFrame en una lista
    numeros = df["Numero"].tolist()
    #elimino el primer elemento(vacio)
    numeros.pop(0)

    numeros_str = []

    for numero in numeros:
        numero_str = str(numero) 
        numeros_str.append(numero_str.rstrip('.0')) # rstrip elimina los caracteres especificados al final de la cadena
    return numeros_str
###################################################################






print(listar_numeros())