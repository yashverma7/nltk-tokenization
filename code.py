# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1srYG8ANNRY6yedp87vlP9aP_4vO1zNdc

Importing NLTK
"""

import nltk

text= ('I must be honest with you. I was about to go to sleep before I opened my mail and read your letter. Now I am wide awake, sitting upright, because you made me question my preferences between shoes and slippers.Be patient with me. I need proper peaceful sleep and let’s sort this out.I am a shoe person. Correction: I am a person obsessed with dry, dust-free feet. Whatever helps me keep a grip on my walk and posture in spite of my profusely sweaty feet, I am that person. Whatever keeps the grainy, pokey sensation of soil or sand in parts of my skin away, I am that person. I guess, I am a shoe person because it is loyal to my whole feet. Not making parts of it lying exposed and parts of it covered, without any symmetry. I am also cotton sock person, preferably red. Sometimes, I am a clean matte (anti-slippery) floor person. Basically, I am a person with issues.I really liked your host-guest theory of travelling, how we do not just get out of home when we travel, the home expands when we step foot at a place engulfing it into our comfort zone. But the thing is I wear socks all the time in my house, and open them when I go to bed, replacing the sock with a comforter. I guess I need that comfort zone close and maybe, mine is restricted to my own skin. So much so, that it doesn’t even include my own home. When I travel, I like wearing shoes, with a firm grip on myself, dust free, protected. When I face situations where I have to open them and I don’t want to, I usually wrinkle my nose. It doesn’t get better that I can’t wear those shoes again with a dirty feet. I take a handkerchief.Imagine my situation at the beach or in a hill stream, when the water feels soothing to my sweaty feet and removes the dust, only to attract more of it when I walk on the sand. I let it irritate me those times, because I always have the ocean and the river on my side. I like my bare feet drowning with no air bubbles left. I don’t like it when droplets of water make only a part of my feet wet, only to let me realise and miss the comfort of dry skin and scowl at the linger of irritation due to a little dampness. I don’t like it when I have to keep on brushing my left leg against my right to flatten the spheres of water. And repeat it with the right. I just realised why I don’t like drizzling rains.Eventually, when I have to get out of the water, I give up my fight with the dirt and wear those damn shoes with muddy feet. Those are the times I miss my slippery slippers. Don’t let my socks or shoes hear me say that. They do not know that sometimes I keep a back-up pair of red flip-flops for such scenarios. Does this make me a slipper person? I guess I am a slipper person when my feet are ankle deep in mud, so that there is no place for me to complain. No alternative. No uneasy half-done feeling. Otherwise, not much of a slipper person.I am a person who likes symmetry. All in or none at all. It’s difficult being me in this world with its shades of grey. But then, my favourite colour is red and thankfully it covers the entire spectrum. All I need is an emotion, and the rest is taken care of.Thank you for being the listener you are. This has been a selfish post. I used your letter for my sense of clarity. You always make me reflect and dig deep. I can finally sleep now. Goodnight.'

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

"""**Tokenization** 

Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. Token is a single entity that is building blocks for sentence or paragraph.

**Sentence Tokenization** 

Sentence tokenizer breaks text paragraph into sentences.
"""

sent_tokenize(text)

"""**Word Tokenization**

 Breaks sentence into words
"""

import regex
regex.split("[\s\.\,]",text)

from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
u= tokenizer.tokenize(text)
print(u)

"""**Stemming** 

is the process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words known as a lemma. Stemming is important in natural language understanding (NLU) and obviously in natural language processing (NLP) as well.
It is a process of linguistic normalization, which reduces words to their word root word or chops off the derivational affixes. For example, connection, connected, connecting word reduce to a common word "connect".
"""

from nltk.stem import PorterStemmer
stemmer= PorterStemmer()
for word in u:
  print(f"{word}>>>{stemmer.stem(word)}")

"""**Lemmatization**: 

retrieving the source of the word Lemmatization reduces words to their base word, which is linguistically correct lemmas. It transforms root word with the use of vocabulary and morphological analysis. Lemmatization is usually more sophisticated than stemming. Stemmer works on an individual word without knowledge of the context. For example, The word "better" has "good" as its lemma. This thing will miss by stemming because it requires a dictionary look-up.
"""

from nltk.stem import WordNetLemmatizer
lemmatizer= WordNetLemmatizer()
import nltk
nltk.download('wordnet')
for word in u:
  print(f"{word}>>>{lemmatizer.lemmatize(word)}")

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)

fdist.most_common(2)
[('is', 3), (',', 2)]
# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()

"""**Sentence segmentation using nltk**"""

sent_tokenize(text)

"""**from scratch using for loop**

**Stopwords**

Stopwords considered as noise in the text. Text may contain stop words such as is, am, are, this, a, an, the, etc.
In NLTK for removing stopwords, you need to create a list of stopwords and filter out your list of tokens from these words.
"""

x = word_tokenize(text)
stopwords = [';', ':', ',', '.', '!', '?']
new =[]
storey = ""
for i in x:
    if i in stopwords:
      storey = storey + i
      new.append(storey)
      storey = " "
    else:
      storey= storey +" "+ i
print(new)