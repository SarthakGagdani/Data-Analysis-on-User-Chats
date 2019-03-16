# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 00:12:58 2018

@author: Sarthak
"""

from datetime import datetime
import pandas as pd
from datetime import timedelta, datetime

#loads chat dataset
df = pd.read_csv('chats.csv')
#Adding index column
df['index_col']=df.index

#the probable keywords related to train delay
keywords_emergency=['accident','derailed','late','delayed','cancelled','halt','halted',
                    'megablock','delay','rush','traffic','chaos','fire','attack','stampade',
                    'rain','water','blast']

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

#removing spam chats keeping relevant that matches with keywords
for i in range(len(df['UID'])):
    msg = df['Message'][i]
    eid=df['index_col'][i]
    if not words_in_string(keywords_emergency, msg.lower()):
        df = df.drop(df[df['index_col']==eid].index)
        

#splits dataset into time interval of 30 minutes and stores in DF_list      
start_date = datetime(2018, 7, 2, 6, 0, 0)
time=[]
for td in (start_date + timedelta(minutes=30*it) for it in range(36)):
    time.append(td.strftime("%Y-%m-%d %H:%M:%S"))

i=0
DF_list = list()
while i<36:
    DF_list.append(df[(df['IST'] > time[i]) & (df['IST'] < time[(i+1)%36])])
    i+=1

print(DF_list)

    


