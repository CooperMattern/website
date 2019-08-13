#!/usr/bin/env python
# coding: utf-8

# In[3]:

import numpy as np
from yattag import Doc
from bs4 import BeautifulSoup as bs
import pickle


def createtable():
    #loads in latest flight data file
    f = open('/var/www/coopermattern.com/data/planes.pkl','rb')
    planes = pickle.load(f)
    f.close()
    
    #gets the current headers that will be used
    headerTable = ['line']
    headerTable.extend(list(planes[list(planes)[0]]))
    headerTable.append('link')
    
    #start writing hmtl
    doc, tag, text = Doc().tagtext()
    with tag('table'):
        with tag('tr'):
            for header in headerTable:
                with tag('th'):
                    text(header)
        #iterate through a sorted list of planes           
        for line in sorted(planes.keys()):
            with tag('tr'):
                with tag('td'):
                    text(line)
                    
                #use the ordered list of headers to place data in the correct cells
                for key in list(planes[list(planes)[0]]):
                    with tag('td'):
                        text(str(planes[line][key]))
                with tag('td'):
                    if planes[line]['ident']!='NaN':
                        with tag('a', href='https://flightaware.com/live/flight/'+planes[line]['ident']):
                            text('flight')
                    else:
                        text('No flight avaliable')

    return(bs(doc.getvalue(),'html.parser').prettify())