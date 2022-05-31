#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 08:52:33 2022

@author: honepa
"""

import speech_recognition as speech_r
from transliterate import translit
from nltk.tokenize import word_tokenize
import sys

#функция распознавания текста из аудио
def recognition_text(path_to_audio):
    #указываем путь до аудио файла
    sample = speech_r.WavFile(path_to_audio)
    #инициализируем метод распознавания из модуля
    r = speech_r.Recognizer()
    #закидываем путь до ауди файла в метод распознавания
    with sample as audio:
        content = r.record(audio)
    #убираем шумы из аудиофайла
    with sample as audio:
        content = r.record(audio)
        r.adjust_for_ambient_noise(audio)
    #распознаём текст из аудиофайла
    text = r.recognize_google(content, language="ru-RU")
    return text

#реализация метода н-грам
def compare(s1, s2):
    #разбиваем искомое слово на триграммы
    ngrams = [s1[i:i+3] for i in range(len(s1))] 
    count = 0
    #считаем количество вхождений тригам в обрабатываемом слове 
    for ngram in ngrams: 
        count += s2.count(ngram) 
    # возвращаем отношения количества вхождений к длине слова, которое имеет максимальну длинну
    return count/max(len(s1), len(s2))

#функция подсчёта частоты слова в тексте
def counting_frequency_of_word_in_text(word, text):
    #разбиваем текст на токены
    text = word_tokenize(text)
    #переводим все буквы в нижний регистр
    text = [x.lower() for x in text]
    #временами распознавалка текста возвращает нам русские слова тринслитирируя на английский, поэтому транслитирируем обрабратно
    text = [translit(x, 'ru') for x in text]
    quantity_word = 0
    #считаем количество искомых слов в тексте
    for i in range(len(text)):
        if compare(word, text[i]) > 0:
            quantity_word = quantity_word + 1
    #возвращаем частоту искомого слова в тексте
    return quantity_word / len(text)

if __name__ == '__main__':
    try:
        #забираем путь до аудио файла из аргумента комадной строки
        path_to_audio = sys.argv[1]
        #забираем искомое слово из аргумента комадной строки
        word = sys.argv[2]
        #запускаем функцию распознавания текста
        text = recognition_text(path_to_audio)
        #выводим ответ
        print("Частота слова -%s- в распозанном тесте = %s" % (word, str(counting_frequency_of_word_in_text(word, text))))
    except IndexError:
        print("You have entered little data")