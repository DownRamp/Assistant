#!/usr/bin/env python

import glob
import pyttsx3
from tkinter import *
import PyPDF2
import threading

# https://www.samuelthomasdavies.com/book-summaries/

stop_flag = False
book_selection = ""


class EbookToAudio:

    # to test later
    # pick a book
    @staticmethod
    def pick_book(root):
        frame = Frame(root)
        list_events = glob.glob("/Books/*")
        list_items = StringVar(value=list_events)
        listing = Listbox(frame, listvariable=list_items, height=len(list_events))
        listing.pack()
        Button(frame, text="Select", command=lambda: EbookToAudio.selection(root, listing.get(listing.curselection())))
        frame.pack()

    @staticmethod
    def selection(main, book):
        global book_selection
        book_selection = book
        main.quit()

    # turn pdf to readable
    @staticmethod
    def pdf_to_read(book):
        file = open(book, 'rb')
        file_reader = PyPDF2.PdfFileReader(file)
        return file_reader

    # turn pdf to readable
    @staticmethod
    def txt_to_read(book):
        file = open(book, "r")
        words = file.read().splitlines()
        file.close()
        return words

    # save point to read from
    @staticmethod
    def save_point(file, i):
        # stop reading
        f = open(file, "w")
        f.write(i)
        f.close()

    @staticmethod
    def stop(self):
        global stop_flag
        stop_flag = True

    @staticmethod
    def fetch_bookmark(filename):
        try:
            with open(filename) as f:
                return f.read()
        except IOError:
            return ''

    @staticmethod
    def window(root):
        frame = Frame(root)
        label = Label(text="Read a book")
        label.pack()
        book = Button(root, text="Pick a book", command=lambda: EbookToAudio.pick_book(Toplevel(root)))
        book.pack()
        start = Button(root, text="Start", command=lambda: threading.Thread(target=EbookToAudio.main))
        start.pack()
        stop = Button(root, text="Stop", command=lambda: threading.Thread(target=EbookToAudio.stop))
        stop.pack()
        frame.pack()

    # main
    @staticmethod
    def main():
        global book_selection, stop_flag
        stop_flag = False
        # take book name and grab txt file with bookmark
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        # I like this one more (7)
        engine.setProperty('voice', voices[7].id)
        engine.say("Hello Reader!")
        engine.runAndWait()
        # for picking book feature later
        # book = pick_book()
        book = f"/books/{book_selection}"
        # fetch any saved points
        bookmark_file = f"/bookmarks/{book_selection}"
        bookmark = EbookToAudio.fetch_bookmark(bookmark_file)
        if bookmark == '':
            bookmark_value = 0
        else:
            bookmark_value = int(bookmark)
        if ".txt" in book_selection:
            file_reader = EbookToAudio.txt_to_read(book_selection)
            for i in range(bookmark_value, len(file_reader)):
                if not stop_flag:
                    engine.say(file_reader[i])
                    engine.runAndWait()
                else:
                    EbookToAudio.save_point(bookmark_file, i)
        else:
            file_reader = EbookToAudio.pdf_to_read(book)
            # start reading from point
            for i in range(bookmark_value, file_reader.numPages):
                engine.say(file_reader.pages[i].extractText())
                engine.runAndWait()
                action = input("Turn page?(y/n)")
                if action == "n":
                    EbookToAudio.save_point(bookmark_file, i)
        engine.stop()


if __name__ == '__main__':
    root = Tk()
    root.title("Audio from ebook")
    root.geometry("350x200")
    EbookToAudio.window(root)
    root.mainloop()

