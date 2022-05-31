#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 22:05:31 2022

@author: honepa
"""

from transliterate import translit
from nltk.tokenize import word_tokenize

def compare(s1, s2): 
    ngrams = [s1[i:i+3] for i in range(len(s1))] 
    count = 0  
    for ngram in ngrams: 
        count += s2.count(ngram) 
    return count/max(len(s1), len(s2))

file = open("text_audio")
recognized_text = file.read()

text = word_tokenize(recognized_text)
text = [x.lower() for x in text]
text = [translit(x, 'ru') for x in text]

index_found_word = text.index(max(text, key=lambda x: compare("крушке", x)))

