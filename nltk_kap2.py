#EIGENES CORPUS

#vor jedes eigene corpus setzen: ACHTUNG "import *" ist notwendig für manche Funktionen
from multiprocessing.sharedctypes import Value
import nltk
from nltk.book import *
import random

from regex import D
# from nltk.corpus import PlaintextCorpusReader
# corpus_root = r"C:\Python\Scripts"
# a = PlaintextCorpusReader(corpus_root, 'corpus.txt')

#LÄNGSTEN SATZ IM KORPUS BESTIMMEN
# b = a.sents('corpus.txt')
# longest_len = max(len(s) for s in b)
# d = [s for s in b if len(s) == longest_len]
# print(d)

#immer corpusname punkt words/sents/raw und beide klammern nutzen

# print(a.fileids())
#print(sorted(set(a.words())))
#print(len(a.sents()))
#print(wordlists.words()[0:20])
# print(a.words().count("die"))
# print(a.sents()[15:30])

# FREQUENZVERTEILUNG

# fdist3 = FreqDist(a.words())
# print(fdist3.most_common(20))

# WÖRTER MIT LÄNGE 10 SUCHEN

# types_text3 = set(a.words())
# long_types = [wort for wort in a.words() if len(wort) == 10]
# print(sorted(long_types))

# WÖRTER MIT LÄNGE ÜBER 3 UND FREQUENZ über 7

# print(sorted(w for w in set(a.words()) if len(w) > 3 and fdist3[w] > 7))

# HÄUFIGSTE WORTLÄNGEN BERECHNEN

# fdist4 = FreqDist(len(w) for w in a.words())
# print(fdist4)
# print(fdist4.most_common())

# VOKABULAR UND NACH BESTIMMTEN WORTEN SUCHEN

# print(sorted(set(w for w in a.words() if "lich" in w)))
# print(len(set(w for w in a.words() if "lich" in w)))

# print(sorted(set(w for w in a.words() if len(w) > 15)))

# for token in a.words():
#     if token.startswith("Z" or "z"):
#       print(token, "fängt mit zet an")

# sein = ["bin", "bist", "ist", "sind", "seid", "sind"]
# for w in a.words():
#     if w in sein:
#         print(w, "ist eine Form von 'sein'")
#
# print(sorted(set(word.lower() for word in a.words() if word.isalpha())))

# häufigste wörter mit 4 buchstaben

# # c = [w for w in a.words() if len(w) == 4]
# freq1 = FreqDist(c)
# print(freq1)
# print(freq1.most_common(50))

#bestimmte wörter und ihre häufigkeit

# fdist = nltk.FreqDist(w.lower() for w in a.words())
# modals = ['kann', "muss", "darf"]
# for m in modals:
#     print(m + ':', fdist[m], end=' ')

# EINFACHE STATISTIKEN IM KORPUS:  	

# num_chars = len(a.raw())
# num_words = len(a.words())
# num_sents = len(a.sents())
# num_vocab = len(set(w.lower() for w in a.words()))

# print("durchschnittliche wortlänge: ", round(num_chars/num_words))
# print("durchschnittliche satzlänge: ", round(num_words/num_sents))
# print("lexikalische diversität: ", round(num_words/num_vocab))

# 2   CONDITIONAL FREQUENCY DISTRIBUTION

# Conditional Frequency: Worthäufigkeit in Abhängigkeit von einer Bedingung (das genre: news oder romanze). 
# Häufigkeitsbestimmung in Abhängigkeit von einer Bedingung heißt "ConditionalFreqDist"

# Beispiel 1

# from nltk.corpus import brown
# cfd = nltk.ConditionalFreqDist(
#         (genre, word)
#         for genre in brown.categories()
#         for word in brown.words(categories=genre))
# genre_word = [(genre, word) 
#         for genre in ['news', 'romance']
#         for word in brown.words(categories=genre)]
# print(len(genre_word))
# print(genre_word[:10])
# print(genre_word[-20:])
# print("_______________")
# cfd = nltk.ConditionalFreqDist(genre_word)
# print(cfd)
# print(cfd.conditions())
# print("_______________")
# print(cfd['news'])
# print("_______________")
# print(cfd['romance'])
# print("_______________")
# print(cfd['romance'].most_common(20))
# print("_______________")
# print(cfd['news'].most_common(20))

# Conditional Frequency "worthäufigkeit + genre" ergibt das gleiche Ergebnis wie direkt
# Frequency Distribution "worthäufigkeit" im schon ausgewählten Genre-Korpus

# print("_______________")
# from nltk.corpus import brown
# q = brown.words(categories='news')
# fdist3 = FreqDist(q)
# print (fdist3.most_common(50))

# BEISPIEL 2: 
# zählt wie häufig ein wort ("america" oder "citizen") in verschiedenen files vorkommt). 
# ausgabe liefert liste mit jahreszahl und häufiglkeit

# from nltk.corpus import inaugural
# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4]) 
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america', 'citizen'] 
#     if w.lower().startswith(target))
# print(cfd["america"].most_common(10))
# print(cfd["citizen"].most_common(10))

# BEISPIEL 3: 
# Häufigkeit des Auftretens von Wortlängen in verschiedenen Sprachen bestimmen und in geordneter Tabelle ausgeben
# Ausgabe in Tabelle funktioniert über die "Tabulate"-Methode. 
# Cumulative = True addiert alle ergebnisse auf. 
# Cumulative = False gibt einzelne häufigkeiten aus.

# from nltk.corpus import udhr
# languages = ['Chickasaw', 'English', 'German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
# cfd = nltk.ConditionalFreqDist(
#     (lang, len(word))
#     for lang in languages
#     for word in udhr.words(lang + '-Latin1'))
# cfd.tabulate(conditions=['English', 'German_Deutsch'],
#             samples=range(10), cumulative=False)

# AUFGABE: 
# wie häufig werden wochentag in verschiedenen genre-typen des brown-korpus genannt

# from nltk.corpus import brown
# cfd = nltk.ConditionalFreqDist(
#         (genre, word)
#         for genre in brown.categories()
#         for word in brown.words(categories=genre))
#         # wie würde ich hier .lower() einbauen, um potentiell kleingeschriebene tage zu finden? 
# genre = ["news", "romance"]
# day = ['Monday', "monday", 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
# cfd.tabulate(conditions=genre, samples=day)

# Häufigste Bigramme bestimmen

# text = fdp_wp.words()
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)
# a = cfd['Deutschland']
# print(a.most_common())

#UNGEWÖHNLICHES VOKABULAR rausstreichen

# def unusual_words(text):
#     text_vocab = set(w.lower() for w in text if w.isalpha())
#     english_vocab = set(w.lower() for w in nltk.corpus.words.words())
#     unusual = text_vocab - english_vocab
#     return sorted(unusual)

# WORDNET: SNYSET (Sammlung von Synonymen/Lemmas) -> Paar aus Synset und Wort = LEMMA (Eintrag)

#Write down all the senses of the word dish that you can think of. #
#Now, explore this word with the help of WordNet, using the same operations we used above.

# Try out NLTK's convenient graphical WordNet browser: nltk.app.wordnet(). 
# Explore the WordNet hierarchy by following the hypernym and hyponym links.

#2.1
# text1 = ["Ich", "gehe", "zur", "Schule"]
# text2 = ["Wie geht es dir?"]
# PP = text1[2:4]
# print(PP)

#2.2
# nltk.corpus.gutenberg.fileids()
# text = nltk.corpus.gutenberg.words('austen-persuasion.txt')
# print(len(text))
# print(len(set(text)))

#Wie oft kommen "mann" und "frau" in verschiedenen texten vor? 

# from nltk.corpus import inaugural
# print(inaugural.fileids())
# cfd = nltk.ConditionalFreqDist(
#     (target,fileid[:4])
#     for fileid in inaugural.fileids() 
#     for w in inaugural.words(fileid) 
#     for target in  ['men','women'] 
#     if w.lower().startswith(target))
# cfd.plot()


# Define a conditional frequency distribution over the Names corpus that 
# allows you to see which initial letters are more frequent for males vs. females (cf. 4.4).

# import matplotlib

# names = nltk.corpus.names
# male_names = names.words('male.txt')
# female_names = names.words('female.txt')

# cfd = nltk.ConditionalFreqDist(
#             (fileid, name[0])
#             for fileid in names.fileids()
#             for name in names.words(fileid))
# print(cfd.plot())

#Write a program to find all words that occur at least three times in the Brown Corpus.

# from nltk.corpus import brown
# text = brown.words()
# fdist = FreqDist(text)
# p = sorted(w.lower() for w in set(text) if fdist[w] > 2)
# print(p)
# print(len(p))

# Write a program to generate a table of lexical diversity scores (i.e. token/type ratios), 
# as we saw in 1.1. Include the full set of Brown Corpus genres (nltk.corpus.brown.categories()).   	

# from nltk.corpus import brown

# def lexical_diversity(text):
#     return len(set(text)) / len(text)

#Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.

# def top_bigrams(text):
# 	fdist = nltk.probability.FreqDist(nltk.bigrams(text)) 
# 	stopwords = nltk.corpus.stopwords.words('english') 
# 	top_list = [(x,y) for x,y in fdist.keys() if x.isalpha() and y.isalpha() and x not in stopwords and y not in stopwords] 
# 	return top_list[:50]

# print(top_bigrams(text3))

# print("__________________")

# def cw_bigrams(text, language, num_bigrams):
#     satzzeichen = [".", ";", ",", ":"]
#     bigrams = nltk.bigrams([w.lower() for w in text])

#     fdist = nltk.FreqDist(bigrams)
#     keys = fdist.keys()
#     stopwords = nltk.corpus.stopwords.words(language)

#     clean = []

#     for bigram in keys:
#         if bigram[0] not in stopwords and bigram[0] not in satzzeichen:
#             if bigram[1] not in stopwords and bigram[1] not in satzzeichen:
#                 clean.append(bigram)

#     return clean[:num_bigrams]

# print(cw_bigrams(text3, 'english', 50))

# TEXT GENERATION

#22 Define a function hedge(text) which processes a text and produces a new version with the word 'like' between every third word.

# def hedge(txt):
#     text = txt.words()

# def hedge(text):
#     n = 3
#     like = list(text) #text wird zur liste gemacht

#     while n <= len(like): #wenn n kleiner als textlänge
#         like.insert(n, 'like') #mach an position n ein like rein: insert nimmt 2 parameter: index und element
#         n = n + 4 #n um 3 erhöhen

#     print(like)

# Aufgabe 23: texterstellung

# 23.1

# def generate_model(cfdist, word, num=15):
#     for i in range(num):
#         print(word, end=' ')
#         word = cfdist[word].max()

# text = text2
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)

# print(generate_model(cfd, 'living'))

# 23.2

# Store the n most likely words in a list words then randomly choose a word from the list using random.choice(). (You will need to import random first.)

#fdist von text3

#frequent_w = fdist.most_common(50)
#satzzeichen = [".", ";", ",", ":"]
# print(frequent_w)

print("___________")    

# 5 mal soll eine wortliste durchsucht werden
# über eine soll bei jedem durchgang festgelegt werden, 
# wie viele inhaltswörter aus wörterliste rausgezogen werden sollen

fdist = FreqDist(text3) #häufigste wörter in text

anfang = sorted(w for w in set(text3) if w.istitle()) #wort am satzanfang, hauptsache groß 
anfang = list(anfang)

satzzeichen = [".", ";", ",", ":", "'"] #satzzeichen für satzende

inhalt = sorted(w for w in set(text3) if fdist[w] > 150 and w not in satzzeichen) #inhaltswörter in der mitte
inhalt = list(inhalt)

zufallszahl = random.randrange(5,15) #zufallszahl, um eine variable zahl von inhaltswörtern zu haben in den sätzen

for x in range(5): # 5 sätze
    a = (random.choice(anfang)) # random satzanfang raussuchen
    c = (random.choice(satzzeichen)) #random satzzeichen
    
    b = random.sample(inhalt, zufallszahl) #random anzahl aus inhaltswortliste nehmen
    str1 = " ".join(b) #umwandeln in string
    
    satz = [a + str1 + c] #so sieht satzformel aus

    print(satz)
    
    zufallszahl = random.randrange(5,15) #damit in den 5 schleifen immer andere sätze rauskommen
    


