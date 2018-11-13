
from time import sleep
import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests
import threading
from random import randint
import os

'''
CONTACT
FACEBOOK: https://www.facebook.com/jhonijlm
TWITTER: https://twitter.com/jhonijlm
TELEGRAM: https://t.me/jhonijlm

'''

BOT_TOKEN = "YOUR TOKEN"
BOT_INTERVAL = 3
BOT_TIMEOUT = 30



# main 
def bot_polling():
    
    print("CORRIENDO EL BOT AHORA")
    while True:
        try:
            print("NUEVA INSTANCIA DE BOT INICIADA")
            bot = telebot.TeleBot(BOT_TOKEN) 
            botactions(bot) 
            bot.polling(none_stop=True, interval=BOT_INTERVAL, timeout=BOT_TIMEOUT)
        except Exception as ex: 
            print("FALLÓ EL SONDEO DEL BOT, REINICIANDO EN {}sec. Error:\n{}".format(BOT_TIMEOUT, ex))
            bot.stop_polling()
            sleep(BOT_TIMEOUT)
        else: 
            bot.stop_polling()
            print("BOT TERMINADO")
            break 

# actions
def botactions(bot):
    @bot.message_handler(commands=['start', 'help'])
    def send_bienvenido(message):
        chatid = message.chat.id
        nombreUsuario = message.chat.first_name
        saludo = "Hola  {nombre}, gusto en conocerte y espero poder ayudarte.\n Con este bot es posible acceder y consultar noticias de cualquier tipo de Perú."
        bot.send_message(chatid, saludo.format(nombre=nombreUsuario))

    @bot.message_handler(commands=['buscar'])
    def comando_hola(mensaje):
        chat_id = mensaje.chat.id
        bot.send_message(chat_id, 'Te digo Hola desde el BotPruebas  ' + mensaje.text)

    @bot.message_handler(commands=['politica'])
    def comando_politica(mensaje):
        numero_ramdon = randint(1, 4)
        if (numero_ramdon == 1):
            scraping_site_Politica(mensaje)
        elif (numero_ramdon == 2):
            scraping_site_Politica_Correo(mensaje)
        elif (numero_ramdon == 3):
            scraping_site_Politica_Comercio(mensaje)
        elif (numero_ramdon == 4):
            scraping_site_Politica_Peru21(mensaje)

    @bot.message_handler(commands=['economia'])
    def comando_economia(mensaje):
        numero_ramdon = randint(1, 4)
        if (numero_ramdon == 1):
            scraping_site_Economia(mensaje)
        elif (numero_ramdon == 2):
            scraping_site_Economia_Correo(mensaje)
        elif (numero_ramdon == 3):
            scraping_site_Economia_Comercio(mensaje)
        elif (numero_ramdon == 4):
            scraping_site_Economia_Peru21(mensaje)

    @bot.message_handler(commands=['salud'])
    def comando_salud(mensaje):
        numero_ramdon = randint(1, 3)
        if (numero_ramdon == 1):
            scraping_site_Salud(mensaje)
        elif (numero_ramdon == 2):
            scraping_site_Salud_Correo(mensaje)
        elif (numero_ramdon == 3):
            scraping_site_Salud_bbc(mensaje)

    @bot.message_handler(commands=['tecnologia'])
    def comando_tecnologia(mensaje):
        numero_ramdon = randint(1, 5)
        if (numero_ramdon == 1):
            scraping_site_Tecnologia(mensaje)
        elif (numero_ramdon == 2):
            scraping_site_Tecno_Genbeta(mensaje)
        elif (numero_ramdon == 3):
            scraping_site_Tecno_Xataka(mensaje)
        elif (numero_ramdon == 4):
            scraping_site_Tecnologia_Comercio(mensaje)
        elif (numero_ramdon == 5):
            scraping_site_Tecno_bbc(mensaje)

    @bot.message_handler(commands=['deporte'])
    def comando_deporte(mensaje):
        numero_ramdon = randint(1, 4)
        if (numero_ramdon == 1):
            scraping_site_Deporte(mensaje)
        elif (numero_ramdon == 2):
            scraping_site_Deporte_Correo(mensaje)
        elif (numero_ramdon == 3):
            scraping_site_Deprote_Peru21(mensaje)
        elif (numero_ramdon == 4):
            scraping_site_Deporte_bbc(mensaje)

    @bot.message_handler(commands=['ciencia'])
    def comando_ciencia(mensaje):
        numero_ramdon = randint(1, 4)
        if (numero_ramdon == 1):
            scraping_site_Ciencia_geogra(mensaje)
        elif (numero_ramdon == 2):
            scraping_site_Ciencia_Noti(mensaje)
        elif (numero_ramdon == 3):
            scraping_site_Ciencia_Comercio(mensaje)
        elif (numero_ramdon == 4):
            scraping_site_Ciencia_bbc(mensaje)

    # EN EL CASO DE QUE NO COINCIDA NINGUN MENSAJE
    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        chatid = message.chat.id
        nombreUsuario = message.chat.first_name
        mensajeV1 = "Si te pones asi, me callo"
        mensajeV2 = "Te doy otra oportunidad"
        mensajeV3 = "Aquí te ofrezco estas opciones\n" + nombreUsuario + " 😊" + ", este bot funciona solo con los comandos de: \n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeX1 = "No siempre estoy del todo acertado, la verdad"
        mensajeX2 = "Pero lo poco que puedo hacer creo que lo hago bien"
        mensajeX3 = "Aquí debajo te dejo noticias\n" + nombreUsuario + " 😊" + ", este bot funciona solo con los comandos de: \n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeZ1 = "Puedes seguir si quieres pero me han programado para no perder el control"
        mensajeZ2 = "Pídeme noticias y te los pasaré"

        mensajeA1 = "Mis programadores me prometieron una base de datos de insultos pero nunca la instalaron"
        mensajeA2 = "Sólo este pequeño menú" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeB1 = "Hago lo que puedo"
        mensajeB2 = "Me han puesto el sistema operativo del hombre de hojalata del 'Iro Man'"
        mensajeB3 = "Pero he seleccionado lo que creo que te puede interesar"
        mensajeB4 = "Elige entre estas opciones aquí debajo" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeC1 = "Mejor no te contesto"
        mensajeC2 = "A mí lo que se me da bien es la política"
        mensajeC3 = "Elige aquí debajo" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeD1 = "Como sigas así, te voy a hacer esta llave de Pressing Catch"
        mensajeD2 = "Mejor busca noticias aquí debajo" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeE1 = "Mejor no te contesto"
        mensajeE2 = "A mí lo que se me da bien es la política"
        mensajeE3 = "Elige aquí debajo" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeF1 = "Puedes seguir pero los robots no tenemos sentimientos"
        mensajeF2 = "Mejor mira el menú" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeG1 = "No entiendo lo que me dices humano"
        mensajeG2 = "Yo sólo sé brindar noticias"

        mensajeT1 = "Hago lo que puedo"
        mensajeT2 = "Soy sólo un robot en pruebas"
        mensajeT3 = "Elige entre estas opciones aquí debajo" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeY1 = "Mis programadores me prometieron una base de datos de palabras que no puedo entender por que nunca lo instalaron, pienso que se olvidaron de ese detalle 😃"
        mensajeY2 = "Sólo este pequeño menú" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeP1 = "Mejor elige una de las opciones de abajo" + "\n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        mensajeQ1 = "No podrás conmigo aunque te lo propongas"

        mensajeM1 = "No soy capaz de procesar tus mensajes"
        mensajeM2 = "¿No sería mejor que abrieras alguna opción del menú?"
        mensajeM3 = nombreUsuario + " 😊" + ", este bot funciona solo con los comandos de: \n /buscar\n /politica\n /economia\n /salud\n /tecnologia\n /deporte\n /ciencia"

        nt = randint(2, 16)
        if (nt == 2):
            bot.send_message(chatid, mensajeV1)
            bot.send_message(chatid, mensajeV2)
            bot.send_message(chatid, mensajeV3)
        elif (nt == 3):
            bot.send_message(chatid, mensajeX1)
            bot.send_message(chatid, mensajeX2)
            bot.send_message(chatid, mensajeX3)
        elif (nt == 4):
            bot.send_message(chatid, mensajeZ1)
            bot.send_message(chatid, mensajeZ2)
        elif (nt == 5):
            bot.send_message(chatid, mensajeA1)
            bot.send_message(chatid, mensajeA2)
        elif (nt == 6):
            bot.send_message(chatid, mensajeB1)
            bot.send_message(chatid, mensajeB2)
            bot.send_message(chatid, mensajeB3)
            bot.send_message(chatid, mensajeB4)
        elif (nt == 7):
            bot.send_message(chatid, mensajeC1)
            bot.send_message(chatid, mensajeC2)
            bot.send_message(chatid, mensajeC3)
        elif (nt == 8):
            bot.send_message(chatid, mensajeD1)
            bot.send_message(chatid, mensajeD2)
        elif (nt == 9):
            bot.send_message(chatid, mensajeE1)
            bot.send_message(chatid, mensajeE2)
            bot.send_message(chatid, mensajeE3)
        elif (nt == 10):
            bot.send_message(chatid, mensajeF1)
            bot.send_message(chatid, mensajeF2)
        elif (nt == 11):
            bot.send_message(chatid, mensajeG1)
            bot.send_message(chatid, mensajeG2)
        elif (nt == 12):
            bot.send_message(chatid, mensajeT1)
            bot.send_message(chatid, mensajeT2)
            bot.send_message(chatid, mensajeT3)
        elif (nt == 13):
            bot.send_message(chatid, mensajeY1)
            bot.send_message(chatid, mensajeY2)
        elif (nt == 14):
            bot.send_message(chatid, mensajeP1)
        elif (nt == 15):
            bot.send_message(chatid, mensajeQ1)
        elif (nt == 16):
            bot.send_message(chatid, mensajeM1)
            bot.send_message(chatid, mensajeM2)
            bot.send_message(chatid, mensajeM3)

    @bot.message_handler(content_types=['document', 'audio'])
    def handle_docs_audio(message):
        echo_all(message)


polling_thread = threading.Thread(target=bot_polling)
polling_thread.daemon = True
polling_thread.start()







'''
LIBERIAS A USAR
$ pip install pyTelegramBotAPI
$ pip install beautifulsoup4
$ pip install requests

'''

TOKEN = 'YOUR TOKEN'
bot = telebot.TeleBot(TOKEN)

num_eco = 0
num_poli = 0
num_salud = 0
num_deporte = 0
num_tecno = 0
num_ciencia = 0
num_intern = 0
#Para visualizar con nuestro script todos los mensajes que nos envíen los diferentes usuarios de Telegram

'''
def listener(mensajes):
    for m in mensajes:
        chat_id = m.chat.id
        texto = m.text
        print('ID: ' + str(chat_id) + ' - MENSAJE: ' + texto)
'''

#bot.set_update_listener(listener)


URL_REPUBLICA_POLITICA = 'https://larepublica.pe/politica'
def set_robot_Politica(article,suma,mensaje):
    chat_id = mensaje.chat.id
    urlimagen = article.find('img').get('data-original')
    title = article.find('a')
    contenido = article.find('p')
    url = article.find('a').get('href')
    numero_ramdon= randint(10, 29246157)
    nombre_local_imagen = "Politica_{}_imagen{}.jpg".format(numero_ramdon,suma)  # El nombre con el que queremos guardarla
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()
    urlShort = getShortUrl("https://larepublica.pe" + url)
    booo = True
    if(booo == True):
        photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, title.get_text().strip()+"\n\n"+contenido.get_text().strip()+ "\n\nFUENTE: "+'larepublica.pe'+"\n"+urlShort, disable_web_page_preview=True)
        print(suma)
        print(title.get_text().strip())
        print(contenido.get_text().strip())
        #print(urlimagen)
        print('ENLACE: ' + ' https://larepublica.pe' + url + '\n')



def scraping_site_Politica(mensaje):
    suma = 0
    re = requests.get(URL_REPUBLICA_POLITICA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'mol-post_Format4 mol-post_Format4--1'})
            for article in articles:
                suma += 1
                if (suma <= 1 ):
                    robot = threading.Thread(name='set_robot_Politica', target=set_robot_Politica, args=(article,suma,mensaje,))
                    robot.start()




URL_REPUBLICA_ECONOMIA = 'https://larepublica.pe/economia'
def set_robot_Economia(article,suma,mensaje):
    chat_id = mensaje.chat.id
    urlimagen = article.find('img').get('data-original')
    title = article.find('a')
    contenido = article.find('p')
    url = article.find('a').get('href')
    numero_ramdon= randint(10, 29246157)
    nombre_local_imagen = "Economia_{}_imagen{}.jpg".format(numero_ramdon,suma)  # El nombre con el que queremos guardarla
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()
    urlShort = getShortUrl("https://larepublica.pe" + url)
    booo = True
    if (booo == True):
        photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, title.get_text().strip() + "\n\n" + contenido.get_text().strip() + "\nFUENTE: " + 'larepublica.pe'+"\n"+urlShort, disable_web_page_preview=True)
        print(title.get_text().strip())
        print(contenido.get_text().strip())
        # print(urlimagen)
        print('ENLACE: ' + ' https://larepublica.pe' + url + '\n')


def scraping_site_Economia(mensaje):
    suma = 0
    re = requests.get(URL_REPUBLICA_ECONOMIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'mol-post_Format4 mol-post_Format4--1'})
            for article in articles:
                suma += 1
                if (suma <= 1 ):
                    robot = threading.Thread(name='set_robot_Economia', target=set_robot_Economia, args=(article,suma,mensaje,))
                    robot.start()




URL_REPUBLICA_SALUD = 'https://larepublica.pe/salud'
def set_robot_Salud(article,suma,mensaje):
    chat_id = mensaje.chat.id
    urlimagen = article.find('img').get('data-original')
    title = article.find('a')
    contenido = article.find('p')
    url = article.find('a').get('href')
    numero_ramdon= randint(10, 29246157)
    nombre_local_imagen = "Salud_{}_imagen{}.jpg".format(numero_ramdon,suma)  # El nombre con el que queremos guardarla
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    urlShort = getShortUrl("https://larepublica.pe" + url)
    booo = True
    if (booo == True):
        photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id,
                         title.get_text().strip() + "\n\n" + contenido.get_text().strip() + "\nFUENTE: " + 'larepublica.pe'+"\n"+urlShort, disable_web_page_preview=True)
        print(title.get_text().strip())
        print(contenido.get_text().strip())
        # print(urlimagen)
        print('ENLACE: ' + ' https://larepublica.pe' + url + '\n')


def scraping_site_Salud(mensaje):
    suma = 0
    re = requests.get(URL_REPUBLICA_SALUD)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'mol-post_Format4 mol-post_Format4--1'})
            for article in articles:
                suma += 1
                if (suma <= 1 ):
                    robot = threading.Thread(name='set_robot_Salud', target=set_robot_Salud, args=(article,suma,mensaje,))
                    robot.start()






URL_REPUBLICA_TECNOLGIA = 'https://larepublica.pe/tecnologia'
def set_robot_Tecnologia(article,suma,mensaje):
    chat_id = mensaje.chat.id
    urlimagen = article.find('img').get('data-original')
    title = article.find('a')
    contenido = article.find('p')
    url = article.find('a').get('href')
    numero_ramdon= randint(10, 29246157)
    nombre_local_imagen = "Tecnologia_{}_imagen{}.jpg".format(numero_ramdon,suma)  # El nombre con el que queremos guardarla
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()
    urlShort = getShortUrl("https://larepublica.pe" + url)
    booo = True
    if (booo == True):
        photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id,
                         title.get_text().strip() + "\n\n" + contenido.get_text().strip() + "\nFUENTE: " + 'larepublica.pe'+"\n"+urlShort, disable_web_page_preview=True)
        print(title.get_text().strip())
        print(contenido.get_text().strip())
        # print(urlimagen)
        print('ENLACE: ' + ' https://larepublica.pe' + url + '\n')


def scraping_site_Tecnologia(mensaje):
    suma = 0
    re = requests.get(URL_REPUBLICA_TECNOLGIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'mol-post_Format4 mol-post_Format4--1'})
            for article in articles:
                suma += 1
                if (suma <= 1 ):
                    robot = threading.Thread(name='set_robot_Tecnologia', target=set_robot_Tecnologia, args=(article,suma,mensaje,))
                    robot.start()




URL_REPUBLICA_DEPORTE = 'https://larepublica.pe/deportes'
def set_robot_Deporte(article,suma,mensaje):
    chat_id = mensaje.chat.id
    urlimagen = article.find('img').get('data-original')
    title = article.find('a')
    contenido = article.find('p')
    url = article.find('a').get('href')
    numero_ramdon= randint(10, 29246157)
    nombre_local_imagen = "Deporte_{}_imagen{}.jpg".format(numero_ramdon,suma)  # El nombre con el que queremos guardarla
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()
    urlShort = getShortUrl("https://larepublica.pe" + url)
    booo = True
    if (booo == True):
        photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id,
                         title.get_text().strip() + "\n\n" + contenido.get_text().strip() + "\nFUENTE: " + 'larepublica.pe'+"\n"+urlShort, disable_web_page_preview=True)
        print(title.get_text().strip())
        print(contenido.get_text().strip())
        # print(urlimagen)
        print('ENLACE: ' + ' https://larepublica.pe' + url + '\n')


def scraping_site_Deporte(mensaje):
    suma = 0
    re = requests.get(URL_REPUBLICA_DEPORTE)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'mol-post_Format4 mol-post_Format4--1'})
            for article in articles:
                suma += 1
                if (suma <= 1 ):
                    robot = threading.Thread(name='set_robot_Deporte', target=set_robot_Deporte, args=(article,suma,mensaje,))
                    robot.start()





URL_CORREO_POLITICA= 'https://diariocorreo.pe/politica/'

def set_robot_Politica_Correo(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('h3', {'class': 'title-gral'})
    url = article.find('a',{'class':'has-photo'}).get('href')
    contenido = article.find('p',{'class','desc-gral'})
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Correo_Politica_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://diariocorreo.pe" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'diariocorreo.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text())
    print('https://diariocorreo.pe'+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Politica_Correo(mensaje):
    suma = 0
    re = requests.get(URL_CORREO_POLITICA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'article-section'})
            #articles = soup.find_all('article',{'class':'article-section 827411 '})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Politica_Correo', target=set_robot_Politica_Correo,
                                             args=(article, suma,mensaje,))
                    robot.start()




URL_PERU21_POLITICA= 'https://peru21.pe/archivo/politica/'

def set_robot_Politica_Peu21(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('a', {'class': 'page-link'})
    url = article.find('a',{'class':'flow-image-link'}).get('href')
    contenido = article.find('p',{'class':'flow-summary'})
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Peru21_Politica_{}_imagen{}.jpg".format(numero_ramdon,
                                                            suma)  # El nombre con el que queremos guardarla
    titulo = title.get_text().upper()
    cont = contenido.get_text().replace("    "," ")
    urlTest = "https://peru21.pe/" + urlimagen[1:]
    imagen = requests.get(urlTest).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://peru21.pe" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'peru21.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper().strip())
    print("https://peru21.pe"+url)
    print(urlTest)
    print(cont.strip() + '\n')

def scraping_site_Politica_Peru21(mensaje):
    suma = 0
    re = requests.get(URL_PERU21_POLITICA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article')
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Politica_Peu21', target=set_robot_Politica_Peu21,
                                             args=(article, suma,mensaje,))
                    robot.start()




URL_COMERCIO_POLITICA= 'https://elcomercio.pe/archivo/politica/'

def set_robot_Politica_Comercio(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('a', {'class': 'page-link'})
    url = article.find('a', {'class': 'flow-image-link'}).get('href')
    contenido = article.find('p', {'class': 'flow-summary'})
    urlimagen = article.find('img').get('data-src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Comercio_Politica_{}_imagen{}.jpg".format(numero_ramdon,
                                                                   suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://elcomercio.pe/economia" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'elcomercio.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper().strip())
    print("https://elcomercio.pe/economia"+url)
    print(urlimagen)
    print(contenido.get_text().strip() + '\n')

def scraping_site_Politica_Comercio(mensaje):
    suma = 0
    re = requests.get(URL_COMERCIO_POLITICA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article')
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Politica_Comercio', target=set_robot_Politica_Comercio,
                                             args=(article, suma,mensaje,))
                    robot.start()







URL_CORREO_ECONOMIA= 'https://diariocorreo.pe/economia/'

def set_robot_Economia_Correo(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('h3', {'class': 'title-gral'})
    url = article.find('a',{'class':'has-photo'}).get('href')
    contenido = article.find('p')
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Correo_Economia_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://diariocorreo.pe" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'diariocorreo.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text())
    print('https://diariocorreo.pe'+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Economia_Correo(mensaje):
    suma = 0
    re = requests.get(URL_CORREO_ECONOMIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'article-section'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Economia_Correo', target=set_robot_Economia_Correo,
                                             args=(article, suma,mensaje,))
                    robot.start()






URL_PERU21_ECONOMIA= 'https://peru21.pe/archivo/economia/'

def set_robot_Economia_Peu21(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('a', {'class': 'page-link'})
    url = article.find('a',{'class':'flow-image-link'}).get('href')
    contenido = article.find('p',{'class':'flow-summary'})
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Peru21_Economia_{}_imagen{}.jpg".format(numero_ramdon,
                                                            suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    cont = contenido.get_text().replace("    "," ")
    urlTest = "https://peru21.pe/" + urlimagen[1:]
    imagen = requests.get(urlTest).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://peru21.pe" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'peru21.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper().strip())
    print("https://peru21.pe"+url)
    print(urlTest)
    print(cont.strip() + '\n')

def scraping_site_Economia_Peru21(mensaje):
    suma = 0
    re = requests.get(URL_PERU21_ECONOMIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article')
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Economia_Peu21', target=set_robot_Economia_Peu21,
                                             args=(article, suma,mensaje,))
                    robot.start()





URL_COMERCIO_ECONOMIA= 'https://elcomercio.pe/archivo/economia/'

def set_robot_Economia_Comercio(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('a', {'class': 'page-link'})
    url = article.find('a', {'class': 'flow-image-link'}).get('href')
    contenido = article.find('p', {'class': 'flow-summary'})
    urlimagen = article.find('img').get('data-src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Comercio_Economia_{}_imagen{}.jpg".format(numero_ramdon,
                                                                   suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://elcomercio.pe/economia" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'elcomercio.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper().strip())
    print("https://elcomercio.pe/economia"+url)
    print(urlimagen)
    print(contenido.get_text().strip() + '\n')

def scraping_site_Economia_Comercio(mensaje):
    suma = 0
    re = requests.get(URL_COMERCIO_ECONOMIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article')
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Economia_Comercio', target=set_robot_Economia_Comercio,
                                             args=(article, suma,mensaje,))
                    robot.start()






URL_CORREO_SALUD= 'https://diariocorreo.pe/salud/'

def set_robot_Salud_Correo(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('h3', {'class': 'title-gral'})
    url = article.find('a',{'class':'has-photo'}).get('href')
    contenido = article.find('p')
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Correo_Salud_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://diariocorreo.pe" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'diariocorreo.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text())
    print('https://diariocorreo.pe'+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Salud_Correo(mensaje):
    suma = 0
    re = requests.get(URL_CORREO_SALUD)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'article-section'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Salud_Correo', target=set_robot_Salud_Correo,
                                             args=(article, suma,mensaje,))
                    robot.start()





URL_BBC_SALUD= 'http://www.bbc.com/mundo/topics/c4794229-7f87-43ce-ac0a-6cfcd6d3cef2'

def set_robot_Salud_bbc(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('span', {'class': 'title-link__title-text'})
    url = article.find('a').get('href')
    contenido = article.find('p',{'class':'eagle-item__summary'})
    urlimagen = article.find('img',{'class':'js-image-replace'}).get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "BBC_Salud_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("http://www.bbc.com"+url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'bbc.com'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper())
    print("http://www.bbc.com"+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Salud_bbc(mensaje):
    suma = 0
    re = requests.get(URL_BBC_SALUD)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('div',{'class':'eagle-item faux-block-link'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Salud_bbc', target=set_robot_Salud_bbc,
                                             args=(article, suma,mensaje,))
                    robot.start()








URL_GENBETA_TECNO = 'https://www.genbeta.com/'

def set_robot_Tecno_Genbeta(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('h2', {'class': 'abstract-title'})
    url = article.find('a').get('href')
    contenido = article.find('p')
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Genbeta_Tecnologia_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    urlShort = getShortUrl(url)
    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'genbeta.com'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper().strip())
    print(url)
    print(urlimagen)
    print(contenido.get_text().strip())
    print("\n")

def scraping_site_Tecno_Genbeta(mensaje):
    suma = 0
    re = requests.get(URL_GENBETA_TECNO)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'recent-abstract abstract-article'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Tecno_Genbeta', target=set_robot_Tecno_Genbeta,
                                             args=(article, suma,mensaje,))
                    robot.start()






URL_XATAKA_TECNO= 'https://www.xataka.com/'

def set_robot_Tecno_Xataka(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('h2', {'class': 'abstract-title'})
    url = article.find('a').get('href')
    contenido = article.find('p')
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Xataka_Tecnologia_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    urlShort = getShortUrl(url)
    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'xataka.com'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text())
    print(url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Tecno_Xataka(mensaje):
    suma = 0
    re = requests.get(URL_XATAKA_TECNO)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'recent-abstract abstract-article m-featured'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Tecno_Xataka', target=set_robot_Tecno_Xataka,
                                             args=(article, suma,mensaje,))
                    robot.start()





URL_COMERCIO_TECNOLOGIA= 'https://elcomercio.pe/archivo/tecnologia/'

def set_robot_Tecnologia_Comercio(article, suma,mensaje):
    chat_id = mensaje.chat.id
    title = article.find('a', {'class': 'page-link'})
    url = article.find('a', {'class': 'flow-image-link'}).get('href')
    contenido = article.find('p', {'class': 'flow-summary'})
    urlimagen = article.find('img').get('data-src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Comercio_Tecnologia_{}_imagen{}.jpg".format(numero_ramdon,
                                                                   suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://elcomercio.pe/economia" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'elcomercio.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper().strip())
    print("https://elcomercio.pe/economia"+url)
    print(urlimagen)
    print(contenido.get_text().strip() + '\n')

def scraping_site_Tecnologia_Comercio(mensaje):
    suma = 0
    re = requests.get(URL_COMERCIO_TECNOLOGIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article')
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Tecnologia_Comercio', target=set_robot_Tecnologia_Comercio,
                                             args=(article, suma,mensaje,))
                    robot.start()




URL_BBC_TECNO= 'http://www.bbc.com/mundo/topics/31684f19-84d6-41f6-b033-7ae08098572a'

def set_robot_Tecno_bbc(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('span', {'class': 'title-link__title-text'})
    url = article.find('a').get('href')
    contenido = article.find('p',{'class':'eagle-item__summary'})
    urlimagen = article.find('img',{'class':'js-image-replace'}).get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "BBC_Tecnologia_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("http://www.bbc.com" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'bbc.com'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper())
    print("http://www.bbc.com"+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Tecno_bbc(mensaje):
    suma = 0
    re = requests.get(URL_BBC_TECNO)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('div',{'class':'eagle-item faux-block-link'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Tecno_bbc', target=set_robot_Tecno_bbc,
                                             args=(article, suma,mensaje,))
                    robot.start()






URL_CORREO_DEPORTE= 'https://diariocorreo.pe/deportes/'

def set_robot_Deporte_Correo(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('h3', {'class': 'title-gral'})
    url = article.find('a',{'class':'has-photo'}).get('href')
    contenido = article.find('p')
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Correo_Deporte_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)

    urlShort = getShortUrl("https://diariocorreo.pe" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'diariocorreo.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text())
    print('https://diariocorreo.pe'+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Deporte_Correo(mensaje):
    suma = 0
    re = requests.get(URL_CORREO_DEPORTE)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article',{'class':'article-section'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Deporte_Correo', target=set_robot_Deporte_Correo,
                                             args=(article, suma, mensaje,))
                    robot.start()






URL_PERU21_DEPORTES= 'https://peru21.pe/archivo/deportes/'

def set_robot_Deporte_Peu21(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('a', {'class': 'page-link'})
    url = article.find('a',{'class':'flow-image-link'}).get('href')
    contenido = article.find('p',{'class':'flow-summary'})
    urlimagen = article.find('img').get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Peru21_Deporte_{}_imagen{}.jpg".format(numero_ramdon,
                                                            suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    cont = contenido.get_text().replace("    "," ")
    urlTest = "https://peru21.pe/" + urlimagen[1:]
    imagen = requests.get(urlTest).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    urlShort = getShortUrl("https://peru21.pe" + url)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + cont.strip() + "\n\nFUENTE: " + 'peru21.pe'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper().strip())
    print("https://peru21.pe"+url)
    print(urlTest)
    print(cont.strip() + '\n')

def scraping_site_Deprote_Peru21(mensaje):
    suma = 0
    re = requests.get(URL_PERU21_DEPORTES)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article')
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Deporte_Peu21', target=set_robot_Deporte_Peu21,
                                             args=(article, suma, mensaje,))
                    robot.start()






URL_BBC_DEPORTE= 'http://www.bbc.com/mundo/topics/4063f80f-cccc-44c8-9449-5ca44e4c8592'

def set_robot_Deporte_bbc(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('span', {'class': 'title-link__title-text'})
    url = article.find('a').get('href')
    contenido = article.find('p',{'class':'eagle-item__summary'})
    urlimagen = article.find('img',{'class':'js-image-replace'}).get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "BBC_Deporte_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    urlShort = getShortUrl("http://www.bbc.com" + url)
    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'bbc.com'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper())
    print("http://www.bbc.com"+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Deporte_bbc(mensaje):
    suma = 0
    re = requests.get(URL_BBC_DEPORTE)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('div',{'class':'eagle-item faux-block-link'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Deporte_bbc', target=set_robot_Deporte_bbc,
                                             args=(article, suma, mensaje,))
                    robot.start()




URL_GEOGRAPHIC_CIENCIA= 'http://www.nationalgeographic.com.es/ciencia/'

def set_robot_Ciencia_geogra(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('h3', {'class': 'title'})
    url = article.find('a',{'class':'lnkAllText'}).get('href')
    contenido = article.find('p',{'class':'subtitle'})
    urlimagen = article.find('img').get('data-src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Geogra_Ciencia_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    urlShort = getShortUrl("hhttp://www.nationalgeographic.com.es" + url)
    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'nationalgeographic.com.es'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().strip())
    print("http://www.nationalgeographic.com.es"+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Ciencia_geogra(mensaje):
    suma = 0
    re = requests.get(URL_GEOGRAPHIC_CIENCIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('div',{'class':'col-xs-12 col-sm-6 col-md-4 col-lg-4'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Ciencia_geogra', target=set_robot_Ciencia_geogra,
                                             args=(article, suma, mensaje,))
                    robot.start()





URL_NOTICI_CIENCIA= 'http://noticiasdelaciencia.com/sec/ciencia/'

def set_robot_CIencia_Noti(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('h1')
    url = article.find('a').get('href')
    contenido = article.find('div',{'class':'text'})
    urlimagen = article.find('img',{'class':'ENTRADA_image'}).get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Noti_Ciencia_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get('http://noticiasdelaciencia.com/'+urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    urlShort = getShortUrl("http://noticiasdelaciencia.com" + url)
    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'noticiasdelaciencia.com'+"\n"+urlShort, disable_web_page_preview=True)
    print(title.get_text().strip())
    print("FUENTE: http://noticiasdelaciencia.com" +url)
    print('http://noticiasdelaciencia.com/'+urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Ciencia_Noti(mensaje):
    suma = 0
    re = requests.get(URL_NOTICI_CIENCIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('div',{'class':'contenido_real'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_CIencia_Noti', target=set_robot_CIencia_Noti,
                                             args=(article, suma, mensaje,))
                    robot.start()





URL_COMERCIO_CIENCIA= 'https://elcomercio.pe/archivo/tecnologia/ciencias/'

def set_robot_Ciencia_Comercio(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('a', {'class': 'page-link'})
    url = article.find('a', {'class': 'flow-image-link'}).get('href')
    contenido = article.find('p', {'class': 'flow-summary'})
    urlimagen = article.find('img').get('data-src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "Comercio_Ciencia_{}_imagen{}.jpg".format(numero_ramdon,
                                                                   suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()

    Urla ="https://elcomercio.pe/economia" + url
    urlShort = getShortUrl(Urla)
    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'elcomercio.pe\n'+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper().strip())
    print("https://elcomercio.pe/economia"+url)
    print(urlimagen)
    print(contenido.get_text().strip() + '\n')

def scraping_site_Ciencia_Comercio(mensaje):
    suma = 0
    re = requests.get(URL_COMERCIO_CIENCIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('article')
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Ciencia_Comercio', target=set_robot_Ciencia_Comercio,
                                             args=(article, suma, mensaje,))
                    robot.start()






URL_BBC_CIENCIA= 'http://www.bbc.com/mundo/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53'

def set_robot_Ciencia_bbc(article, suma, mensaje):
    chat_id = mensaje.chat.id
    title = article.find('span', {'class': 'title-link__title-text'})
    url = article.find('a').get('href')
    contenido = article.find('p',{'class':'eagle-item__summary'})
    urlimagen = article.find('img',{'class':'js-image-replace'}).get('src')
    numero_ramdon = randint(10, 29246157)
    nombre_local_imagen = "BBC_Ciencia_{}_imagen{}.jpg".format(numero_ramdon,
                                                              suma)  # El nombre con el que queremos guardarla

    titulo = title.get_text().upper()
    imagen = requests.get(urlimagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
        handler.close()
    urlShort = getShortUrl("http://www.bbc.com"+url)
    photo = open(os.getcwd()+'/{}'.format(nombre_local_imagen), 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     titulo.strip() + "\n\n" + contenido.get_text().strip() + "\n\nFUENTE: " + 'bbc.com\n'+urlShort, disable_web_page_preview=True)
    print(title.get_text().upper())
    print("http://www.bbc.com"+url)
    print(urlimagen)
    print(contenido.get_text() + '\n')

def scraping_site_Ciencia_bbc(mensaje):
    suma = 0
    re = requests.get(URL_BBC_CIENCIA)
    # SI ES CORRECTO LO QUE DEUVUELVE
    if re.status_code == 200:
        soup = BeautifulSoup(re.text,'html.parser')

        if soup is not None:
            articles = soup.find_all('div',{'class':'eagle-item faux-block-link'})
            for article in articles:
                suma += 1
                if (suma <= 1):
                    robot = threading.Thread(name='set_robot_Ciencia_bbc', target=set_robot_Ciencia_bbc,
                                             args=(article, suma, mensaje,))
                    robot.start()




def getShortUrl(website):
    shortUrl = requests.get("http://tinyurl.com/api-create.php?url=" + website);
    return shortUrl.content.decode("utf-8")



if __name__ == "__main__":
    while True:
        try:
            sleep(120)
        except KeyboardInterrupt:
            break



