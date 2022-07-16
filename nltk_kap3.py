import nltk, re, pprint
from nltk import word_tokenize
#from nltk.book import *
import unicodedata
import matplotlib
from urllib import request
from bs4 import BeautifulSoup
import random

# 1. Textdatei lesen:

# f = open('Linke.txt')
# raw = f.read()
# tokens = word_tokenize(raw)
# #tokens sind anschließend in einer liste
# stopwords = nltk.corpus.stopwords.words('german')
# text = nltk.Text(tokens)
# words = [w.lower() for w in tokens if w.isalpha() and w not in stopwords]
# vocab = sorted(words)
# fdist3 = FreqDist(vocab)
# #print (fdist3.most_common())

# suche = [w for w in fdist3 if re.search('^alten', w)]
# for w in suche:
#     print(w + ':', fdist3[w])

# print("___________")

#2. von LATIN II oder ASCI II in Unicode (utf8)

# Python läuft in Unicode/UFT8
# # "ä" ist Zeichen aus Latein II
# # Um Unicode eines Symobls zu bekommen, erst die dem Symbol zugeordnete ganze Zahl finden: 
# print(ord("ä"))
# # Dann ganze Zahl in Heximalzahl umwandeln:
# print(hex(228)) # = 0x34, "x" hinter "0" bedeutet, dass "0" doppelt kommt
# ae = "\u00e4" # Unicode von ä ist "\u00e4" 
# print(ae)
# print(ae.encode('utf8'))


# 3. REGULAR EXPRESSIONS

# import re = notwendig für RegEx
# RegEx ermöglichen komplexere Suchanfragen

# 1) nach wörter suchen (re.search) oder 2) nach buchstabenabfolgen (re.findall)

# f = open('Linke.txt')
# raw = f.read()
# tokens = word_tokenize(raw)
# stopwords = nltk.corpus.stopwords.words('german')
# text = nltk.Text(tokens)
# words = [w.lower() for w in tokens if w.isalpha() and w not in stopwords]
# vocab = sorted(words)
# fdist3 = nltk.FreqDist(vocab)
# suche = [w for w in fdist3 if re.search('^alten', w)] #alle wörter, die mit alten anfangen
# for w in suche:
#     print(w + ':', fdist3[w])


# ^ markiert den wortanfang, z. B. (^..j..t..$)
# $ markiert das wortende
# . markiert einen beliebigen buchstaben
# ? markiert vorangehendes zeichen als optional, z. B. (^e-?mail$)
# Buchstaben in [ ] führt zu Suche von einem oder mehreren Buchstabens ('^[ghi][mno][jlk][def]$')
# - sucht von Buchstabe bis Buchstabe ('^[g-o]+$')
# + sucht nach BELIEBIGER Anzahl von vorangehendem Buchstaben ('^[g-o]+$')  
# * zero or more instances of the preceding item
# \m sucht genau das nachfolgende Zeichen, z.b. ein "m"
# {4} Exactly n repeats where n is a non-negative integer, 
# {2,} least n repeats
# {,2} No more than n repeats
# {m,n} At least m and no more than n repeats
# (b|a) entweder b oder a 
# \s = leerzeichen
# \w = alphanumerischer charakter


# RE.SEARCH (findet ganze wörter)

# suche = [w for w in fdist3 if re.search('^alten', w)] #alle wörter, die mit alten anfangen
# for w in suche:
#     print(w + ':', fdist3[w])
# print("_____")

# suche = [w for w in fdist3 if re.search('^[a-z]+mm+[a-z]$', w)] #alle wörter, die mit beliebiger buchstabenanzahl anfangen, dann "mm", dann wieder beliebig
# for w in suche:
#     print(w + ':', fdist3[w])
# print("_____")

# suche = [w for w in fdist3 if re.search('^[^aeiouAEIOU]+$', w)] #alle wörter, die keinen vokal enthalten
# for w in suche:
#     print(w + ':', fdist3[w])

# print("_____")

# suche = [w for w in fdist3 if re.search('^[0-9]{4}$', w)] #vier mal wird nach einer zahl zwischen 0 und 9 gesucht
# for w in suche:
#     print(w + ':', fdist3[w])

# print("_____")

# suche = [w for w in fdist3 if re.search('(end|ig)$', w)] #wortende "end" oder "ig"
# for w in suche:
#     print(w + ':', fdist3[w])

# print("_____")


# RE.FINDALL (findet zeichenabfolgen)

# re.findall (r'[^asd]+, wort)

# finde alle abfolgen, in denen 7 konsonaten aufeinander folgen und extrahiere die gesuchte abfolge

# wsj = sorted(set(vocab))
# fd = nltk.FreqDist(
#     vs for word in wsj
#     for vs in re.findall(r'[^aeiou]{7,}', word))
# print(fd.most_common(10))

# print("_____")

#  extrahiere vokale außer am wortanfang und mache text neu

# regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
# def compress(word):
#      pieces = re.findall(regexp, word)
#      return ''.join(pieces)
# print(nltk.tokenwrap(compress(w) for w in words[1000:1100]))

# -> mir unklar, wie das funktioniert 


# WORD STEMS finden

# p = "Katzen"
# print(p[:-1])
# print(re.findall(r'^(.*?)(n)$', 'Katzen'))

# a = text.findall(r"(<.*>) <Dienst>")
# print(a)

# Aufgabe:
# findall
# Kollokationen links von Wort finden
# Frequenzen von Wort links angeben


# STEMMERS

# porter = nltk.PorterStemmer()
# lancaster = nltk.LancasterStemmer()
# a = [porter.stem(t) for t in tokens]
# print(a)


#ZUSAMMENFASSUNG

#0.Text reinladen und durchsuchbar machen

#f = open('Linke.txt')
#raw = f.read()
#tokens = word_tokenize(raw)
# stopwords = nltk.corpus.stopwords.words('german')
# text = nltk.Text(tokens)
# words = [w.lower() for w in tokens if w.isalpha() and w not in stopwords]
# vocab = sorted(words)

#nltk.tokenize_words vs. split()

# split zerlegt string nach vorliegenden whitespaces oder z.b. punkten, dadurch fallen oft worte mit z.b. satzzeichen zusammen
# tokenize zerlegt nach whitespaces, aber erfasst auch nicht alphanummerische zeichen einzeln, wie z.b. satzzeichen


#1.Textdaten von Website oder TXT reinziehen und bearbeiten

# def regex_text (text, regex, sprache): #txt-datei wird geöffnet und tokeniziert, stopwörter rausgenommen, dann mit beliebiger regex durchsucht
#     f = open(text)
#     raw = f.read()
#     tokens = word_tokenize(raw)
#     stopwords = nltk.corpus.stopwords.words(sprache)
#     text = nltk.Text(tokens)
#     words = [w.lower() for w in tokens if w.isalpha() and w not in stopwords]
#     vocab = sorted(words)
#     fdist3 = nltk.FreqDist(vocab)
#     suche = [w for w in fdist3 if re.search(regex, w)] 
#     for w in suche:
#         print(w + ':', fdist3[w])

# regex_text ('Linke.txt', '^alten', 'german')

#EINFÜGEN von arbeitsrechner: website-funktion


#2. Regular Expressions

#wichtige RegEx siehe oben

# re.findall
# suche = [w for w in fdist3 if re.search('^alten', w)]
# for w in suche:
#     print(w + ':', fdist3[w])

# re.search (a.suchmuster, textquelle) 
# text = ("we don't see quotation characters. I don't like school. You don't mean that.")
# re.findall(r"do|n't|\w+", text)

# re.sub (a.suchmuster, b.ersetzung, c.textquelle)
# z. B. ohne_html = re.sub(r'<[^>]+>', '', html)
#z.B. nouns_new = re.sub(r'(\w+)an', r'\1a', adjectives)


#3.Sachen in TXT schreiben: 

#output_file = open('output.txt', 'w') #"w" ist notwenig, um "word"-input zu markieren
#words = set(nltk.corpus.genesis.words('english-kjv.txt'))
#   for word in sorted(words):
#       print(word, file=output_file)


#4.Listen und Strings

#split(): string wird so zur liste

# silly = "newly formed bland ideas are inexpressible in an infuriating way"
# bland = silly.split()


#join(): liste wird so zum string:

# adjectives = ["Zelandian", "African", "Asian", "Australian", "Canadian"]
# adjectives = " ".join(adjectives)
# print(adjectives)


# Append: Elemente in Listen einfügen

# saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
# length = []
# for w in saying:
#     length.append(len(w))


# 5. FILES schreiben

# #FILE öffnen

# file = open("pythonforling.txt") #Achtung: manchmal muss man hier noch encoding='uft8' angeben
# raw = file.read()
# tokens = nltk.word_tokenize(raw)
# print(raw)

# #FILE schreiben

# file = open("pythonforling.txt", "w") # "w" für "write", "r" für "read"
# file.write("das ist text! \n")
# file.write("noch mehr text ...")
# file.close()

# Liste in File schreiben

# file = open("resultate.txt", "w") # "w" für "write"
# for (x, y) in fd.most_common(50):
#     file.write ("%s: " % x )
#     file.write ("%s\n" % y )

# importieren von eigenen modulen
# z. B. # from dec_freq import dec_freq 