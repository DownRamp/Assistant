#!/usr/bin/env python

import glob
import pyttsx3
from tkinter import *
import PyPDF2
import threading
import os
import tkinter.messagebox

# https://www.samuelthomasdavies.com/book-summaries/

stop_flag = False
book_selection = ""


class EbookToAudio:

    # to test later
    # pick a book
    def pick_book(self,root):
        frame = Frame(root)
        frame.grid()
        list_events = glob.glob("Books/*")
        list_items = StringVar(value=list_events)
        listing = Listbox(frame, listvariable=list_items, height=len(list_events))
        listing.grid(row=1)
        Button(frame, text="Select", command=lambda: self.selection(root, listing.get(listing.curselection())))\
            .grid(row=5)

    def selection(self, main, book):
        global book_selection
        book_selection = book
        tkinter.messagebox.showinfo("Selection made", "Selection Made")

    # turn pdf to readable
    def pdf_to_read(self, book):
        file = open(book, 'rb')
        file_reader = PyPDF2.PdfFileReader(file)
        return file_reader

    # turn pdf to readable
    def txt_to_read(self, book):
        file = open(book, "r")
        words = file.read().splitlines()
        file.close()
        return words

    # save point to read from
    def save_point(self, file, i):
        # stop reading
        f = open(file, "w")
        f.write(i)
        f.close()

    def stop(self):
        global stop_flag
        stop_flag = True

    def fetch_bookmark(self, filename):
        try:
            if os.path.exists(filename):
                with open(filename) as f:
                    return f.read()
            return ''
        except IOError:
            return ''

    def window(self, root):
        frame = Frame(root)
        frame.grid()
        Label(frame, text="Read a book").grid(row=1)
        Button(frame, text="Pick a book", command=lambda: self.pick_book(Toplevel(root))).grid(row=3)
        Button(frame, text="Start", command=lambda: self.main()).grid(row=4)
        Button(frame, text="Stop", command=lambda: self.stop()).grid(row=5)

    # main
    def main(self):
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
        # fetch any saved points
        bookmark_file = f"/Bookmarks/{book_selection}"
        bookmark = self.fetch_bookmark(bookmark_file)
        if bookmark == '':
            bookmark_value = 0
        else:
            bookmark_value = int(bookmark)
        if ".txt" in book_selection:
            file_reader = self.txt_to_read(book_selection)
            for i in range(bookmark_value, len(file_reader)):
                if not stop_flag:
                    value = file_reader[i].strip()
                    if value == "":
                        continue
                    engine.say(value)
                    engine.runAndWait()
                else:
                    self.save_point(bookmark_file, i)
            # archive book
            path = book_selection[:6]+"Done/"+book_selection[6:]
            os.rename(book_selection, "path/to/new/destination/for/file.foo")

#         else:
#             file_reader = self.pdf_to_read(book_selection)
#             # start reading from point
#             for i in range(bookmark_value, file_reader.numPages):
#                 engine.say(file_reader.pages[i].extractText())
#                 engine.runAndWait()
#                 action = input("Turn page?(y/n)")
#                 if action == "n":
#                     self.save_point(bookmark_file, i)
        engine.stop()


if __name__ == '__main__':
    root = Tk()
    root.title("Audio from ebook")
    root.geometry("350x200")
    EbookToAudio.window(root)
    root.mainloop()

