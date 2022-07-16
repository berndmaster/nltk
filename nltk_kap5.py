import nltk
from nltk.corpus import brown

# a = "Bernhard"
# print(a[1:]) #ab 1
# print(a[:1]) #bis 1

# 1. POS-Tagging

#1.1 .pos_tag

# Wortarten an Wörter anheften: Tuple aus Wort und Wortart, z. B. ('a', 'DT')
# pos_tagger funktioniert über .pos_tag() im englischen, im deutschen leider nicht

def pos_tagging(text):
    text = list(text.split())
    tagged_text = nltk.pos_tag(text)
    print (tagged_text)

# pos_tagging("It was a race against time")
# pos_tagging("We race against time")

# text = nltk.word_tokenize("Das ist ein einfacher Satz.")
# wortart = ["DEM", "KOP", "ART", "ADJ", "N"]
# zusammen = list(zip(text, wortart))
# print(zusammen)


#1.2 tagging in nltk-corpora 

# texte in nltk-corpus sind teilweise schon getaggt. dadurch lassen sie sich anschauen mittels .tagged_words(). 

# a = nltk.corpus.brown.tagged_words()
# print(a)
# b = nltk.corpus.brown.tagged_words(tagset='universal')
# print(b)


# 1.3 suchen nach tags

# Häufigste Wortarten und ihre Frequenz heraussuchen:

#brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
#tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
#print(tag_fd.most_common())
#tag_fd.plot(cumulative=True)

# Welche wortart steht am häufigsten vor einem nomen?

#brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
#word_tag_pairs = nltk.bigrams(brown_news_tagged) #bigramliste
#word_tag_pairs = list(word_tag_pairs)
#print(word_tag_pairs[100:200])
#noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN']  #alle wortartentags von den paaren angeben, die im zweiten teil ein "noun" stehen haben
# fdist = nltk.FreqDist(noun_preceders) #häufigkeit der tags
# a = [tag for (tag, _) in fdist.most_common()] #häufigste tags ausgeben
# print(a)

# welche sind die häufigsten verben in einem korpus?

# wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
# word_tag_fd = nltk.FreqDist(wsj)
# # #a = word_tag_fd.most_common(20)
# # #a = [wt[0] for (wt, _) in word_tag_fd.most_common(500) if wt[1] == 'VERB'] #liste von teil1 (wt[0]) von wort-tag-pairs angeben, wenn teil2 = verb
# # #print(a[5][0][0])
# # a = [(x[0],x[1], y) for (x, y) in word_tag_fd.most_common(500) if x[1] == 'VERB'] #ausgabe von Verb, Tag und Anzahl
# a = [(x[0], y) for (x, y) in word_tag_fd.most_common(500) if x[1] == 'VERB'] #ausgabe von Verb und Anzahl
# print(a)

# welches ist das häufigste tag, das ein wort erhält?

# wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
# cfd1 = nltk.ConditionalFreqDist(wsj)
# a = cfd1['yield'].most_common()
# print(a)

# welches sind die häufigsten wörter, die ein bestimmtes tag bekommen?

# wsj = nltk.corpus.treebank.tagged_words()
# cfd2 = nltk.ConditionalFreqDist((y, x) for (x,y) in wsj) #umgedreht
# a = list(cfd2['NN'])
# print(a)

# welche wörter erhalten sowohl ein als auch ein anderes tag? 

# wsj = nltk.corpus.treebank.tagged_words()
# cfd1 = nltk.ConditionalFreqDist(wsj)
# a = [w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]]
# print(a)

# was steht am häufigsten vor "kicked"/"been"?

# brown_news_tagged = nltk.corpus.treebank.tagged_words()
# word_tag_pairs = nltk.bigrams(brown_news_tagged) #bigramliste
# verb_preceders = [a for (a, b) in word_tag_pairs if b[0] == 'been']  #alle wortartentags von den paaren angeben, die im zweiten teil ein "noun" stehen haben
# print(verb_preceders)
# fdist = nltk.FreqDist(verb_preceders) #häufigkeit der tabs
# a = [(x[0],x[1], y) for (x, y) in fdist.most_common(20)] #häufigste tags ausgeben
# print(a)

# was steht am häufigsten vor einem past particple?

# brown_news_tagged = nltk.corpus.treebank.tagged_words()
# word_tag_pairs = nltk.bigrams(brown_news_tagged) #bigramliste
# verb_preceders = [a for (a, b) in word_tag_pairs if b[1] == 'VBN']
# print(verb_preceders)
# fdist = nltk.FreqDist(verb_preceders) #häufigkeit der tabs
# fdist.tabulate()
# a = [(x[0],x[1], y) for (x, y) in fdist.most_common(20)] #häufigste tags ausgeben
# print(a)

# welche wortart steht am häufigsten vor "been"? inklusive tabulate-funktion

# brown_news_tagged = nltk.corpus.treebank.tagged_words()
# word_tag_pairs = nltk.bigrams(brown_news_tagged) #bigramliste
# verb_preceders = [a[1] for (a, b) in word_tag_pairs if b[0] == 'been']  #alle wortartentags von den paaren angeben, die im zweiten teil ein "been" stehen haben
# #print(verb_preceders)
# fdist = nltk.FreqDist(verb_preceders) #häufigkeit der tabs
# fdist.tabulate()

# suche nach konstruktionen [Verb to Verb] mittels trigram

# def process(sentence):
#     for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence): 
#         if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')): 
#             print(w1, w2, w3)

# for tagged_sent in brown.tagged_sents():
#     process(tagged_sent)


# 3.dicctionaries

# data type that can be used for mapping between arbitrary types bzw. zuordnung beliebiger daten
# dicctionary besteht aus key und zugeordnetem value (z.b run: verb)

# pos = {} # leeres dicctionary
# pos['colorless'] = 'ADJ' # wert wird angehangen
# pos['ideas'] = 'N'
# print(pos)
# print(list(pos))
# print(dict(pos))

# .key = nur key ausgeben 
# .values = nur value ausgeben
# .items = key und value ausgeben

pos = {'furiously': 'ADV', 'ideas': 'N', 'colorless': 'ADJ', 'sleep': 'V'}
# print(pos)
# print(pos.keys())
# print(pos.values())
#print(pos.items())
#print(list(pos.items()))


#defaultdict: einem key direkt einen defaultdatentyp oder einen defaultwert zuweisen

# defaultdatentyp

from collections import defaultdict
# pos = defaultdict(list)
# pos['sleep'] = ['NOUN', 'VERB']
# pos['ideas']
# print(pos)

# defaultwert mittels lambda: jder key bekommt einen defaultwert zugewiesen. das kann sein:
# string, int, list etc. sein

# pos = defaultdict(lambda: 'NOUN')
# pos['colorless'] = 'ADJ'
# pos['blog']
# pos['ideas']
# pos['town']
# print(pos)
# print(pos.items())
# print(list(pos.items()))


# We can preprocess a text to replace low-frequency words with a special "out of vocabulary" token UNK, 
# with the help of a default dictionary. 
# Can you work out how to do this without reading on?

#a) meine lösung (ohne dictionary)

# text = "Hallo Hallo, das ist ein Text, der einfach nur ein Text ist."
# text = nltk.word_tokenize(text)
# fd = nltk.FreqDist(text)
# text_neu = []
# for w in text: 
#     if fd[w] > 1:
#         text_neu.append(w)
#     if fd[w] == 1:
#         text_neu.append("unk")
# print(text_neu)


#b) musterlösung

# alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
# vocab = nltk.FreqDist(alice)
# v1000 = [word for (word, _) in vocab.most_common(1000)] #häufigste wörter, nur wörter ohne frequenz
# mapping = defaultdict(lambda: 'UNK') #alle dicctionary-einträge erhalten "unk" als defaultwert
# for v in v1000: #alle häufigsten 1000 wörter kommen in dicctionary mit z.b. key = "like" und vale = "like"
#     mapping[v] = v
# print(mapping)
# alice2 = [mapping[v] for v in alice] #alle anderen wörter erhalten value "unk"
# print(alice2[:150])

# bei 3.5

# wichtige funktion1: tokenizieren, taggen, in dicctionary, zählen wie häufig

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
text_tagged = nltk.pos_tag(text)
counts = defaultdict(int)
for (word, tag) in text_tagged:
    counts[tag] += 1
print(list(counts.items()))

# last_letters = defaultdict(list)
# words = nltk.corpus.words.words('en')
# for word in words:                  #dicctionary mit allen endungen w-2:
#     key = word[-2:]                 #allen endungen (key = -2:) werden die values angehangen (wörter im korpus)
#     last_letters[key].append(word)
# print(list(last_letters['ly']))

# ly = []                            #gleiche funktion wie drüber, aber nur mit endung "ly"
# words = nltk.corpus.words.words('en')
# for w in words:
#     if w[-2:] == "ly":
#         ly.append(w)
# print(ly)
# print(len(ly))

#funktion1 schematisch ausgedrückt: 
    # my_dictionary = defaultdict(function to create default value)
    # for item in sequence:
        # my_dictionary[item_key] is updated with information about item


# wichtige funktion2: sorting a dictionary by its values

# from operator import itemgetter
# print(sorted(counts.items(), key=itemgetter(1), reverse=True)) 


#weitere anwendung: anagrame

# words = nltk.corpus.words.words('en') #alle englischen wörter
# anagrams = defaultdict(list) #default-dicctionary mit liste
# for word in words: #wörter durchgehen
#     key = ''.join(sorted(word)) #jedes wort wird sortiert (buchstaben) und dann als key in dicctionary gepackt
#     anagrams[key].append(word) #jedem sortiertem wort-key, also dem anagram, werden die wörter, also die values, zugeordnet
# print(anagrams['abelt'])


#weitere anwendung: welche tags erhält ein wort, das nach einer bestimmten wortart steht?

# pos = defaultdict(lambda: defaultdict(int))
# brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
# for ((w1, t1), (w2, t2)) in nltk.bigrams(brown_news_tagged): #durch alle bigrame (wort und tag) gehen
#     pos[(t1, w2)][t2] += 1 #eintrag in dicctionary enthält tag von wort1, wort2 und tag von wort2
# a = pos[('DET', 'right')] #suche nach tag determiner und wort "right"
# print(a.items())


# dicctionary umdrehen (key:value -> value:key)

# counts = defaultdict(int)
# for word in nltk.corpus.gutenberg.words('milton-paradise.txt'):
#     counts[word] += 1 #dicctionary geordnet nach wort(key) und frequenz(value)
# pos2 = dict((value, key) for (key, value) in counts.items()) #dicctionary geordnet nach frequenz(value) und wort(key)
# print(sorted(list(pos2.items())))


# dicctionary umdrehen geht auch so:

# pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'} #dicctionary
# pos.update({'cats': 'N', 'scratch': 'V', 'peacefully': 'ADV', 'old': 'ADJ'}) #mehr einträge hinzufügen
# pos2 = defaultdict(list) #defaultwerte = liste
# for key, value in pos.items(): #dicctionary durchgehen
#     pos2[value].append(key) #werte als keys setzen und keys dem wert zuordnen
# print(pos2)


# 4. POS-tagging-Techniken

# !!! Text -> in Sätze segmentieren -> Wörter tokenisieren -> POS-tagging!!!

# text = "Das ist ein einfacher Text. In ihm steht nicht viel. Aber dennoch enthält er Inhalt. Der Inhalt besteht aus Konzepten."
# text_sents = nltk.sent_tokenize(text)
# text_neu = []
# for sentence in text_sents:
#     text_words = nltk.word_tokenize(sentence)
#     text_neu.append(text_words)
#     tagged = nltk.pos_tag(text_words)
#     print(tagged)
# print(text_neu)

# from nltk.corpus import brown
# brown_tagged_sents = brown.tagged_sents(categories='news')
# brown_sents = brown.sents(categories='news')
# print(brown_sents[2007])

# Lookup-Tagger

# fd = nltk.FreqDist(brown.words(categories='news'))
# cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news')) #cfd = paar aus event und condition bzw. wort und kategorie "news"
# #print(sorted(list(cfd.items())))
# #p = [freq for (word, freq) in cfd.items()]
# most_freq_words = fd.most_common(100)
# likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
# print(likely_tags)

# wichtige Taggingbefehle:
 
# default_tagger = nltk.DefaultTagger('NN') #alles mit NN taggen
# default_tagger.tag(tokens) #tokens taggen mit taggermodell
# default_tagger.evaluate(brown_tagged_sents) #getaggte daten mit golden standard abgleichen
    

# Taggertypen

# 1. Default-tagging (alles Nomen)
# 2. Regular Expression-tagging (z. B. r'*/'s$ -> Nomen im Genitiv, r'*\er -> Plural im Dt.)
# 3. Lookup Tagger (z.b. 100 häufigste Worttags aus anderem Korpus nehmen und auf Daten draufsetzen)
# 4. Unigram tagger: statistisch häufigste Tags werden an Wortformen vergeben 
# 5. N-Gram Tagging: bezieht vorangehenden tag-kontext ein und wählt davon aus das wahrscheinlichste tag.  
    # N-Gram-Tagger bzw. Bigram-Tagger mit n = 2 bezieht zielwort und  worte davor ein 
    # Er lebt nur noch im Gestern (Präposition vor Nomen gestern: frequenz = 1 im gesamten korpus) 
    # vs. 
    # Ich war gestern arbeiten (Verb vor Adverb gestern: frequenz = 5 im gesamten Korpus)
        # -> Tagger wählt eher Tag Adverb, weil häufiger in Daten
    # N-Gram-Tagger mit n = 3 beziehen zielwort und beide worte davor ein 


# Trainieren Unigram tagger

# from nltk.corpus import brown

# text = "When we perform a language processing task based on unigrams, we are using one item of context. In the case of tagging, we only consider the current token, in isolation from any larger context. Given such a model, the best we can do is tag each word with its a priori most likely tag. This means we would tag a word such as wind with the same tag, regardless of whether it appears in the context the wind or to wind."
# text_sents = nltk.sent_tokenize(text) # text tokenize 
# text_neu = []
# for sentence in text_sents: # in sätze aufteilen
#     text_words = nltk.word_tokenize(sentence)
#     text_neu.append(text_words) # in liste speichern

# brown_tagged_sents = brown.tagged_sents(categories='news') #vergleichsdaten festlegen
# unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) #tagger intialisieren mit einem schon getagten datensatz
# print(unigram_tagger.tag(text_neu[1])) #tagger mit einem neuen satz trainieren 
# print(unigram_tagger.accuracy(brown_tagged_sents)) #tagger-ergebnis evaluieren 



def unigram_tagging_one_sentence(text): 
    #funktion, die einen unbekannten satz taggt und evaluiert, wie akkurat getaggt wurde
    #text muss als volltext rein
    text_sents = nltk.sent_tokenize(text) # text tokenize 
    text_neu = []
    for sentence in text_sents: # in sätze aufteilen
        text_words = nltk.word_tokenize(sentence)
        text_neu.append(text_words) # in liste speichern
    brown_tagged_sents = brown.tagged_sents(categories='news') #vergleichsdaten festlegen
    unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) #tagger intialisieren mit einem schon getagten datensatz
    print(unigram_tagger.tag(text_neu[0])) #tagger mit einem neuen satz trainieren 
    print(unigram_tagger.accuracy(brown_tagged_sents)) #tagger-ergebnis evaluieren 

# N-Gram-Tagger, bzw. Bi-Gram-Tagger

# text = "When we perform a language processing task based on unigrams, we are using one item of context. In the case of tagging, we only consider the current token, in isolation from any larger context. Given such a model, the best we can do is tag each word with its a priori most likely tag." 
# text_sents = nltk.sent_tokenize(text) # text tokenize 
# text_neu = []
# for sentence in text_sents: # in sätze aufteilen
#     text_words = nltk.word_tokenize(sentence)
#     text_neu.append(text_words)
# train_sent = text_neu[0]

# brown_tagged_sents = brown.tagged_sents(categories='news')
# bigram_tagger = nltk.BigramTagger(brown_tagged_sents)

# print(bigram_tagger.tag(train_sent))
# print(bigram_tagger.accuracy(brown_tagged_sents))


# tagger-abfolgen

#backoff = wenn 1 tagger keine lösung findet, kommt ein anderer zum einsatz 

# from nltk.corpus import brown
# brown_tagged_sents = brown.tagged_sents(categories='news') #

# size = int(len(brown_tagged_sents) * 0.9)
# train_sents = brown_tagged_sents[:size]
# test_sents = brown_tagged_sents[size:]

# t0 = nltk.DefaultTagger('NN') #default-tagging mit NN
# t1 = nltk.UnigramTagger(train_sents, backoff=t0) #unigram-tagger verteilt häufigste wortart-wort-paare
# t2 = nltk.BigramTagger(train_sents, backoff=t1) #bigram-tagger 
# t3 = nltk.TrigramTagger(train_sents, backoff=t2) # trigram tagger
# print(t3.accuracy(test_sents))


# Wortartenklassifikation:

    #-> siehe Imos Wortartenmurmelbahn
# Morphologie: z.B. -schaft = Nomen
# Flektion: konjugierbar/deklinierbar, 
# Syntax: Vorfeldfähig? zwischen Artikel/Nomen?
