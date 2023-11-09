import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text= """Samsung was founded by Lee Byung-chul in 1938 as a trading company. 
Over the next three decades, the group diversified into areas including food
 processing, textiles, insurance, securities, and retail. Samsung entered the electronics industry in the late 1960s and the 
 construction and shipbuilding industries in the mid-1970s; these areas would drive its subsequent growth. Following Lee's death in 1987, Samsung was separated into 
 five business groups – Samsung Group, Shinsegae Group, CJ Group and Hansol Group, and JoongAng Group. """



stopwords=list(STOP_WORDS)
#print(stopwords)
nlp=spacy.load('en_core_web_sm')
doc=nlp(text)
#print(doc)
tokens=[token.text for token in doc]
#print (tokens)
word_freq={}
for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text  not in word_freq.keys():
            word_freq[word.text]=1
        else:
            word_freq[word.text]+=1
#print(word_freq)
max_freq