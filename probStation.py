import pandas as pd
import nltk
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('chats.csv')

stations = ['cst','masjid','sandhurst road','byculla','chinchpokli','currey road',
'parel','dadar','matunga','sion','kurla','vidyavihar','ghatkopar','vikroli',
'vikhroli','kanjur marg','mulund','thane','mumbra','dombivli','kalyan','ulhas nagar','ambernath','badlapur','karjat','titwala']

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

def cleanData(df):
    keywords_emergency=['delay', 'late']

    for i in range(len(df['UID'])):
        msg = df['Message'][i]
        eid = df['Index'][i]
        if not words_in_string(keywords_emergency, msg.lower()):
            df = df.drop(df[df['Index']==eid].index)

    return df

def most_complained_station(df):
    common_string = ""
    for line in df['Message']:
        for word in nltk.word_tokenize(line):
            if word.lower() in stations:
                if word.lower()=='csmt':
                    common_string+='cst'
                else:
                    common_string+=word.lower()
                common_string+=' '

    all_stations = common_string.split()
    # res_count = Counter(all_stations)
    # return res_count.most_common(5)
    return all_stations

def plotBar(all_stations):
    labels, values = zip(*Counter(all_stations).items())
    
    indexes = np.arange(len(labels))
    width = 0.3

    plt.bar(indexes, values, width)
    plt.xticks(indexes+width*0.5, labels)
    plt.title('Complaints Distribution Chart')
    plt.show()


all_stations = most_complained_station(df)
plotBar(all_stations)

