#!/usr/bin/env python3

import pickle
import numpy as np
import sys
import os.path

# TODO: parallelize prediction to improve performance
def pred(X, forest): # make prediction for forest
    for x in X: # import needed trees
        bucket = x[5] - 19968
        if forest[bucket] == None and os.path.isfile(f"forest/{bucket}.tree"):
            forest[bucket] = pickle.load(open(f"forest/{bucket}.tree", "rb"))

    return [forest[x[5] - 19968].predict(x.reshape(1,-1)).item() if forest[x[5] - 19968] != None else np.nan for x in X]

def to_hiragana(text, forest):
    text_int = np.fromiter((ord(char) for char in text), dtype=int)
    paded_int = np.pad(text_int, 5, 'constant', constant_values=0)

    mask = np.logical_and(text_int > 19967, text_int < 40846) # supported unicode range
    X = np.fromiter((paded_int[i:i+11] for i in range(len(text)) if mask[i]), dtype=np.dtype((int, 11)))
    bundled_prediction = pred(X, forest)

    return ''.join(char if not boolean
                   else f'{char}[{bundled_prediction.pop(0)}]'
                   for char, boolean in zip(text, mask))


forest = [None] * 20878 # Initialize buckets
print(to_hiragana(sys.argv[1], forest))
