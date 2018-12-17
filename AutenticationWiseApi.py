import datetime
import hashlib

import bs4

import requests


# ------------------------------------------------------------------------
# Necesario calcular SHA1 y Base64 de Clave Primera Vez
def password(original):
    hoy = datetime.datetime.now().utcnow()
    fechaOrdenada = hoy.strftime('%Y%m%d')
    print "Clave: ", original + fechaOrdenada
    m = hashlib.sha1(original + fechaOrdenada).hexdigest();
    m = m.decode("hex")
    m = m.encode('base64')
    print "Clave: ", m
    return m.strip()


# ------------------------------------------------------------------------
# Necesario calcular SHA1 y Base64 de Clave Consultas
def passConsulta(original):
    m = hashlib.sha1(original).hexdigest();
    m = m.decode("hex")
    m = m.encode('base64')
    print "m:", m
    return m


# ------------------------------------------------------------------------
def getToken(direccion, user, clave):
    headers = {'username': user, 'password': clave}
    print "URL:", direccion
    print "Clave:", clave.strip()
    print "Usuario:", user.strip()
    token = requests.post(direccion, headers=headers)
    soup = bs4.BeautifulSoup(token.content, "html.parser")
    print soup.prettify()

    for link in soup.find_all("token"):
        token = link.text
    print "Token: ", token
    return token
