import sys
from suds import null, WebFault
from suds.client import Client
from urllib.error import HTTPError
from suds.transport import TransportError
import logging
import numpy as np
import pysnooper
import pickle
from collections import OrderedDict

print('START')

#FlightXML Api creation
file = open('/var/www/coopermattern.com/data/apikey')
x = file.read().split("\n")
file.close()
username = x[0]
apiKey = x[1]
url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'

logging.basicConfig(level=logging.INFO)
api = Client(url,username=username, password=apiKey)

planes = np.load('data.npy') #load previously parsed email data

size = np.size(planes,0) 

flightData = {}

i=0
while i < size:
    plane = OrderedDict()
    tail = planes[i][3]
    try:
        result = api.service.FlightInfo(tail,1)
        ident = result['flights'][0]['ident']
        flight = api.service.InFlightInfo(ident)
        plane['tail'] = str(planes[i].tolist()[3])
        plane['ident'] = flight['ident']
        plane['origin'] = api.service.AirportInfo(flight['origin'])['name']
        plane['destination'] = api.service.AirportInfo(flight['destination'])['name']
        plane['speed'] = flight['groundspeed']
        plane['altitude'] = flight['altitude']*100
        plane['latitude'] = flight['latitude']
        plane['longitude'] = flight['longitude']
    except(HTTPError, TransportError, WebFault):
        plane['tail'] = str(planes[i].tolist()[3])
        plane['ident'] = 'NaN'
        plane['origin'] = 'NaN'
        plane['destination'] = 'NaN'
        plane['speed'] = 'NaN'
        plane['altitude'] = 'NaN'
        plane['latitude'] = 'NaN'
        plane['longitude'] = 'NaN'
    finally:
        flightData[str(planes[i].tolist()[0])] = plane
        i+=1
f = open('/var/www/coopermattern.com/data/planes.pkl','wb')
pickle.dump(flightData,f)
f.close()