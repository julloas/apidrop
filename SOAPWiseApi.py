import requests
import hashlib
import datetime
from suds.client import Client




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
    return m

# ------------------------------------------------------------------------
# Necesario calcular SHA1 y Base64 de Clave Consultas
def passConsulta(original):
    m = hashlib.sha1(original).hexdigest();
    m = m.decode("hex")
    m = m.encode('base64')
    print "m:",m
    return m


# ------------------------------------------------------------------------
def getToken(direccion, user, clave):
    headers = {'username':user, 'password': clave}
    print "URL:", direccion
    print "Clave:", clave
    print "Usuario:",user.strip()
    finaltoken = requests.post(direccion, headers=headers)
    soup = BeautifulSoup(finaltoken.content)
    print soup.prettify()

    for link in soup.find_all("token"):
        token = link.text
    print "Token: ", token
    return token


# ------------------------------------------------------------------------
def getSummary(direccion, user, token):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey
    username= user.strip()
    password= nuevaKey.strip()
    print password

    client = Client(direccion, soapheaders=(username, password))
    data = client.service.getSummary()

    soup = BeautifulSoup(data)
    print soup.prettify()

    for tag in soup.find_all('measure'):
        tag
        #print "-----------------------------------------"
        print "Campo:", tag.farm.text
        #print "-----------------------------------------------------------"


# ------------------------------------------------------------------------
def getNuevoToken(direccion, user, token):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey



# ------------------------------------------------------------------------
def getLastData(direccion, user, token, identificador):
    #identificador = identificador.strip()
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey
    username= user
    password= nuevaKey.strip()
    print "ID:", identificador
    client = Client(direccion, soapheaders=(username, password))
    data = client.service.getLastData(identificador)
    soup = BeautifulSoup(data)
    print soup.prettify()
    for tag in soup.find_all('measure'):
        print "-----------------------------------------"
        print "ID", tag['id']
        print "Sector: ",tag['sector']
        print "Sensor:",tag['variable']+ " " + tag['unit']
        print "Fecha:",tag.time.text
        print "Valor", tag.value.text
    return


# ------------------------------------------------------------------------
def getAllData(direccion,user,token,IDs,initTime,endTime):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey
    username= user.strip()
    password= nuevaKey.strip()
    print password
    client = Client(direccion, soapheaders=(username, password))
    data = client.service.getAllData(IDs, initTime, endTime)
    soup = BeautifulSoup(data)
    print soup.prettify()

    for tag in soup.find_all('data'):
        if tag.text != '':
            print "Fecha:", tag.time.text
            print "Valor:", tag.value.text
            print "-----------------------------------------"

# ------------------------------------------------------------------------
def getData(direccion,user,token,IDs, IDOperacion, IDInterval, initTime,endTime):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey
    username= user.strip()
    password= nuevaKey.strip()
    print password
    client = Client(direccion, soapheaders=(username, password))
    data = client.service.getData(IDs, IDOperacion, IDInterval, initTime, endTime)
    soup = BeautifulSoup(data)
    print soup.prettify()

    for tag in soup.find_all('value'):
        if tag.text != '':
            print tag.text
            print "-----------------------------------------"

# ------------------------------------------------------------------------
def getField(direccion, user, token):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey
    username= user.strip()
    password= nuevaKey.strip()
    print password
    client = Client(direccion, soapheaders=(username, password))
    data = client.service.getField()
    soup = BeautifulSoup(data)
    print soup.prettify()

    for tag in soup.find_all('value'):
        if tag.text != '':
            print tag.text
            print "-----------------------------------------"

# ------------------------------------------------------------------------
def getSector(direccion, user, token, identificador):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey
    username= user
    password= nuevaKey.strip()
    print "ID:", identificador
    client = Client(direccion, soapheaders=(username, password))
    data = client.service.getSector(identificador)
    soup = BeautifulSoup(data)
    print soup.prettify()
    #for tag in soup.find_all('measure'):
    #    print "-----------------------------------------"
    #    print "ID", tag['id']
    #    print "Sector: ",tag['sector']
    #    print "Sensor:",tag['unidad']
    #    print "Fecha:",tag.time.text
    #    print "Valor", tag.value.text

# ------------------------------------------------------------------------
def getDailyIrrigationData(direccion,user,token,identificador,initTime,endTime):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey
    username= user
    password= nuevaKey.strip()
    print "ID:", identificador
    client = Client(direccion, soapheaders=(username, password))
    data = client.service.getDailyIrrigationData(identificador,initTime,endTime)
    soup = BeautifulSoup(data)
    print soup.prettify()
    #for tag in soup.find_all('measure'):
    #    print "-----------------------------------------"
    #    print "ID", tag['id']
    #    print "Sector: ",tag['sector']
    #    print "Sensor:",tag['unidad']
    #    print "Fecha:",tag.time.text
    #    print "Valor", tag.value.text

# ------------------------------------------------------------------------
def saveSubscription(direccion, user, token, queryParameters, period, expirationTime, channelParams):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey

    username= user
    password= nuevaKey.strip()

    client = Client(direccion, soapheaders=(username, password))
    print queryParameters
    print channelParams

    data = client.service.saveSubscription(queryParameters, period, expirationTime, channelParams)
    soup = BeautifulSoup(data)
    print soup.prettify()


# ------------------------------------------------------------------------
def deleteSubscription(direccion, user, token, ID):
    API_KEY=token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = passConsulta(API_KEY);
    print "Nueva Key:",nuevaKey

    username= user
    password= nuevaKey.strip()

    client = Client(direccion, soapheaders=(username, password))

    data = client.service.deleteSubscription(ID)
    soup = BeautifulSoup(data)
    print soup.prettify()

# ------------------------------------------------------------------------
    return

