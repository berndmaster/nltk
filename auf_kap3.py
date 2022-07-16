# Kapitel 3 AUFGABEN

# AUFGABE 1
# s = 'colorless' # -> colourless
# print(s[:3] + "ou" + s[4:])

# AUFGABE 6
# '[a-zA-Z]+
# [A-Z][a-z]*
# p[aeiou]{,2}t
# \d+(\.\d+)?
#print(nltk.re_show(r'\d+(\.\d+)?',"Match 98.3232 .98 879 f9889"))
# ([^aeiou][aeiou][^aeiou])*
# \w+|[^\w\s]+'

# print(nltk.re_show(r'[a-zA-ZÄÖÜäüö]+', "Hä, warum geht das 123 %%"))

# suche = [w for w in fdist3 if re.search('\w+|[^\w\s]+', w)] #wird nach einem wort oder einer zahl gesucht
# for w in suche:
#     print(w + ':', fdist3[w])

# AUFGABE 7
#☼ Write regular expressions to match the following classes of strings:
#A single determiner (assume that a, an, and the are the only determiners).
#An arithmetic expression using integers, addition, and multiplication, such as 2*3+8.

# print(nltk.re_show(r'(a\s|an\s|the\s)', "The tree is on a mountain but an ant is coming to eat the bird."))
# print(nltk.re_show(r'([\d+][\+\*]|[\d+])+', "2*3+8 5+5+5 3*3*6 6+4*2"))
# test_exp="2*3+8 5+5+5 3*3*6 6+4*2"
# print(nltk.re_show(r'([0-9][\+\-\*]|[0-9])*',test_exp))

#AUFGABE 8 

#Save some text into a file corpus.txt. 
# Define a function load(f) that reads from the file named in its sole argument, 
# and returns a string containing the text of the file.

# def corpus_open(corpusfile):
#     f = open(corpusfile)
#     text = f.read()
#     return(text)
   
# Use nltk.regexp_tokenize() to create a tokenizer 
# that tokenizes the various kinds of punctuation in this text. 
# Use one multi-line regular expression, with inline comments, using the verbose flag (?x).

# f = open("crps.txt")
# raw = f.read()
# print(raw)

# def punctuation (text):
#     pattern = r'''(?x)
#     \W # alle nicht alphanumerischen Elemente, ähnlich zu re.findall(r"\W", raw)
#     '''
#     a = set(nltk.regexp_tokenize(raw, pattern))
#     print(a)

# punctuation ("crps.txt")

# def dates (text):
#     pattern = r'''(?x)
#     (January|May)\s(\d\d)
#     '''
#     b = nltk.regexp_tokenize(raw, pattern)
#     print(b)

# dates ("crps.txt")

# namen = ["Biden", "Harris", "Al Sharpton"]

# def names (text):
#     pattern = r'''(?x)
#     ^[A-Z][a-z]+
#     '''
#     b = nltk.regexp_tokenize (raw, pattern)
#     treffer = [n for n in b if n in namen]
#     print(treffer)

# names("crps.txt")

#Aufgabe 9
#list comprehension

# sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
# sent_len = [(x, len(x)) for x in sent]
# print(sent_len)

#Aufgabe 10
#Define a string raw containing a sentence of your own choosing. Now, split raw on some character other than space, such as 's'.

# sent = "The\t\tdog\t\tgave\n\nJohn\t\t the\n\nnewspaper."
# print(sent.split(" "))

#Aufgabe 11
#Write a for loop to print out the characters of a string, one per line.

# sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
# for word in sent: 
#     for char in word:
#         print(char)

#Aufgabe 14

# raw_words=nltk.corpus.brown.sents()[0]
# print(raw_words)

# raw_words.sort()
# print(raw_words)

# raw_words=nltk.corpus.brown.sents()[0]
# print(sorted(raw_words))

# Aufgabe 15

# print("5"*10) # 55555 
# print(5*10) # 50
# print(int("5")*10) # 50
# print(5*str(10)) #1010101010

# Aufgabe 16
# geht nicht

# Aufgabe 17

# print("Number is : %6s" % 'thisisaword')
# print("Number is : %-6s" % 'thisisaword')
# print("Number is : %6s" % 'aword')
# print("Number is : %-6s" % 'aword')

# Aufgabe 18
# Read in some text from a corpus, tokenize it, and print the list of all wh-word types that occur. 

#lang
# f = open("crps.txt")
# output_file = open('output.txt', 'w')
# raw = f.read()
# #print(raw)
# tokens = word_tokenize(raw)
# text = nltk.Text(tokens)
# words = [w.lower() for w in tokens if w.isalpha()]
# vocab = sorted(words)
# fdist3 = nltk.FreqDist(vocab)
# fdist3.plot(20)

# suche = [w for w in fdist3 if re.search('^wh+', w)] #wh-word ^\w\h[a-z]+ oder if w.startswith("wh") and len(w) < 6
# for w in suche:
#     print(w + ':', fdist3[w])

#kurz

# fdist = nltk.FreqDist(w.lower() for w in vocab)
# modals = ["what", "which"]
# for m in modals:
#     print(m + ':', fdist3[m], end=' ')

#in TXT-datei ausgeben
# f = open("LINKE.txt")
# output_file = open('output.txt', 'w')
# raw = f.read()
# tokens = word_tokenize(raw)
# stopwords = nltk.corpus.stopwords.words('german')
# text = nltk.Text(tokens)
# words = [w.lower() for w in tokens if w.isalpha() and w not in stopwords]
# vocab = sorted(words)
# fdist3 = nltk.FreqDist(vocab)
# print(fdist3.most_common(100), file=output_file)


# Aufgabe 19

#Read the file into a Python list using open(filename).readlines(). 
#Next, break each line into its two fields using split(), and convert the number into an integer using int(). The result should be a list of the form: 

# filename = 'wordfreq.txt'
# lines = open(filename).readlines()
# fields = [] # leere liste 
# for line in lines: #jede zeile durchgehen
#     field = line.split() #inhalte zeile zweiteilen
#     field[1] = int(field[1]) #teil2, also zahl, wird in zahl verwandelt, da vorher strg
#     fields.append(field) #in die leere liste "fields" werden die inhalte eingefügt
# print(fields)

#Aufgabe 20

# url = "https://www.bbc.com/"
# html = request.urlopen(url).read().decode('utf8')
# temp = re.findall(r"\w+", html) #hier temperatur entnehmen, hm! 
# print(temp)

#Aufgabe 21

# Write a function unknown() that takes a URL as its argument, and returns a list of unknown words that occur on that webpage. 
# In order to do this, extract all substrings consisting of lowercase letters (using re.findall()) and 
# remove any items from this set that occur in the Words Corpus (nltk.corpus.words). Try to categorize these words manually and discuss your findings.

#url öffnen
#beautiful soup
#tokenizieren
#re.findall mit lowercase lettern und if not in nltk.corpus.words

#siehe Arbeitsrechner


#Aufgabe 23

# Are you able to write a regular expression to tokenize text in 
# such a way that the word don't is tokenized into do and n't? 
# Explain why this regular expression won't work: «n't|\w+».

# text = ("we don't see quotation characters. I don't like school. You don't mean that.")
# #print(re.findall(r"do|n't|\w+", text))
# print(re.findall(r'(do)(n\'t)|\w+', text))


#aufgabe 24

#Try to write code to convert text into hAck3r, using regular expressions and substitution, where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8. 
#Normalize the text to lowercase before converting it. 
#Add more substitutions of your own. Now try to map s to two different values: $ for word-initial s, and 5 for word-internal s.

# text = ("we don't see quotation characters. I don't like school. You don't mean that.")
# text1 = re.sub(r'e', '3', text)
# text2 = re.sub(r'(i|I)', '1', text1)
# text3 = re.sub(r'o', '0', text2)
# text4 = re.sub(r'l', '|', text3)
# text5 = re.sub(r's', '5', text4)
# text6 = re.sub(r'\.', ' 5w33t!', text5)
# text7 = re.sub(r'(\b)(w)', r'\1$', text6) 
# print(text7)

# text = ("we don't see quotation characters. I don't like school. You don't mean that. I ate at home.")
# new_text = []

# pattern = re.compile(r'ate') #regEx-pattern aufstellen
# text = pattern.sub('8', text) #text nach pattern durchsuchen und mit element "8" substituieren

# pattern = re.compile(r'[eiols]|\.') #regEx-pattern aufstellen
# for w in text: #jeder buchstaben durchgehen
# 	if re.search(pattern, w): #buchstaben nach pattern gehen
# 		if w == 'e': #ersetzen
# 			w = '3'
# 		elif w == 'i':
# 			w = '1'
# 		elif w == 'o':
# 			w = '0'
# 		elif w == 's':
# 			w = '5'
# 		elif w == 'l':
# 			w = '|'
# 		elif w == '.':
# 			w = '5w33t!'
# 	new_text.extend(w) #buchstaben werden in liste gelegt
# new_text = ''.join(new_text) #alle elemente werden zusammengefügt

# # # pattern = re.compile(r'\b5')
# # # new_text = pattern.sub('$', new_text)
# print(new_text)

# AUFGABE 27

# y = [] # leere liste
# for i in range (500): #500 mal zufallstreffer
#     x = random.choice("aehh ") #aus der folgenden buchstabenfolge
#     y.append(x) #zufallstreffer in liste y legen
# z = ''.join(y) #zufallstreffer zusammenfügen 
# print(z)

# AUFGABE 31
# Process this list using a for loop, and store the length of each word in a new list lengths. 
# Hint: begin by assigning the empty list to lengths, using lengths = []. 
# Then each time through the loop, use append() to add another length value to the list. Now do the same thing using a list comprehension.

# saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
# length = []
# for w in saying:
#     length.append(len(w))
# print(length)

# saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
# length = [len(x) for x in saying]
# print(length)

# AUFGABE 32

# Split silly into a list of strings, one per word, using Python's split() operation, and save this to a variable called bland.
#Extract the second letter of each word in silly and join them into a string, to get 'eoldrnnnna'.
#Combine the words in bland back into a single string, using join(). Make sure the words in the resulting string are separated with whitespace.
#Print the words of silly in alphabetical order, one per lin

# silly = "newly formed bland ideas are inexpressible in an infuriating way"
# bland = silly.split()

# bland_neu = ' '.join(bland)    
# print(bland_neu)

# for w in bland:     
#     print(w[1],end='')

# bland = sorted(bland)
# for w in bland:
#     print(w)

# AUFGABE 33
# words = ["Hallo", "Wie", "geht", "es", "dir", "?"]
# print(words.index("geht"))

# silly = "newly formed bland ideas are inexpressible in an infuriating way"
# bland = silly.split()
# phrase = bland[:6] # oder: phrase = bland[:bland.index('in')]  
# print (phrase)


#AUFGABE 34

# adjectives = ["Zelandian", "African", "Asian", "Australian", "Canadian"]
# nouns = []
# for w in adjectives: 
#     nouns.append(w[:-1])
# print(nouns)

# adjectives = ["Zelandian", "African", "Asian", "Australian", "Canadian"]
# adjectives = " ".join(adjectives)
# print(adjectives)
# nouns_new = re.sub(r'(\w+)an', r'\1a', adjectives) #???
# nouns = nouns_new.split(" ")  
# print(nouns)

# AUFGABE 37

#v1

# url = "https://www.bbc.com/"
# html = request.urlopen(url).read().decode('utf8')
# ohne_html = re.sub(r'<[^>]+>', '', html)
# ohne_whitespace = re.sub(r'\s', " ", ohne_html)
# print(ohne_whitespace)

#v2
# f = open('file.html')
# raw = html.read() 
# pattern = re.compile(r'<[^>]+>') #sets a pattern for stripping out tags
# processed_text = pattern.sub('', html) #strips them
# pattern = re.compile(r'\s') #sets a new pattern for normalizing whitespace.
# processed_text = pattern.sub(' ', processed_text)
# print(processed_text)

# AUFGABE 43 List comprehension

# words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
# vokale = [''.join(re.findall(r'[aeiou]', w)) for w in words]
# print(sorted(vokale))
#['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa']

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy" #0 bis 2 werden angehangen, 2 bis 5 werden angehangen
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000" #i=1 an stelle 1, i=1 an stelle 5

words = []
last = 0
for i in range(len(seg1)): #alle 55 zeichen von seg1 durchgehen 
    if seg1[i] == '1': #wenn in seg1 an stelle [i] eine "1" steht
        words.append(text[last:i+1]) #hänge wortliste aus text von "i" bis stelle "i"+1 an
        last = i+1 #markiert die wortgrenze
words.append(text[last:])
print(words)