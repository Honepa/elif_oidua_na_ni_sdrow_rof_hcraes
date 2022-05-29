#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:13:28 2022

@author: honepa
"""

import speech_recognition as speech_r
#import matplotlib.pyplot as plt
#import librosa.display

sample = speech_r.WavFile("test_audio.wav")

r = speech_r.Recognizer()

with sample as audio:
    content = r.record(audio)

with sample as audio:
    content = r.record(audio)
    r.adjust_for_ambient_noise(audio)

text = r.recognize_google(content, language="ru-RU")

file = open('text_audio', 'w')

for index in text:
    file.write(index)

"""
#plot waveshow
y , sf = librosa.load('test_audio.wav')   
plt.figure(figsize=(14, 5)) 

librosa.display.waveshow(y, sr=sf)

plt.show()
"""