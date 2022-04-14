import logging
from pathlib import Path
from tkinter import *
from tkinter import ttk


class Assistant:
    # if data present then greet else create
    @staticmethod
    def initialize():
        logging.debug("initializing")
        file = "filing_system/boss.txt"
        my_file = Path(file)
        if my_file.exists():
            f = open(file, "r")
            return f.read()
        else:
            boss = input("Please enter your name: ")
            f = open(file, "w")
            f.write(boss)
            return boss

    @staticmethod
    def add_event(action):
        logging.debug("Event created")
        file = "filing_system/events.txt"
        my_file = Path(file)
        if my_file.exists():
            f = open(file, "a")
            f.write(action)
        else:
            return []

    @staticmethod
    def check_chores():
        chores = []
        logging.debug("Events checked")
        file = "Chores/daily.txt"
        my_file = Path(file)
        if my_file.exists():
            f = open(file, "r")
            f.read().split(',')
        file = "Chores/weekly.txt"
        my_file = Path(file)
        if my_file.exists():
            f = open(file, "r")
            f.read().split(',')
        file = "Chores/monthly.txt"
        my_file = Path(file)
        if my_file.exists():
            f = open(file, "r")
            f.read().split(',')
        file = "Chores/quarterly.txt"
        my_file = Path(file)
        if my_file.exists():
            f = open(file, "r")
            f.read().split(',')
        file = "Chores/yearly.txt"
        my_file = Path(file)
        if my_file.exists():
            f = open(file, "r")
            f.read().split(',')

    @staticmethod
    def create_google_event():
        logging.debug("Google calendar event created")

    @staticmethod
    def fetch_google_event():
        logging.debug("Google calendar event created")

    @staticmethod
    def check_events():
        logging.debug("Cleaning Schedule")
        file = "filing_system/events.txt"
        my_file = Path(file)
        if my_file.exists():
            f = open(file, "r")
            return f.read().split(',')
        else:
            return []

    @staticmethod
    def find_file():
        logging.debug("Looking for file")

    # Additional features

    # 1
    # Put into store folder, then input new location
    @staticmethod
    def store():
        # cold storage chapter
        logging.debug("Storing file")

    # 2
    @staticmethod
    def clothing():
        print()

    # 3
    @staticmethod
    def workout():
        print()

    # 4
    @staticmethod
    def clocks():
        print()

    # 5
    @staticmethod
    def hypnosis():
        print()

    # 6
    @staticmethod
    def ebook_reader():
        print()

    # 7
    @staticmethod
    def date_night():
        print()

    # 8
    @staticmethod
    def investing():
        print()

    # 9
    @staticmethod
    def password_gen():
        print()

    # 10
    @staticmethod
    def therapy():
        print()

    @staticmethod
    def main(person):
        greeting = "Hello "+person
    
        # Day's events
        list_events = Assistant.check_events()
    
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        ttk.Label(frm, text=greeting).grid(column=0, row=0)
        ttk.Button(frm, text="Add an event", command=lambda: Assistant.add_event()).grid(column=0, row=2)
    
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
        list_items = StringVar(value=list_events)
        ttk.Listbox(frm, listvariable=list_items, height=len(list_events))
    
        root.mainloop()

    if __name__ == "__main__":
        boss = initialize()

        # add cold storage

        main(boss)
