#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 22:05:31 2022

@author: honepa
"""

from transliterate import translit
from nltk.tokenize import word_tokenize
from Levenshtein import distance

file = open("text_audio")
recognized_text = file.read()

text = word_tokenize(recognized_text)
text = [x.lower() for x in text]
text = [translit(x, 'ru') for x in text]

index_found_word = text.index(min(text, key=lambda x: distance("главы", x)))

print("%s %s %s %s %s" % (text[index_found_word - 2], text[index_found_word - 1], text[index_found_word], text[index_found_word + 1], text[index_found_word + 2]))
