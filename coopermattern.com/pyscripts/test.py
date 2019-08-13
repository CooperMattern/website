import sys
from suds import null, WebFault
from suds.client import Client
import logging
import numpy as np
import pickle
import pysnooper
from yattag import Doc
from bs4 import BeautifulSoup as bs

# file = open('apikey')
# x = file.read().split("\n")
# file.close()
# username = x[0]
# apiKey = x[1]
# url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'

# logging.basicConfig(level=logging.INFO)
# api = Client(url,username=username, password=apiKey)

# # Get the weather
# result = api.service.Metar('KAUS')
# print(result)

# # Get the flights enroute
# result = api.service.FlightInfo("N128AM",3)
# flights = result['flights']

# print("Aircraft en route to KSMO:")
# for flight in flights:
#     print("%s (%s) \t%s (%s)" % ( flight['ident'], flight['aircrafttype'],
#                                   flight['originName'], flight['origin']))

htmlTable = '<table>'

f = open('planes.pkl','rb')
planes = pickle.load(f)
f.close()
headerTable = ['line']
headerTable.extend(list(planes[list(planes)[0]]))
doc, tag, text = Doc().tagtext()
# for key in sorted(planes.keys()):
#      print('%s: %s' % (key,planes[key]))


for header in headerTable:
    with tag('th'):
        text(header)
for line in sorted(planes.keys()):
    print(line + ' '+ str(planes[line]))
    with tag('tr'):
        with tag('td'):
            text(line)
        for key in list(planes[list(planes)[0]]):
            with tag('td'):
                text(str(planes[line][key]))
                
print(bs(doc.getvalue()).prettify())


# result = api.service.FlightInfo('SPLSE',1)
# ident = result['flights'][0]['ident']
# flight = api.service.InFlightInfo(ident)
# print(flight)

# i=0

# #with pysnooper.snoop():
# while i < planes.size:
#     try:
#         test = planes[i][3]
#         result = api.service.FlightInfo(test,3)
#         flights = result['flights']
#         print(flights)
#     except WebFault:
#         pass
#     i+=1

# print(planes[18][3])
# for p in planes:
#     print(p)
#     while True:
#         try:
#             result = api.service.FlightInfo(p[3],3)
#             flights = result['flights']
#             print(p[0]+'\n'+flights)
#             break
#         except:
#             pass