#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:50:26 2022

@author: honepa
"""
from frequency_word import recognition_text, counting_frequency_of_word_in_text
from tkinter import Tk, messagebox, ttk, StringVar, Entry, Button
#функция вывода ответа и запуска скрипта обработки аудио
def show_answer():
    try:
        #распознавание текста из аудио
        text = recognition_text(path_to_audio.get())
        #генерация строки ответа
        answer = "Частота слова -" + word.get() + "- в распозанном тесте ="  + str(counting_frequency_of_word_in_text(word.get(), text))
        #вызов окна с выводом ответа
        messagebox.showinfo("Answer", answer)
    except Exception as e:
        #вызов окна с выводом ошибки
        messagebox.showinfo("Exception", str(e))
#иницилизая модуля ткинтера
root = Tk()
#задаём заголовок приложения
root.title("Frequency of word in text")
#задаем размер окна приложения
root.geometry("350x250")
#инициализируем переменные для вводимого слова и путя до файла с аудио
word = StringVar()
path_to_audio = StringVar()
#пишем слова рядом с блоком ввода текста
ttk.Label(root, text="Search word").place(relx=.10, rely=.1)
ttk.Label(root, text="Path to audio file").place(relx=.10, rely=.2)
#создаём блоки для ввода текста
word_entry = Entry(textvariable=word)
path_to_audio_entry = Entry(textvariable=path_to_audio)
#задаём положения блокам текста
word_entry.place(relx=.5, rely=.1)
path_to_audio_entry.place(relx=.5, rely=.2)
#инициализируем и задаём положения кнопка получения ответа и выхода
answer_button = Button(text="Get Answer", command=show_answer)
answer_button.place(relx=.10, rely=.5)
quit_button = Button(text="Quit", command=root.destroy)
quit_button.place(relx=.6, rely=.5)

#запускаем приложение
root.mainloop()