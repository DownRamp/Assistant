#!/usr/bin/env python

import glob
import pyttsx3
import tkinter as tk
from tkinter import *
import PyPDF2
from os.path import exists

# https://www.samuelthomasdavies.com/book-summaries/

class EbookToAudio:

    # to test later
    # pick a book
    @staticmethod
    def pick_book():
        for name in glob.glob("/books/*.pdf"):
            print(name)
            select = "Would you like to read this book?(y/n)"
            if select == "y":
                return name

    # turn pdf to readable
    @staticmethod
    def pdf_to_read(book):
        file = open(book, 'rb')
        file_reader = PyPDF2.PdfFileReader(file)
        return file_reader

    # save point to read from
    @staticmethod
    def save_point(file, i):
        # stop reading
        f = open(file, "w")
        f.write(i)
        f.close()

    @staticmethod
    def fetch_bookmark(filename):
        try:
            with open(filename) as f:
                return f.read()
        except IOError:
            return ''

    # main
    @staticmethod
    def main(engine):
        # for picking book feature later
        # book = pick_book()
        book = "/books/book.pdf"
        book_name = "book"
        # fetch any saved points
        bookmark_file = f"/bookmarks/{book_name}.txt"
        bookmark = EbookToAudio.fetch_bookmark(bookmark_file)
        if bookmark == '':
            bookmark_value = 0
        else:
            bookmark_value = int(bookmark)
        file_reader = EbookToAudio.pdf_to_read(book)

        # start reading from point
        for i in range(bookmark_value, file_reader.numPages):
            engine.say(file_reader.pages[i].extractText())
            engine.runAndWait()
            action = input("Turn page?(y/n)")
            if action == "n":
                EbookToAudio.save_point(bookmark_file, i)

    if __name__ == '__main__':
        root = Tk()
        # take book name and grab txt file with bookmark
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        # I like this one more (7)
        engine.setProperty('voice', voices[7].id)
        engine.say("Hello Reader!")
        engine.runAndWait()
        root.title("Audio from ebook")

        root.geometry("350x100")
        label = Label(text="Read a book")
        label.pack()
        start = Button(root, text="Start", command=main(engine))
        start.pack()
        stop = Button(root, text="Stop", command=save_point)
        stop.pack()
        root.mainloop()
        engine.stop()

