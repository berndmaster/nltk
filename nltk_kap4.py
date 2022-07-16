import string
import nltk, re, pprint
from nltk import word_tokenize
import random

#0. Zugriff auf Werte von FreqDist:

# fdist = nltk.FreqDist(text)
# for wort in fdist:
#     print(wort + ':', fdist[wort], end='; ') #aufpassen mit "+ und ","


#1. Variablen assignment

#A. Assignment always copies the value of an expression 
#siehe Ausgabe "bernhard" von text2

# text1 = "Bernhard"
# text2 = text1
# text1 = "Barbara"
# print(text2) = "Bernhard"

#B. the "value" of a structured object 
# such as a list is actually just a reference to the object.

#C. Kopien einer Liste enthalten alle die gleichen Werte

# empty = ["2"]
# nested = [empty, empty, empty]
# print(nested)
# nested[1].append('Python')
# print(nested)

#D. difference between modifying an object via an object reference, 
# and overwriting an object reference

# nested = [[]]*3
# print(nested)
# nested[1].append("hi")
# nested[2].append("hallo")
# nested[0] = ["wurst"]
# print(nested)
# print(id(nested[0]))
# print(id(nested[1]))
# print(id(nested[2]))

# E. wenn werte neu zugewiesen werden, haben sie eine andere object-ID

# size = 5
# python = ['Python']
# snake_nest = [python] * size
# position = random.choice(range(size))
# snake_nest[position] = ["Python"]
# print(snake_nest)
# print([id(snake) for snake in snake_nest])


#2. Zweifache Zuordnung von Variablen in einer zeile
# z. B. training_data, test_data = text[:cut], text[cut:]


#3. Tuple (Paare von zwei oder mehr Werten)

# tuple1 = "peter", 2 #ohne klammer
# tuple2 = ("peter", 1, "wurst") #mit klammer

# words = ['I', 'turned', 'off', 'the', 'spectroroute']
# tags = ['noun', 'verb', 'prep', 'det', 'noun']
# print(tags[:2]) # bis wert 2 
# print(tags[2:]) # ab wert 2
# print(list(zip(words, tags))) #tupleliste, die über "zip" zwei listen zusammenfügt

#umwandlung datentypen

# a = "hallo, wie gehts".split() -> string in liste
# b = " ".join(tags) -> liste in string
# (list(tuple1)) -> tuple in liste 
# (tuple(words)) -> liste in tuple


# 4. Listen vs. Tupel

# A list is typically a sequence of objects all having the same type, of arbitrary length. mutable, z. B. Wortlisten
# In contrast, a tuple is typically a collection of objects of different types, of fixed length. non mutable, z. B. Wort und Frequenz, Wort und Worttyp

# listen und dicctionaries können über assignments statements geändert werden, z. B.:
# x = [a, b, c], x[1] = d, x = [a, d, c]

# tupel, strings, nummern etc können nicht über assignment statements geändert werden


# 3 werte in einem tuple in einer liste

# words = 'I turned off the spectroroute and I was not sure'.split() #string in liste
# wordlens = [(len(word), word) for word in words] #list comprehension, die aus liste mit tupeln besteht
# wordlens = " ".join(w for (_,w) in wordlens) #wiederzusammenfügen, "_" bedeutet nur zweiten wert
# print(wordlens)


#5. Procedural vs Declarative Style

#prozedural ("durchschnittliche wortlänge")

    #tokens = nltk.corpus.brown.words(categories='news')
    #count = 0
    #total = 0
    #for token in tokens:
    #    count += 1
    #    total += len(token)
    # total / count

#declarative:

# gesamtlänge = sum(len(t) for t in tokens)
# print(gesamtlänge / len(tokens))

# maxlen = max(len(word) for word in text)
# p = [word for word in text if len(word) == maxlen]


# im deklarativen stil mehrdimensionale strukturen bauen:

m, n = 3, 7
array = [[set() for i in range(n)] for j in range(m)] #baue ein array mit 3 spalten und 7 reihen
array[2][5].add('Alice') #füge array an stelle 2, 5 "alice" hinzu
pprint.pprint(array)

# sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
# bigrams = list(nltk.ngrams(sent,4))
# print(bigrams)

#6. Funktionen

# funktionen = building blocks
# funktionen können mit oder ohne argumente funktionieren
# in funktionieren definierte variablen funktionieren in nur innerhalb der funktionen 
# werden variablen außerhalb von funktionen definiert, nennt man sie "globale variablen"
# das RETURN statement legt fest, welcher wert von der funktion zurückgegeben wird 

# Beispiel "hole mir text von seite und normalisiere ihn"

# import re
# def get_text(file):
#     """Read text from a file, normalizing whitespace and stripping HTML markup.""" -> sogenannter docstring
#     text = open(file).read()
#     text = re.sub(r'<.*?>', ' ', text)
#     text = re.sub('\s+', ' ', text)
#     return text

# Beispiel "gib mir die häufigsten wörter von einer website aus"

# from urllib import request
# from bs4 import BeautifulSoup

# def freq_words(url, n):
#     html = request.urlopen(url).read().decode('utf8')
#     text = BeautifulSoup(html, 'html.parser').get_text()
#     freqdist = nltk.FreqDist(word.lower() for word in word_tokenize(text))
#     return [word for (word, _) in fd.most_common(n)]

# sent = "Das ist ein exemplarischer Text mit ein paar Buchstaben, Wörtern und Zahlen. Es ist unklar, was mit diesem Text passiert ist"
# sent = sent.split()
# freqdist = nltk.FreqDist(word.lower() for word in sent)
# sent1 = [word for (word, _) in freqdist.most_common(5)]
# print(sent1)

# def tag(word):
#     assert isinstance(word, string) #soll checken, ob string ... geht aber nicht 
#     if word in ['a', 'the', 'all']:
#         return 'det'
#     else:
#         return 'noun'
# tag("the")

# Higher Order Functions

# filter()
# map()

# Namend Arguments: Argumente von Funktionen können optionaö sein, ausgeschrieben werden, explizit angegeben werden ... etc.

# def freq_words(file, min=1, num=10):
    # text = open(file).read()
    # tokens = word_tokenize(text)
    # freqdist = nltk.FreqDist(t for t in tokens if len(t) >= min)
    # return freqdist.most_common(num)

# Aufruf über z.b. 
# fw = freq_words('ch01.rst', 4, 10)
# fw = freq_words('ch01.rst', min=4, num=10)
# fw = freq_words('ch01.rst', num=10, min=4)

# Rekursive Funktionen
# schwierige sache. platt ausgedrückt: rekursive funktionen sind in sich selbst eingebettet und rufen sich auf

#Lambda Funktionen
#lambda kann genutzt werden, um funktionen "on the fly" zu erstellen, also ohne "def ..." etc
#Beispiel: print((lampda x: x + x)("Haus))