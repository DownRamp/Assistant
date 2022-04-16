import logging
from pathlib import Path
from tkinter import *
from tkinter import ttk
from pysondb import db
from datetime import date
import os
import email
import clocks
import clothing
import cold_storage
import date_night
import investing
import password_gen
import therapy
import hypnosis
import workout
import ebook_audiobook


class Assistant:
    # if data present then greet else create
    @staticmethod
    def initialize():
        logging.debug("initializing")
        file = "filing_system/boss.json"
        my_file = Path(file)
        if my_file.exists():
            b = db.getDb("filing_system/boss.json")
            return b.getAll()[0]["name"]
        else:
            boss = input("Please enter your name: ")
            b = db.getDb("filing_system/boss.json")
            b.add({"name": boss})
            return boss

    @staticmethod
    def check_events():
        logging.debug("Cleaning Schedule")
        events = db.getDb("Events/events.json")
        return events.getAll()

    @staticmethod
    def add_event(action):
        today = date.today()
        day = today.strftime("%b-%d-%Y")

        logging.debug("Event created")
        events = db.getDb("Events/events.json")
        events.add({"name": action, "time": day})

    @staticmethod
    def check_chores():
        chores = []
        logging.debug("Events checked")
        chores.append(db.getDb("Chores/daily.json").getAll())
        chores.append(db.getDb("Chores/weekly.json").getAll())
        chores.append(db.getDb("Chores/monthly.json").getAll())
        chores.append(db.getDb("Chores/quarterly.json").getAll())
        chores.append(db.getDb("Chores/yearly.json").getAll())
        return chores

    @staticmethod
    def send_email():
        email.email()

    @staticmethod
    def create_google_event():
        logging.debug("Google calendar event created")


    @staticmethod
    def fetch_google_event():
        logging.debug("Google calendar event created")


    @staticmethod
    def find_file(name, path):
        logging.debug("Looking for file")
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

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
