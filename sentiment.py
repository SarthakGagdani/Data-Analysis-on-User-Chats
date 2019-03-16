from textblob import TextBlob
import nltk
import enchant
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

engDict = enchant.Dict('en_US')
stopWords = nltk.corpus.stopwords.words('english')

df = pd.read_csv('chats.csv')


def cleanData(df):

    df['Index'] = df.index
    for i in range(len(df)):
        idx = df['Index'][i]
        # print(idx)
        for word in nltk.word_tokenize(df['Message'][i]):
            if engDict.check(word) == False:
                df = df.drop(df[df['Index'] == idx].index)

    df.to_csv('sent_analysis_july.csv', index=False)

#show sentiment in terms of positive,negative and neutral
def sentimentAnalysis(df):

    for i in range(len(df)):
        wiki = TextBlob(df['Message'][i])
        pol = 'neutral'
        if wiki.sentiment.polarity < 0:
            pol = 'negative'
        elif wiki.sentiment.polarity > 0:
            pol = 'positive'

        df['Sentiment'][i] = pol

    df.to_csv('july_sent_analysis.csv', index=False)

def plotPie(df):

    counts = Counter(df['Sentiment'])
    pie = []
    labels = ['Positive\n'+str(counts['positive']),'Neutral\n'+str(counts['neutral']),'Negative\n'+str(counts['negative'])]
    pie.append(counts['positive'])
    pie.append(counts['neutral'])
    pie.append(counts['negative'])
    plt.title('Sentiment Analysis')
    plt.pie(pie, labels=labels, shadow=True)
    plt.show()



plotPie(df)
