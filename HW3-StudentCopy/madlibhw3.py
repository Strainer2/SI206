# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  
#JOHN STRAINER
# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk 
from nltk.book import text2
import random

tokens = text2[:151]

print("The First 150 tokens: ", tokens)

tagged_tokens = nltk.pos_tag(tokens)
tagged_tokens = tagged_tokens[:151] 


tagS = {"NN":"a noun","NS":"a plural noun","VB":"a verb","RB":"an adverb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NS":.15,"VB":.1,"RB":.1, "JJ":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":", "[", "]"]:
		return word
	else:
		return " " + word

words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagS[tag]))
		words.append(spaced(new_word))

print ("".join(words))

print("\n\nEND*******")

