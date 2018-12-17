# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import AutenticationWiseApi
import RESTWiseApi
from easygui import *

# Oficial SSL API
apiLogin = 'https://api.wiseconn.com/WiseApi/Auth/login'
restURL ="https://api.wiseconn.com/WiseApi"



def main():
    print "Espáñol"
    msg = "Enter logon information"
    title = "WiseAPI Demo"
    logonNames = ["User Email", "Password"]
    logonValues = multpasswordbox(msg, title, logonNames)
    user = logonValues[0]

    while(1):
        clave = AutenticationWiseApi.password(logonValues[1])
        token = AutenticationWiseApi.getToken(apiLogin, logonValues[0], clave)

        msg = "What Method do you like to test?"
        title = "WiseAPI Demo Software"
        choices = ["Get Farms", "Get Summary", "Get Last Data", "Get Data", "Get Daily Irrigation Data","Scheduled Irrigations"]
        choice = choicebox(msg, title, choices)


        if(choice=="Get Summary"):
            RESTWiseApi.restGetSummary(restURL+'/rest/read/summary', user, token)

        if (choice == "Get Last Data"):
            RESTWiseApi.restGetLastData(restURL+'/rest/read/lastData', user, token, enterbox("ID Sensor","ID"))

        if (choice == "Get Data"):
             msg = "Enter the Data information. \nOperation\nAVERAGE = 0 , MAX = 1 , MIN = 2 , SUM = 3 , COUNT = 4\n\nInterval\nHOUR = 0 , DAY = 1 , MONTH = 2"
             title = "Get Data Method"
             fieldNames = ["Sensor ID", "Operation", "Interval", "Init Time", "End Time"]
             fieldValues = multenterbox(msg, title, fieldNames)
             RESTWiseApi.restGetData(restURL+'/rest/read/data', user, token, fieldValues[0],fieldValues[1],fieldValues[2],fieldValues[3],fieldValues[4])

        if (choice == "Get Daily Irrigation Data"):
            msg = "Enter the information."
            title = "Get Daily Irrigation"
            fieldNames = ["Sector ID", "Init Time", "End Time"]
            fieldValues = multenterbox(msg, title, fieldNames)
            RESTWiseApi.restGetDailyIrrigationData(restURL+'/rest/read/dailyIrrigationData', user, token,fieldValues[0],fieldValues[1],fieldValues[2] )

        if (choice == "Get Farms"):
            RESTWiseApi.restGetFarms(restURL+'/rest/read/farm', user, token)

        if (choice == "Scheduled Irrigations"):
            msg = "Enter the information. \n Operations: \n CREATE , UPDATE , DELETE , READ \n Example Sector: 8478"
            title = "New Scheduled Irrigations"
            fieldNames = ["Init Time", "End Time","Sector ID", "Operation"]
            fieldValues = multenterbox(msg, title, fieldNames)
            RESTWiseApi.restScheduledIrrigations(restURL+'/rest/write/scheduledIrrigations', user, token,fieldValues[0],fieldValues[1],fieldValues[2],fieldValues[3] )

        msg = "Do you want to continue?"
        title = "Please Confirm"
        if ccbox(msg, title):     # show a Continue/Cancel dialog
            pass  # user chose Continue
        else:
            sys.exit(0)           # user chose Cancel

main()
