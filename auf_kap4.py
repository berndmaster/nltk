import nltk
from nltk.corpus import stopwords
import re, pprint
from copy import deepcopy


#Identify three operations that can be performed on both tuples and lists. 
#Identify three list operations that cannot be performed on tuples. 
#Name a context where using a list instead of a tuple generates a Python error.

# tuple2 = ("peter", 1, "wurst")
# words = ['I', 'turned', 'off', 'the', 'spectroroute']
# words = tuple(words)
# words = list(words)
# print(words)

# tuple1 = "a",
# print(tuple1)
# print(type(tuple1))


#Create a list words = ['is', 'NLP', 'fun', '?'] . Use a series of assignment statements 
# (e.g. words[1] = words[2] ) and a temporary variable tmp to transform this list 
# into the list ['NLP', 'is', 'fun', '!'] . Now do same transformation using tuple assignment.

#words = ['is', 'NLP', 'fun', '?'] #reihenfolge der items in liste ändern
# words = [words[1], words[0], words[2], words[3]]
# words[0], words[1] = words[1], words[0]
# words[3] = "!"

# words = tuple(words) #reihenfolge der items in tuple ändern
# words = words[1], words[0], words[2], "!"
# print(words)


# ☼ Does the method for creating a sliding window of n-grams behave correctly 
# for the two limiting cases: n = 1, and n = len(sent)?

# words = ['I', 'turned', 'off', 'the', 'spectroroute', 'and', 'the', 'computer', 'started', 'to', 'work','.']
# print(list(nltk.ngrams(words,1)))
# print(list(nltk.ngrams(words,len(words))))
# n = 1
# print([words[i:i+n] for i in range(len(words)-n+1)])
# n = len(words)
# print([words[i:i+n] for i in range(len(words)-n+1)])


# Use the inequality operators to compare strings, e.g. 'Monty' < 'Python' . 
# What happens when you do 'Z' < 'a' ? Try pairs of strings which have a common prefix, e.g. 'Monty' < 'Montague' . 
# Read up on "lexicographical sort" in order to understand what is going on here. 
# Try comparing structured objects, e.g. ('Monty', 1) < ('Monty', 2) . Does this behave as expected?

# vergleiche basieren auf asciII-werten
# kleine buchstaben haben einen höheren wert als große, z.B. z' < 'A' = true 


#Write code that removes whitespace at the beginning and end of a string, 
# and normalizes whitespace between words to be a single space character.
# do this task using split() and join()
# do this task using regular expression substitutions

#variante1

#words = " I turned   off the   spectroroute and the   computer started  to work "
# words = words.split()
# words = " ".join(words)
# print(words)

#variante2

# text4 = re.sub(r'(\s+)', ' ', words) #kein mehrfacher whitespace zwischen wörtern
# text5 = re.sub(r'^\s|\s$', '', text4)  #kein whitespace am satzanfang oder ende
# print(text5) 

#variante3
# pattern1 = re.compile(r'\s+') #regEx-pattern aufstellen
# text1 = pattern1.sub(' ', words) #text nach pattern durchsuchen und mit element "8" substituieren
# pattern2 = re.compile(r'^\s|\s$')
# text2 = pattern2.sub("", text1)
# print(text2)

#☼ Write a program to sort words by length. 
# Define a helper function cmp_len which uses the cmp comparison function on word lengths.

# words = ['I', 'turned', 'off', 'the', 'spectroroute', 'and', 'the', 'computer', 'started', 'to', 'work','.']
# print(sorted((len(w), w) for w in words if w.isalpha()))
# print(sorted(words, key=len))


# Create a list of words and store it in a variable sent1. 
# Now assign sent2 = sent1. Modify one of the items in sent1 and verify that sent2 has changed.

# sent1 = ['I', 'turned', 'off', 'the', 'spectroroute', 'and', 'the', 'computer', 'started', 'to', 'work','.']
# sent2 = sent1
# sent1[0] = "You"
# print(sent2)

#Now try the same exercise but instead assign sent2 = sent1[:]. 
# Modify sent1 again and see what happens to sent2. Explain.

# sent1 = ['I', 'turned', 'off', 'the', 'spectroroute', 'and', 'the', 'computer', 'started', 'to', 'work','.']
# sent2 = sent1[:] #kopie wird erstellt aller werte, sent2 somit unabhängig von sent1 
# sent1[0] = "You"
# print(sent2)

# Now define text1 to be a list of lists of strings (e.g. to represent a text consisting of multiple sentences. 
# Now assign text2 = text1[:] , assign a new value to one of the words, e.g. text1[1][1] = 'Monty' . 
# Check what this did to text2 . Explain.

# text1 = [['I', 'turned', 'off', 'the', 'spectroroute'], ['and', 'the', 'computer', 'started', 'to', 'work','.']]
# text2 = text1[:]
# text1[0][1] = "switched"
# print(text2) #listen in listen sind objekte, weswegen referenz mitkopiert wird und änderungen beide listen betreffen

# text1 = [['I', 'turned', 'off', 'the', 'spectroroute'], ['and', 'the', 'computer', 'started', 'to', 'work','.']]
# text2 = deepcopy(text1) # deepcopy kopiert referenz nicht mit, text2 ist somit eigenständig und wird nicht geändert, wenn text1 geändert wird
# text1[0][1] = "switched"
# print(text2) 
# print(text1)


# Initialize an n-by-m list of lists of empty strings using list multiplication, e.g. word_table = [[''] * n] * m. 
# What happens when you set one of its values, e.g. word_table[1][2] = "hello"? Explain why this happens. 
# Now write an expression using range() to construct a list of lists, and show that it does not have this problem.

# n = 4
# m = 5
# word_table = [[''] * n] * m
# word_table[1][2] = "hello"
# print(word_table) # multiplikation kopiert alle werte

# m, n = 4, 5
# array = [[" " for i in range(n)] for j in range(m)] #baue ein array mit 3 spalten und 7 reihen
# array[1][2] = "hello" #füge an stelle 1,2 hinzu
# pprint.pprint(array)


#13. Write code to initialize a two-dimensional array of sets called word_vowels 
# and process a list of words, adding each word to word_vowels[l][v] 
# where l is the length of the word and v is the number of vowels it contains.

# sent1 = ['I', 'turned', 'off', 'the', 'spectroroute', 'and', 'the', 'computer', 'started', 'to', 'work','.']
# sent1 = [w.lower() for w in sent1] #kleiner machen, um auch großgeschriebene vokale zu finden
# vokale = [(w, len(w), len(re.findall(r'[aeiou]', w))) for w in sent1] #gibt aus wort, wortlänge und anzahl vokale
# print(vokale)

# -> kein array ...


# Write a function novel10(text) that prints any word that appeared in the last 10% 
# of a text that had not been encountered earlier.

# def novel10(text):
#     teil1 = round(len(text) / 100 * 90)
#     vocab1 = set(text[:teil1])
#     vocab2 = set(text[teil1:])
#     neu = []
#     for w in vocab2:
#         if w not in vocab1:
#             neu.append(w)
#     print(neu)


# Write a program that takes a sentence expressed as a single string, splits it and counts up the words. 
# Get it to print out each word and the word's frequency, one per line, in alphabetical order.

#text = "Deutschland erhält ab Montag wohl deutlich weniger russisches Gas. Trotz Debatten über ein Embargo ist Russland noch immer einer der wichtigsten \n Erdgaslieferanten Deutschlands. Doch der Netzagentur-Chef Müller warnt nun: Im Sommer werden diese Gasflüsse wohl zeitweise \n zu einem großen Teil versiegen. Die Erdgaslieferungen aus Russland nach Deutschland und Westeuropa werden im Sommer wohl drastisch \n sinken. Dies gab der Chef der Bundesnetzagentur, Klaus Müller, am Montag bekannt."

# def count (sent1):
#     sent1 = sent1.split()
#     sent1 = sorted(sent1)
#     print(len(sent1))
#     fd = nltk.FreqDist(sent1)
#     for w in sorted(set(sent1)):
#         print(w, fd[w])

# count(text)


#gemania-aufgabe

# wort = "hallo"
# letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
# 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
# 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}

# hidden = 0

# for char in wort:
#     if char in letter_vals:
#         hidden += letter_vals[char]
# print(hidden)


#. Write a function shorten(text, n) to process a text, 
# omitting the n most frequently occurring words of the text. 
# How readable is it?

# text = "Deutschland erhält ab Montag wohl deutlich weniger russisches Gas. Trotz Debatten über ein Embargo ist Russland noch immer einer der wichtigsten \n Erdgaslieferanten Deutschlands. Doch der Netzagentur-Chef Müller warnt nun: Im Sommer werden diese Gasflüsse wohl zeitweise \n zu einem großen Teil versiegen. Die Erdgaslieferungen aus Russland nach Deutschland und Westeuropa werden im Sommer wohl drastisch \n sinken. Dies gab der Chef der Bundesnetzagentur, Klaus Müller, am Montag bekannt."    

# def shorten(text, n):
#     text = text.split()
#     fd = nltk.FreqDist(text)
#     freq = fd.most_common(n)
#     freq_neu = [w for (w, _) in freq] #in liste sollen nur hochfrequente wörter und nicht werte stehen
#     neutext = [] #neue liste
#     for w in text: # eingangstext durchgehen
#         if w not in freq_neu: #wenn worte nicht in hochfrequenten worten
#             neutext.append(w) #in neuen text anhängen
#     print(neutext)

# shorten(text, 5)


# Write a function that takes a list of words (containing duplicates) and 
# returns a list of words (with no duplicates) sorted by decreasing frequency. 
# E.g. if the input list contained 10 instances of the word table and 9 instances of the word chair, 
# then table would appear before chair in the output list.

# text = "Deutschland erhält ab Montag wohl deutlich weniger russisches Gas. Trotz Debatten über ein Embargo ist Russland noch immer einer der wichtigsten \n Erdgaslieferanten Deutschlands. Doch der Netzagentur-Chef Müller warnt nun: Im Sommer werden diese Gasflüsse wohl zeitweise \n zu einem großen Teil versiegen. Die Erdgaslieferungen aus Russland nach Deutschland und Westeuropa werden im Sommer wohl drastisch \n sinken. Dies gab der Chef der Bundesnetzagentur, Klaus Müller, am Montag bekannt."    
# words = ['this', 'is', 'my', 'list', 'of', 'list', 'of', 'list', 'is', 'this', 'of', 'list', 'of', 'list', 'of', 'list', 'of', 'list', 'of', 'words']
# words = " ".join(words)

# def dec_freq(text):
#     text = text.split()
#     fd = nltk.FreqDist(text)
#     liste = [(w, fd[w]) for w in fd]
#     print(liste)

# dec_freq(words)


# Write a function that takes a text and a vocabulary as its arguments and returns the set of words that 
# appear in the text but not in the vocabulary. Both arguments can be represented as lists of strings. 
# Can you do this in a single line, using set.difference()?

# def diff(text, vocab):
#     return set(text).difference(vocab)

# text = "Deutschland erhält ab Montag wohl deutlich weniger russisches Gas. Trotz Debatten über ein Embargo ist Russland noch immer einer der wichtigsten \n Erdgaslieferanten Deutschlands. Doch der Netzagentur-Chef Müller warnt nun: Im Sommer werden diese Gasflüsse wohl zeitweise \n zu einem großen Teil versiegen. Die Erdgaslieferungen aus Russland nach Deutschland und Westeuropa werden im Sommer wohl drastisch \n sinken. Dies gab der Chef der Bundesnetzagentur, Klaus Müller, am Montag bekannt."    
# text = text.split()
# text = set(text)
# vocab = "Alle Brücken nach Sjewjerodonezk zerstört, Selenskyj verspricht Rückeroberung der Krim – das geschah in der Nacht. Das ostukrainische Sjewjerodonezk ist weitgehend von der Außenwelt abgeschnitten. Prorussische Separatisten berichten von Beschuss auf Donezk. Und: Die Ukraine hat ein Viertel ihrer Aussaatfläche verloren. Die seit Wochen umkämpfte Stadt Sjewjerodonezk im Osten der Ukraine ist nach der Zerstörung der dritten und letzten Brücke über den Fluss Siwerskyj Donez nahezu vollständig von russischen Truppen eingekreist. Es ist jetzt leider völlig unmöglich, in die Stadt zu fahren oder etwas in die Stadt zu liefern, sagte Gouverneur Serhiy Gaidai am Montag. Eine Evakuierung ist unmöglich.« Nur das ukrainische Militär habe noch einen begrenzten Zugang zur Stadt."
# vocab = vocab.split()
# vocab = set(vocab)

# print(text.difference(vocab)) #->v1

# text_new = [] #->v2
# for w in text:
#     if w not in vocab:
#         text_new.append(w)
# print(text_new)


#Import the itemgetter() function from the operator module in Python's standard library 
# (i.e. from operator import itemgetter ). Create a list words containing several words. 
# Now try calling: sorted(words, key=itemgetter(1)) , 
# and sorted(words, key=itemgetter(-1)) . Explain what itemgetter() is doing.

# import operator
# from operator import itemgetter

# text = "Deutschland erhält ab Montag wohl deutlich weniger russisches Gas."
# text = text.split()
# print(sorted(text, key=itemgetter(1)))
# g = operator.itemgetter(-1)(text)
# print(g)
# print(type(g))

#itemgetter kann elemente aus liste herausnehmen und gibt sie dann in form von tuple wieder


#◑ Write a recursive function lookup(trie, key) that looks up a key in a trie, 
# and returns the value it finds. Extend the function to return a word 
# when it is uniquely determined by its prefix 
# (e.g. vanguard is the only word that starts with vang-, 
# so lookup(trie, 'vang') should return the same thing as lookup(trie, 'vanguard')).

# import pdb

# def factorial1(n):        # 3
#     result = 1            #
#     for i in range(n):    # 1, 2, 3
#         result *= (i+1)   # bei i=0, result = 1, bei i=1, result = 2 (1*2), bei i=3, result = 6 (1*2*3), bei i=4, result = 24 (6*4)
#                           # wenn Range = z.b. 4, geht "for i ..." nur bis 0, 1, 2, 3 
#     print(result)


# Develop a simple extractive summarization tool, that prints the sentences of a document which contain the highest total word frequency. 
# Use FreqDist() to count word frequencies, and use sum to sum the frequencies of the words in each sentence. 
# Rank the sentences according to their score. Finally, print the n highest-scoring sentences in document order. 
# Carefully review the design of your program, 
# especially your approach to this double sorting. Make sure the program is written as clearly as possible.

#1. meine Version: klappte ok, aber nicht ganz!

# file = open("pforten.txt") 
# raw = file.read()

# sents = nltk.sent_tokenize(raw)
# sents =[s.lower() for s in sents]

# wörter = nltk.word_tokenize(raw)
# rausdamit = stopwords.words('german') # stopwords
# words = [w.lower() for w in wörter] 

# fd = nltk.FreqDist(words)
# häufige_wörter = fd.most_common()

# scorewörter = []
# for x,y in häufige_wörter: #liste der wörter erstellen, die mindestens 2 mal vorkommen, alphanumerisch sind und kein stopword sind
#     if y >= 2 and x.isalpha() and x not in rausdamit:
#         scorewörter.append(x)

# scoring = {}

# sents[0] = sents[0].split()
# score0 = 0
# for w in sents[0]:
#     if w in scorewörter:
#         score0 = score0 + 1
# scoring.update(Satz_0=score0)

# sents[5] = sents[5].split()
# score5 = 0
# for w in sents[5]:
#     if w in scorewörter:
#         score5 = score5 + 1
# scoring.update(Satz_5=score5)

# sents[8] = sents[8].split()
# score8 = 0
# for w in sents[8]:
#     if w in scorewörter:
#         score8 = score8 + 1
# scoring.update(Satz_8=score8)

# print(scoring)
# print(max(scoring))

# jeden satz splitten
# jeden satz durchgehen
# jedes wort von satz durchgehen
# pro häufiges wort +1 im score
# score für jeden satz speichern, in neuer liste?
# ergebnis von score in liste speichern, zusammen mit z.b. "satz1: "

# score = 0
# scoring = []
# for s in sents:
#     s = s.split()
#     print(s)
#     for w in s:
#         if w in scorewörter:
#             score = score + 1
# scoring.append(score)

#2. andere version: ähnlich meiner, aber besser!

file = open("pforten.txt") 
raw = file.read()

sents = nltk.sent_tokenize(raw)
sents =[s.lower() for s in sents]
rausdamit = stopwords.words('german') # stopwords

wörter = nltk.word_tokenize(raw)
words = [w.lower() for w in wörter if w.isalpha() and w not in rausdamit] 

fd = nltk.FreqDist(words) 
häufige_wörter = dict(fd.most_common()) 
# meine variante: wort + absolutes auftreten, z.b. johnny, 6
# andere variante: wort + gewichtetes auftreten, z.b. buch, 0.5
# -> auftreten des worts geteilt durch auftreten des häufigsten worts
# andere variante: auftreten des worts geteilt durch gesamtzahl worte 

sentence_value = {} #leeres dicctionary

for s in sents: #alle sätze durchgehen
    for word, freq in häufige_wörter.items(): #alle wörter und auftreten
        if word in s: #wenn word in satz vorkommt
            if s in sentence_value: #satz einfügen in dicctionary
                sentence_value[s] += freq #wenn satz vorhanden: addiere key: satz und value: wortfreqenz
            else: 
               sentence_value[s] = freq #wenn satz nicht vorhanden, füge satz mit frequenz hinzu

sumValues = 0 #durchschnittlichen häufigkeitswert ausrechnen: werte aller sätze zusammenrechnen geteilt durch anzahl werte
for s in sentence_value:
    sumValues += sentence_value[s] #833
average = sumValues / len(sentence_value)

hochfrequent = [s for s in sentence_value if sentence_value[s] >= average] 
# zusammenfassung = alle sätze mit einem häufigkeitswert über dem durchschnitt
print(hochfrequent)