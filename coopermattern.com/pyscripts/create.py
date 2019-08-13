#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sys

fn = sys.argv[0]

def emailparse(filename):

    file = open(filename)
    content = np.array(file.readlines())
    file.close()
    
    index1 = np.argwhere(content == 'Content-Type: text/plain; charset="us-ascii"\n') #get index of start of plain (hehe) text data
    index2 = np.argwhere(content== 'Content-Type: text/html; charset="us-ascii"\n') #get index of end of plain text data
    index = np.append(index1,index2) #combine the two for ease
    data = content[index[0]:index[1]] #make data set of that 
    index = np.argwhere(data == '\n') #indexes of empty new line characters
    data1 = np.delete(data,index)[2:-1] #deletion of new lines and edge triming
    data2 = np.char.strip(data1,'\n') #stripping new line characters from leftover data
    
    #tests the first and last of a group of 6 data points to see if they are ints, we want the first one to be an int but not the second
    #if the last is and int, we insert a NaN and reupdate the list we are working with. the continues on itarating the chunks of the list 
    
    data3 = []
    i=0
    while i < data2.size:
        test = data2[i:i+7]
        try:
            int(test[0])
            try:
                int(test[6])
                data2 = np.insert(data2,i+3,'NaN')
            except:
                pass
            test = data2[i:i+7]
            data3.append(test.tolist())
            i+=7
        except:
            print('this shouldnt ever happen')
    np.save("data",np.array(data3))           
    return(data3)

emailparse(fn)