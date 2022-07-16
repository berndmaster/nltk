import random
import nltk
from nltk.corpus import names
from nltk.corpus import brown

# Supervised Classification

# Classification is the task of choosing the correct class label for a given input.
# supervised classifcation basiert auf einem trainingsset mit korrekt klassifizierten daten
# input->feature extractor->feature set->feature values

print(a[1:]) #ab 1
print(a[:1]) #bis 1
print(len(labeled_names))

# _____________

def gender_features(name):
     feature_extractor: welche feature sind relevant für suche?
     features = {}
     features['last_letter'] = name[-1:]
     #features['last_two_letter'] = name[-2:]
     #features['first_letter'] = name[0]
     #features[ 'length_name'] = len(name)
     return features

# daten werden gemischt
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)

# daten werden aufgeteilt
train_names = labeled_names[1500:] # training_set: train the model # ab 1500
devtest_names = labeled_names[500:1500] # dev_set: perform error analysis # von 500 bis 1500
test_names = labeled_names[:500] # test set: final evaluation of system # bis 500

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print("accuracy:",nltk.classify.accuracy(classifier, devtest_set))
classifier.show_most_informative_features(5)

# mit dev_test herausfinden, welche tags falsch vergeben werden
# und dann feature_extractor verbessern

errors = []
for (name, tag) in devtest_names: #alle namen mit gender in dev_test durchgehen
     guess = classifier.classify(gender_features(name)) #gender tippen
     if guess != tag: #wenn tipp ungleich tag 
         errors.append((tag, guess, name)) #in liste anhängen
print(errors)

# ____________

from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
 random.shuffle(documents)

# daten, filmrezensionen enthalten text (liste) und klassifikation neg/pos am ende

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words()) #häufigkeit aller wörter im moviekorpus
word_features = list(all_words)[:2000] #erstmal nur die ersten 2000 wörter, da sonst zu langsam

def document_features(document):
     #feature_extractor, der checkt, ob text wörter aus "typischen" movie-wörtern enthält
     document_words = set(document) 
     features = {}
     for word in word_features:
         features['contains({})'.format(word)] = (word in document_words)
     return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(5)) 

# ___________

#POS-tagging: simpel

from nltk.corpus import brown

# alle wörter werden auf drei verschiedene suffixlängen durchgegangen, die frequenz der suffixe wird gezählt
# und die häufigsten werden in einer liste gesammelt
suffix_fdist = nltk.FreqDist()
for word in brown.words():
     word = word.lower()
     suffix_fdist[word[-1:]] += 1
     suffix_fdist[word[-2:]] += 1
     suffix_fdist[word[-3:]] += 1
common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]

def pos_features(word):
     #checkt, welche suffixe ein wort enthält (z.B. 'endswith(nt)': False) und ordnet boolean (true/false) zu
     features = {}
     for suffix in common_suffixes:
         features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)
     return features

#pos_features("definitly")

tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n,g) in tagged_words]

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

classifier = nltk.DecisionTreeClassifier.train(train_set)
nltk.classify.accuracy(classifier, test_set)

print(classifier.classify(pos_features('dogs')))

# ___________

# POS-tagging: advanced

# a = "I must say that this is a really big house you are living in with your family here in Boston"
# a = a.split()
# a = list(a)

def pos_features(sentence, i): #tagging basiert auf suffixen und vorangehendem wort (aber nicht wortart)
     # gibt an suffix 1, 2, 3 von einem wort (an position i) in einem satz an
     # plus gibt wort vor zielwort an (kontext)
     features = {"suffix(1)": sentence[i][-1:],
                 "suffix(2)": sentence[i][-2:],
                 "suffix(3)": sentence[i][-3:]}
     if i == 0:
         features["prev-word"] = "<START>"
     else:
         features["prev-word"] = sentence[i-1]
     #print(features)
     return features

tagged_sents = brown.tagged_sents(categories='news')
# tagged_sents = tagged_sents[0:5] #5 sätze, die als wort + tag gespeichert sind

featuresets = []
for tagged_sent in tagged_sents:
     untagged_sent = nltk.tag.untag(tagged_sent) #sätze werden enttaggt
     for i, (word, tag) in enumerate(tagged_sent): 
         featuresets.append( (pos_features(untagged_sent, i), tag) ) 
         # in jedem ungetagten satz wird für jedes wort 
         # ein listeneintrag mit suffix 1,2,3 + vorangehenden wort und tag erstellt
         # z.B. [({'suffix(1)': 'e', 'suffix(2)': 'he', 'suffix(3)': 'The', 'prev-word': '<START>'}, 'AT'), 
         #       ({'suffix(1)': 'n', 'suffix(2)': 'on', 'suffix(3)': 'ton', 'prev-word': 'The'}, 'NP-TL'), 
         #       ({'suffix(1)': 'y', 'suffix(2)': 'ty', 'suffix(3)': 'nty', 'prev-word': 'Fulton'}, 'NN-TL') ...
#print(featuresets)

# train-daten und test-daten festlegen
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

# trainieren mit traindaten
classifier = nltk.NaiveBayesClassifier.train(train_set)

# genauigkeit messen mit testdaten
print(nltk.classify.accuracy(classifier, test_set))

# print("___________")

# POS-tagging: noch advanceder

tagged_sents = brown.tagged_sents(categories='news')
tagged_sents = tagged_sents[0] 

def pos_features(sentence, i, history): #tagging basiert auf suffixen und vorangehendem wort und seinem tag
    
    features = {"suffix(1)": sentence[i][-1:],
                 "suffix(2)": sentence[i][-2:],
                 "suffix(3)": sentence[i][-3:]}
    if i == 0:
         features["prev-word"] = "<START>"
         features["prev-tag"] = "<START>"
    else:
         features["prev-word"] = sentence[i-1]
         features["prev-tag"] = history[i-1]
    print(features)
    return features

# print("___________")

# 2.1 Sentence Segmentation

sents = nltk.corpus.treebank_raw.sents()
sents = sents[:6]
tokens = []
boundaries = set()
offset = 0
for sent in sents: #jeden satz einzeln durchgehen, sätze sind in als einzelne elemente in liste gespeichert 
    tokens.extend(sent) #wörter des satzes der liste anhängen
    offset += len(sent) #länge des satzes speichern 
    boundaries.add(offset-1) #alle auftretenden satzlängen in liste als set speichern = entspricht potentiellen satzlängen

def punct_features(tokens, i):
    return {'next-word-capitalized': tokens[i+1][0].isupper(), #ist der buchstabe des nächsten worts großgeschrieben?
            'prev-word': tokens[i-1].lower(), #angabe des vorangehenden wortes
            'punct': tokens[i], #wort
            'prev-word-is-one-char': len(tokens[i-1]) == 1} #länge des wortes ist gleich eins?

print(punct_features(tokens, 3))

featuresets = [(punct_features(tokens, i), (i in boundaries))
            for i in range(1, len(tokens)-1)
            if tokens[i] in '.?!']
# create a list of labeled featuresets by selecting all the punctuation tokens, 
# and tagging whether they are boundary tokens or not
# ergibt: 
     #({'next-word-capitalized': True, 'prev-word1': 'n', 'prev-word2': 'elsevier', 'punct': '.', 'prev-word-is-one-char': True}, False)
     #({'next-word-capitalized': False, 'prev-word1': 'group', 'prev-word2': 'publishing', 'punct': '.', 'prev-word-is-one-char': False}, True) 
