# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:07:09 2020

@author: anjuchawla_takkar
"""

import pandas as pd
import json
import numpy as np
import time
#(columns=['User_ID', 'UserName', 'Action'])
location_time= pd.DataFrame(columns=["address","Stime","Etime"])
# Thu Apr  2 10:46:19 2020
iter=0
dictnew={}

import numpy as np
file = 'D:\\Anaconda_MLfiles_Anju\\coursera\\GPS\\hotspots.xlsx'
hotspots = pd.read_excel(file)
#print(df)

with open('2020_march.json') as f:
 data = json.load(f)

#from datetime import datetime, timedelta
import datetime


#print(date_from_webkit(1583296815256))
#input("hello")
def recursive_items(dictionary):
    for key, value in dictionary.items():
        
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
            
        else:
            yield (key, value)

for p_id, p_info in data.items():
    #print("\nPerson ID:", p_id)
    #location_time=list()  
    dictnew={}
    index=0
    for newkey in p_info:
      if("placeVisit" in newkey):
        for key, value in recursive_items(newkey):
            if("TimestampMs" in key):
               timestr=int(value[0:10])
               #print (timestr)
               readable = datetime.datetime.fromtimestamp(timestr).isoformat()
               
               if("startTimestampMs" in key):
             
                   
                 #df.loc[dl,'A']='Yes'
                 location_time.loc[index,"Stime"]=readable
               else :
                 location_time.loc[index,"Etime"]=readable
                 index+=1
              #
                #print(key,time.ctime(int(value)))
              #readable = time.ctime(1584701268406)
              #print(readable)
            if("address" in key):
             #print(key,value)
             location_time=location_time.append({'address':value},ignore_index=True)     
             #location_time.extend(value)
             
             
        
        
        #input("HOLD")
        #print("#####################")

        #print("next location") 
found= pd.DataFrame(["Been There"])
for i in hotspots['city'] :
    #print(i)
    found=location_time[location_time["address"].str.contains(i)]

print(found["address"],["Stime"])

print("<content-type:text/html\n>")
print("<html><head><title>Hello from Python</title></head>/html>")

     
    
