import os
import time
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Importar .csv con contactos y lista de xpath
input_csv = "/home/mariolopez7/PycharmProjects/WA/mehphones.csv"
contactos_lista = pd.read_csv(input_csv)
xpath_csv = "/home/mariolopez7/PycharmProjects/WA/xpath_message_and_attachment.csv"
xpath_lista = pd.read_csv(xpath_csv)

# Use webdriver for Chromium
driver = webdriver.Chrome("/home/mariolopez7/PycharmProjects/WA/chromedriver")
driver.set_page_load_timeout(90)

# Find address
driver.get("http://web.whatsapp.com")
driver.maximize_window()
# Esperar a que cargue pagina
driver.implicitly_wait(30)

# Pausa para escanear código QR
input("Precione enter para continuar")

# Empieza a contar desde 0 y va sumando +1 cada vez hasta que termine
i = 0

# Agregar time.sleep
# Empezar for loop tomando nombre de la columna con la que quieres trabajar, Nombre y Teléfono
# Caja
for contacto, telefono in zip(contactos_lista["Name"], contactos_lista["Phone 1 - Value"]):

    telefono = str(telefono)

    caja_search = driver.find_element_by_xpath(xpath_lista.iloc[0, 1])
    caja_search.send_keys(Keys.CONTROL+"a")
    caja_search.send_keys(Keys.DELETE)

    caja_search.send_keys(contacto)  # Tomar nombre de for loop
    caja_search.send_keys(Keys.ENTER)
    time.sleep(4)

    # Mensaje
    message_box = driver.find_element_by_xpath(xpath_lista.iloc[1, 1])
    message_box.send_keys("Mensaje de Ejemplo")
    time.sleep(3)

    # Send Button
    send_button = driver.find_element_by_xpath(xpath_lista.iloc[2, 1])
    send_button.click()

    # Boton para abrir el clip(Attach)
    print("Abriendo clip")
    clip_button = driver.find_element_by_xpath(xpath_lista.iloc[3, 1])
    clip_button.click()

    time.sleep(4)

    # "Descubrir el boton tipo "file"" en este caso "Imagen"
    # Boton para escoger el archivo a adjuntar
    image_button = driver.find_element_by_xpath(xpath_lista.iloc[4, 1])
    driver.execute_script("arguments[0].setAttribute('style','visibility:visible;');", image_button)

    # Capturar el path de la imagen a enviar + el nombre del archivo (Escribir path)
    print(os.getcwd() + "/promo.png")
    image_button.send_keys("/home/mariolopez7/PycharmProjects/WA/promo.png")

    time.sleep(4)

    # Click en la Flecha de enviar, con el archivo ya cargado
    # Click para enviar imagen
    image_send_button = driver.find_element_by_xpath(xpath_lista.iloc[5, 1])
    image_send_button.click()

    time.sleep(2)

    # Crear log para saber por donde va el programa (Escribir path del log)
    # El valor debe ser el nombre de la columna en la que se encuentran los teléfono celulares
    logging.basicConfig(filename="/home/mariolopez7/PycharmProjects/WA/log.txt", filemode="a", level=logging.INFO,
                        datefmt="%d/%m/%Y %I:%M:%S %p", format="%(asctime)s - %(name)s - %(message)s")
    logging.info(contacto + ", " + str(telefono))

i += 1
