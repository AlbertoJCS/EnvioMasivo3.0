import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

###################################################################
#funcion para listar los numeros ya verificados que tiene whatsapp
def crear_diccionario():
    df = pandas.read_excel("D:/NewTool/REPORTE_NUMEROS_ACTIVOS.xlsx",sheet_name="REGISTRADOS EN WHATSAPP")
    #convierto el dataFrame en una lista
    #numeros = df["NUMERO"].tolist()
    #msj = df["MSJ"].tolist()
    #elimino el primer elemento(vacio)
    #numeros.pop(0)
    dictionary = dict(zip(df["numeros"],df["MSJ"]))
    return dictionary
###################################################################
crear_diccionario();

#########################################################################################################################################################################################################
class whatsapp_bot:
###################################################################
#funcion para crear una instancia de la clase
    def __init__ (self):
        self.driver = None
###################################################################

###################################################################
#funcion para iniciar_sesion
    def iniciar_sesion(self):
        #Configuracion del controlador de Selenium
        service = Service('path/to/chromedriver') #Ruta al controlador de ChromeDriver
        options = Options()
        options.add_argument('--user-data-dir=path/to/profile') # Ruta al perfil de usuario de Chrome

        #Inicializar el controlador de Selenium
        self.driver = webdriver.Chrome(service=service, options=options)

        #Abrir WhatsApp Web
        self.driver.get("https://web.whatsapp.com")
        input("Presiona Enter después de escanear el código QR")
###################################################################

###################################################################
#funcion para enviar mensajes de whatsapp
    def enviar_mensaje(self, numero, mensaje):
        if not self.driver:
            self.iniciar_sesion()
###################################################################

###################################################################
#funcion para enviar mensajes de whatsapp
    def cerrar_sesion(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
###################################################################

#########################################################################################################################################################################################################

bot = whatsapp_bot()


for numero, mensaje in crear_diccionario().items():
    bot.enviar_mensaje(numero, mensaje)
