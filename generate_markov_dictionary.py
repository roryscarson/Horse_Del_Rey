#!/usr/bin/env python -tt
  
import pickle
import codecs

fh = codecs.open("lyrics6.txt", encoding='utf-16')
chain = {}
  
def generate_trigram(words):
    if len(words) < 3:
        return
    for i in xrange(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])
  
for line in fh.readlines():
    words = line.split()
    #generates 3 consecutive words
    for word1, word2, word3 in generate_trigram(words):
        #creates tuplet from first 2 words and adds word3 as value
        key = (word1, word2)

        if key in chain:
            chain[key].append(word3)
        #or creates new key with word3 as value
        else:
            chain[key] = [word3]

pickle.dump(chain, open("chain.p", "wb" ))