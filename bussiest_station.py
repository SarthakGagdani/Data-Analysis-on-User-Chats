#imports
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

#read chatdata file  
df = pd.read_csv('chats.csv')
df['index_col'] = df.index


# Keywords for stations on Route
stations = ['cst','masjid','sandhurst road','byculla','chinchpokli',
'currey road','parel','dadar','matunga','sion','kurla','vidyavihar',
'ghatkopar','vikroli','kanjur marg','mulund','thane','mumbra','dombivli'
,'kalyan','ulhas nagar','ambernath','badlapur','karjat','titwala']

#returns most common user of the chat box.
def get_common_user(df):
    return df['Username'].value_counts()[0:5]

def most_discussed_station(df):
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
    res_count = Counter(all_stations)
    return all_stations

#plots barchart of bussiest station in mumbai central line
def plotBar(all_stations):
    labels, values = zip(*Counter(all_stations).items())
    
    indexes = np.arange(len(labels))
    width = 0.3

    plt.title('Popular Stations Chart')
    plt.bar(indexes, values, width)
    plt.xticks(indexes+width*0.5, labels)
    plt.show()


print('Top 5 Most Active Users:')
print(get_common_user(df))

all_stations = most_discussed_station(df)
plotBar(all_stations)




