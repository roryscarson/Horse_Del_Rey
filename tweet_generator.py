#!/usr/bin/env python -tt

import pickle
import random

chain = pickle.load(open("chain.p", "rb"))

muse = []
keys = chain.keys()
muse_length = 0
index = random.randrange(0,len(keys))
w1, w2 = keys[index]


while True:
	w1, w2 = w2, random.choice(chain[(w1, w2)])
	if (len(muse) + muse_length + len(w2)) >= 141:
		break
	muse_length += len(w2)
	muse.append(w2)

print ' '.join(muse) 

