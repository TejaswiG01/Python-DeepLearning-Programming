#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk import word_tokenize,pos_tag, ne_chunk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

nltk.download()
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


# In[20]:


sentence = open('C:/Users/Tejaswi/PycharmProjects/ICP7/input.txt', encoding="utf8").read()

# Tokenization
stokens = nltk.sent_tokenize(sentence)
wtokens = nltk.word_tokenize(sentence)
print("\n Word Tokenization :\n")
print(wtokens)

print("\n Sentence Tokenization :\n")
print(stokens)


# In[3]:


# Parts of Speech
text = nltk.word_tokenize(sentence)
print("POS:\n")
print(nltk.pos_tag(text))


# In[16]:


# Stemming
print("Stremming:\n")
pStemmer = PorterStemmer()
lStemmer = LancasterStemmer()
sStemmer = SnowballStemmer('english')
for t in wtokens:
   print(pStemmer.stem(t), lStemmer.stem(t), sStemmer.stem(t))


# In[17]:


# Lemmatization

print("Lemmatization :\n")
lemmatizer = WordNetLemmatizer()
for t in wtokens:
    print(lemmatizer.lemmatize(t))


# In[18]:


# Named Entity Recognition
print("Named Entity Recognition: \n")
for s in stokens:
    print(ne_chunk(pos_tag(word_tokenize(s))))


# In[19]:


# Trigram
print("Trigram:\n")
for s in stokens:
    token = nltk.word_tokenize(s)
    trigrams = list(ngrams(token, 3))
    print("The text:", s, "\nword_tokenize:", token, "\ntrigrams:", trigrams)

