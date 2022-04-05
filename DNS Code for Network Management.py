# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:43:05 2022

@author: caina
"""
#Import needed modules
import pandas as pd
import socket
    
#Pandas reads the file and seperates it, global variables are under
x = pd.read_csv("domains.tsv", sep = '\t')['domain']
doc = {}
docHost = {}

for i in range(len(x)): #goes through x, where i is the iterantion number
    temp = [] #resets the temp var after every iteration
    try:
        long = socket.getaddrinfo(str(x[i]),443) #temp var to store the IP
        for b in range(len(long)): #goes through the temp list of IP, b is the iteration number
            temp.append(long[b][4]) #sets the desired IP section to the temperary list
        doc[x[i]] = temp #sets the index of the host name to the value of the IP
        
    except Exception as e:
        #Gives error message for websites that are no longer functioning
        print("\nERROR PRESENT: "+str(e)+'\n')

print(doc)
    
for k in doc: #goes through every key/vlaue of dictionary 'doc'
    try:
        #sets the name of the site to the key and adds the value of the extra bits
        docHost[k] = socket.gethostbyaddr(str(doc[k][0][0]))
        docHost[k] = docHost[k][0] #removes the extra bits, leaves host name
        
    except Exception as e:
        #Gives error message the IPs that do not produce a host name
        print("Error : ", e)

for z in docHost: #goes thorough every key/value in dictionary 'docHost'
    doc[z].append(docHost[z]) #adds the host name from docHost to the matching key of doc

print(doc) #prints the final dictionary of the site name, IP, and host name respectivly. 

