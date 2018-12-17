# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import requests
import AutenticationWiseApi
from bs4 import BeautifulSoup
from easygui import *
from json import *


def increaseToken(user, token):
    API_KEY = token + '1'
    print "Token Incrementado: ", API_KEY
    nuevaKey = AutenticationWiseApi.passConsulta(API_KEY);
    print "Nueva Key:", nuevaKey
    username = user.strip()
    password = nuevaKey.strip()
    print password
    return username, password


# ------------------------------------------------------------------------
#                       REST CODES
#  -----------------------------------------------------------------------

def restGetSummary(direccion, user, token):
    username, password = increaseToken(user, token)
    headers = {'Accept':'application/json', 'username':username, 'password': password}
    print headers
    data = requests.get(direccion, headers=headers)
    parsed = loads(data.content)
    codebox("Summary for user:"+username, "GetSummary Response", dumps(parsed, indent=4, sort_keys=True))
    return

# ------------------------------------------------------------------------
def restGetLastData(direccion, user, token, identificador):
    username, password = increaseToken(user, token)
    headers = {'Accept':'application/json', 'username':username, 'password': password}
    print headers
    payload = {'ids':str(identificador)}
    print "Payload:", payload
    data = requests.get(direccion, headers=headers, params=payload)
    print (data.url)
    parsed = loads(data.content)
    codebox("Last Data for user:"+username, "GetLastData Response", dumps(parsed, indent=4, sort_keys=True))
    return

# ------------------------------------------------------------------------
def restGetData(direccion,user,token,IDs, IDOperacion, IDInterval, initTime,endTime):
    username, password = increaseToken(user, token)
    headers = {'Accept':'application/json', 'username':username, 'password': password}
    print headers
    payload = {'ids':IDs,'idOperation':IDOperacion, 'idInterval':IDInterval, 'initTime':initTime, 'endTime': endTime}
    print "Payload:", payload
    print "Direccion:", direccion

    data = requests.get(direccion, headers=headers, params=payload)
    print (data.url)
    print (data.content)
    parsed = loads(data.content)
    codebox("Get Data for user:"+username, "GetData Response", dumps(parsed, indent=4, sort_keys=True))
    return

# ------------------------------------------------------------------------
def restGetDailyIrrigationData(direccion,user,token,identificador,initTime,endTime):
    username, password = increaseToken(user, token)
    headers = {'Accept':'application/json', 'username':username, 'password': password}
    print headers
    payload = {'ids':identificador, 'initTime':initTime, 'endTime': endTime}
    print payload
    data = requests.get(direccion, headers=headers, params=payload)
    print (data.url)
    parsed = loads(data.content)
    codebox("Get Daily Irrigation Data for user:"+username, "Get Daily Irrigation Data", dumps(parsed, indent=4, sort_keys=True))
    return

# ------------------------------------------------------------------------
def restSaveSubscription(direccion, user, token, queryParameters, period, expirationTime, channelParams):
    username, password = increaseToken(user, token)
    headers = {'Accept':'application/json', 'username':username, 'password': password}
    print headers
    payload = {'queryParameters':queryParameters, 'period':period, 'expirationTime': expirationTime,'channelParams': channelParams}
    print payload
    data = requests.get(direccion, headers=headers, params=payload)
    print (data.url)
    parsed = loads(data.content)
    codebox("Get Save Subscription for user:"+username, "Get Daily Irrigation Data", dumps(parsed, indent=4, sort_keys=True))
    return


# ------------------------------------------------------------------------
def restDeleteSubscription(direccion, user, token, id):
    username, password = increaseToken(user, token)
    headers = {'Accept':'application/json', 'username':username, 'password': password}
    print headers
    payload = {'subscriptionId':id}
    print payload
    data = requests.get(direccion, headers=headers, params=payload)
    print (data.url)
    parsed = loads(data.content)
    codebox("Delete Subscription for user:"+username, "Delete Subscription", dumps(parsed, indent=4, sort_keys=True))
    return


# ------------------------------------------------------------------------
def restGetFarms(direccion, user, token):
    username, password = increaseToken(user, token)
    headers = {'Accept': 'application/json', 'username': username, 'password': password}
    print headers
    data = requests.get(direccion, headers=headers)
    print (data.url)
    parsed = loads(data.content)
    codebox("Farms for :" + username, "getFarms Response", dumps(parsed, indent=4, sort_keys=True))
    return


# ------------------------------------------------------------------------
def restScheduledIrrigations(direccion, user, token, initTime, endTime, sectorIds, Operacion):
    username, password = increaseToken(user, token)
    headers = {'Accept': 'application/json', 'username': username, 'password': password}
    print headers
    payload = {'initTime': initTime , 'endTime': endTime, 'sectorIds': sectorIds}
    print "Payload:", payload

    if (Operacion == "READ"):
        data = requests.get(direccion, headers=headers, params=payload)

    if (Operacion == "CREATE"):
        data = requests.post(direccion, headers=headers, params=payload)


    if (Operacion == "UPDATE"):
        data = requests.put(direccion, headers=headers, params=payload)


    if (Operacion == "DELETE"):
        data = requests.delete(direccion, headers=headers, params=payload)

    print (data.url)
    parsed = loads(data.content)
    codebox("Programmed Irrigations for :" + username, "get ScheduledIrrigations Response", dumps(parsed, indent=4, sort_keys=True))
    return



