# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:30:19 2018

@author: Sarthak
"""

import pandas as pd
import numpy as np

#reads chat dataset from csv file and searches for the following emergency keywords indicating some missing complaints from users 
df = pd.read_csv('chats.csv')

keywords_emergency=['lost','missing','found','atm','wallet','bag','child','forgot','mobile','phone'
                    ,'iphone','backpack','suitcase','purse','laptop','stolen','steal','cell'
                    ,'keys']

df['index_col']=df.index

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

for i in range(len(df['UID'])):
    msg = df['Message'][i]
    eid=df['index_col'][i]
    if not words_in_string(keywords_emergency, msg.lower()):
        df = df.drop(df[df['index_col']==eid].index)
        
print(df)        
        
    
    
    

