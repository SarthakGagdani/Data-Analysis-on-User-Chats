# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 08:11:54 2018

@author: Sarthak
"""

import pandas as pd

df = pd.read_csv('chats.csv')
df['index_col']=df.index

stations = ['cst','masjid','sandhurst road','byculla','chinchpokli','currey road','parel',
            'dadar','matunga','sion','kurla','vidyavihar','ghatkopar','vikroli','vikhroli'
            ,'kanjur marg','mulund','thane','mumbra','dombivli'
            ,'kalyan','ulhas nagar','ambernath','badlapur','karjat','titwala']

for i in range(len(df['UID'])):
    msg = df['Message'][i]
    eid=df['index_col'][i]
    res=df['Message'][i].split("(sent from ",1)
    
    if len(res)==1:
        df = df.drop(df[df['index_col']==eid].index)
        
        
df2=pd.DataFrame(columns=['user','station'])
      

for i in df['index_col']:
   df2.loc[i, 'user'] =df['Username'][i]
   
 
   z=df['Message'][i].split("(sent from ")[1]
   y=z.replace(')',"")
   df2.loc[i,'station']=y


#grouping users corresponding to station name
print(df2.groupby('station')['user'].apply(lambda x: "{%s}" % ','.join(x)))


