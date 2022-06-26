#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 14:27:21 2022

@author: honepa
"""

import os
from frequency_word import recognition_text, counting_frequency_of_word_in_text
import shutil
import sys
#получение пути до директории с аудиофайлами для распознавания
path = sys.argv[1]
#получение имени директории
new_dir_name = sys.argv[2]
#получение слова для подсчёта частоты
word = sys.argv[3]
#создание новой директории
try:
    os.mkdir(path + new_dir_name)
except:
    print("Такая директория уже есть")

#получение списка файлов
list_of_file = os.listdir(path)
#убираем из списка фалов директории
list_of_audio = [x for x in list_of_file if os.path.isfile(path + x)]
#получаем только файлы с расширением wav
list_of_audio = [x for x in list_of_audio if os.path.splitext(path + x)[1] == '.wav']
#цикл для перебора всех аудиофайлов
for audio_name in list_of_audio:
    #подсчитываем частоту
    frequency = counting_frequency_of_word_in_text(word, recognition_text(path + audio_name))
    #округляем до четырёх знаков после точки
    frequency = round(frequency, 4)
    #выводим на экран подсчитанную частоту у текущего аудио файла
    print(audio_name + "  --  " + str(frequency))
    #копируем аудиофайл с новым именем в директорию
    shutil.copyfile(path + audio_name, path + new_dir_name + audio_name + "_frequency-" + str(frequency))
