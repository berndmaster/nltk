import nltk
from nltk.corpus import brown

# text = "They wind back the clock, while we chase after the wind."
# text = list(text.split())
# tagged_text = nltk.pos_tag(text)
# print (tagged_text)

# pos1 = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
# pos2 = {'bernhard': 'N', 'barbara': 'N', 'run': 'V', 'fastly': 'ADV'}
# pos1.update(pos2)
# print(pos1)
# print(list(pos1))
# print(list(pos1.items()))
# print(sorted(pos1.items()))

# lexical_entry_tree = {}
# lexical_entry_tree['headword'] = 'tree'
# lexical_entry_tree['pos']='N'
# print(lexical_entry_tree)


#Train a unigram tagger and run it on some new text. Observe that some words are not assigned a tag. Why not?

text = "When we perform a language processing task based on unigrams, we are using one item of context. In the case of tagging, we only consider the current token, in isolation from any larger context. Given such a model, the best we can do is tag each word with its a priori most likely tag. This means we would tag a word such as wind with the same tag, regardless of whether it appears in the context the wind or to wind."
text_sents = nltk.sent_tokenize(text) # text tokenize 
text_neu = []
for sentence in text_sents: # in sätze aufteilen
    text_words = nltk.word_tokenize(sentence)
    text_neu.append(text_words) # in liste speichern

# brown_tagged_sents = brown.tagged_sents(categories='news') #vergleichsdaten festlegen
# unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) #tagger intialisieren mit einem schon getagten datensatz
# print(unigram_tagger.tag(text_neu[1])) #tagger mit einem neuen satz trainieren 


# Train a bigram tagger with no backoff tagger, and run it on some of the training data. 
# Next, run it on some new data. What happens to the performance of the tagger? Why?

# from nltk.corpus import gutenberg
# from nltk.corpus import brown
# import nltk

# brown_tagged_sents = brown.tagged_sents(categories='news')
# #brown_sents = brown.sents(categories='news')
# size = int(len(brown_tagged_sents) * 0.7)
# train_sents = brown_tagged_sents[:size]
# test_sents = brown_tagged_sents[size:]

# bigram_tagger = nltk.BigramTagger(train_sents)
# print(bigram_tagger.accuracy(train_sents)) # ca. 80 % akkurat, weil tagger auch mit diesen sätzen trainiert wurde
# print(bigram_tagger.accuracy(test_sents)) # ca. 10 % akkurat, weil tagger diese daten noch nicht gesehen hat


# Use sorted() and set() to get a sorted list of tags used in the Brown corpus, removing duplicates.

# brown_tagged_words = brown.tagged_words(categories='news', tagset='universal')
# list_of_tags1 = sorted(set(x[1] for x in brown_tagged_words))
# print(list_of_tags1)

#aufgabe 15

# Write programs to process the Brown Corpus and find answers to the following questions:
# a. Which nouns are more common in their plural form, rather than their singular form? (Only consider regular plurals, formed with the -s suffix.)

# brown_tagged_words = brown.tagged_words(categories='news', tagset='universal')
# print(brown_tagged_words)
# freq = nltk.defaultdict(int) #dicctionary mit defaultvalue zahl öffnen
# for w in [w.lower() for (w,t) in brown_tagged_words if t.startswith('N')]: # alle getaggten, kleingeschriebenen wörter durchgehen, wenn tag = nomen
#     freq[w] +=1 #in dicctionary jeweils +1 für jedes wort
# print ("\nWhich Nouns are more common as plural?\n")

# #liste =[]

# for w in freq: #jedes wort in dicctionary freg durchgehen
#     if w+'s' in freq and freq[w+'s'] > freq[w]: #wenn pluralnomen ("+s") und freq von pluralnomen größer als freq von singularnomen
#         #liste.append(w)
#         #liste.append(freq[w])
#         #liste.append(freq[w+'s'])
#         print ("%s (%d, %d)" % (w, freq[w+'s'], freq[w])) #gebe aus: wort, frequenz von pluralnomen, frequenz von singularnomen 
# print(freq)


# b. Which word has the greatest number of distinct tags. What are they, and what do they represent?

brown_tagged_words_universal = brown.tagged_words(categories='news', tagset='universal')
brown_tagged_words = brown.tagged_words(categories='news')


#b.v1 (aus nltk)

# data = nltk.ConditionalFreqDist((word.lower(), tag)
#                                 for (word, tag) in brown_tagged_words)
# for word in sorted(data.conditions()):
#     if len(data[word]) > 3:
#         tags = [tag for (tag, _) in data[word].most_common()]
#         print(word, ' '.join(tags))

#b.v2

# print ("\nWord with the most distinct tags\n")
# word_tag = nltk.defaultdict(set)
# for w,t  in  brown_tagged_words:
#     word_tag[w.lower()].add(t) #für jedes wort die tags angeben
# m = max(len(word_tag[w]) for w in word_tag) #welche ist die maximale anzahl an tags?
# print ([(w, t) for w,t  in word_tag.items() if len(t) == m]) #liste von wort und tags mit dem maximalwert

# c. List tags in order of decreasing frequency. What do the 20 most frequent tags represent?

# tags = [w[1] for w in brown_tagged_words]
# fd = nltk.FreqDist(tags)
# freq_tags = [tag for tag in fd.most_common()]
# print(freq_tags)

# tags = [w[1] for w in brown_tagged_words_universal]
# fd = nltk.FreqDist(tags)
# freq_tags = [tag for tag in fd.most_common()]
# print(freq_tags)

# d. Which tags are nouns most commonly found after? What do these tags represent?

# brown_tagged_words_universal = brown.tagged_words(categories='news', tagset='universal')
# word_tag_pairs = nltk.bigrams(brown_tagged_words_universal) #bigramliste
# verb_preceders = nltk.FreqDist(a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN')  #im zweiten teil ein "noun" 
# print(verb_preceders.most_common()) 


# 18
# What proportion of word types are always assigned the same part-of-speech tag?


# Conditional Frequency
# Frequenz eines Paars aus Condition und Event (und nicht eines einzelnen Eintrags), z.b. (word, tag) = 3 oder (word, genre) = 5
# z.b. Angabe eines Frequenz eines Paars in einer Liste 


# 19
# Write code to search the Brown Corpus for particular words and phrases according to tags, to answer the following questions:

# Produce an alphabetically sorted list of the distinct words tagged as MD.

brown_tagged_words = brown.tagged_words(categories='news', tagset='universal')
# MD = [w.lower() for w, t in brown_tagged_words if t == 'MD']
# print(sorted(set(MD)))

# Identify words that can be plural nouns or third person singular verbs (e.g. deals, flies).

# nomen = [w.lower() for w, t in brown_tagged_words if w.endswith('s') and t.startswith('N')]# and t.startswith('v')]
# verben = [w.lower() for w, t in brown_tagged_words if w.endswith('s') and t.startswith('V')]# and t.startswith('v')]
# mixed = [w for w in nomen if w in verben]
# print(sorted(set(mixed)))

# Identify three-word prepositional phrases of the form IN + DET + NN (eg. in the lab).

# brown_news_tagged = nltk.corpus.treebank.tagged_words()
# word_tag_triples = nltk.trigrams(brown_news_tagged)
# triples = []
# for (w1,t1), (w2,t2), (w3,t3) in word_tag_triples:
#     if t1.startswith('I') and t2.startswith('D') and t3.startswith('N'): 
#         triples.append([w1, w2, w3])
# print(triples)


# In 3.1 we saw a table involving frequency counts for the verbs adore, love, like, prefer and preceding qualifiers absolutely and definitely. 
# Investigate the full range of adverbs that appear before these four verbs.

# adore, love, like, prefer

# suche nach bigramen, deren teil 1 = ADV ist und teil 2 = VERB, adore, love, like, prefer 

# brown_tagged_words_universal = brown.tagged_words(tagset='universal')
# word_tag_pairs = nltk.bigrams(brown_tagged_words_universal) #bigramliste
# ADV_prefer = [a[0] for (a, b) in word_tag_pairs if a[1] == 'ADV' and b[0] == 'prefer']
# ADV_adore = [a[0] for (a, b) in word_tag_pairs if a[1] == 'ADV' and b[0] == 'adore']
# ADV_love = [a[0] for (a, b) in word_tag_pairs if a[1] == 'ADV' and b[0] == 'love']
# ADV_like = [a[0] for (a, b) in word_tag_pairs if a[1] == 'ADV' and b[0] == 'like']

# print(ADV_prefer)


# We defined the regexp_tagger that can be used as a fall-back tagger for unknown words. 
# This tagger only checks for cardinal numbers. By testing for particular prefix or suffix strings, it should be possible to guess other tags. 
# For example, we could tag any word that ends with -s as a plural noun. Define a regular expression tagger (using RegexpTagger()) 
# that tests for at least five other patterns in the spelling of words. (Use inline documentation to explain the rules.)

# ing -> gerund
# ed -> past participle
# ly -> ADV

# patterns = [
#     (r'.*ing$', 'VBG'),                # gerunds
#     (r'.*ed$', 'VBD'),                 # simple past
#     (r'.*es$', 'VBZ'),                 # 3rd singular present
#     (r'.*ould$', 'MD'),                # modals
#     (r'.*\'s$', 'NN$'),                # possessive nouns
#     (r'.*s$', 'NNS'),                  # plural nouns
#     (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # cardinal numbers
#     (r'.*', 'NN')                      # nouns (default)
# ]

# regexp_tagger = nltk.RegexpTagger(patterns)
# brown_sents = brown.sents(categories='news')
# print(regexp_tagger.tag(brown_sents[4]))


# There are 264 distinct words in the Brown Corpus having exactly three possible tags.
# Print a table with the integers 1..10 in one column, and the number of distinct words in the corpus having 1..10 distinct tags in the other column.
# For the word with the greatest number of distinct tags, print out sentences from the corpus containing the word, one for each possible tag.
