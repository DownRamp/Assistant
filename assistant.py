import logging
from pathlib import Path
from tkinter import *
from pysondb import db
from datetime import date
import os

import email
import password_gen
import clocks
import affirmation

#os.system("streamlit run investing.py")


class Assistant:
    # if data present then greet else create
    @staticmethod
    def initialize():
        logging.debug("initializing")
        file = "Boss/boss.json"
        my_file = Path(file)
        if my_file.exists():
            b = db.getDb("Boss/boss.json")
            return b.getAll()[0]["name"]
        else:
            boss = input("Please enter your name: ")
            b = db.getDb("Boss/boss.json")
            b.add({"name": boss})
            return boss

    @staticmethod
    def check_events():
        logging.debug("Cleaning Schedule")
        events = db.getDb("Events/events.json")
        event_list = events.getAll()
        build_list = []
        for item in event_list:
            build_list.append(item["name"] + " " + item["time"])
        return build_list

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

    # 4
    @staticmethod
    def clocks():
        clocks.main()

    # 5
    @staticmethod
    def hypnosis():
        print()

    # 6
    @staticmethod
    def ebook_reader():
        print()

    # 9
    @staticmethod
    def password_gen():
        password_gen.password()

    # 10
    @staticmethod
    def therapy():
        print()

    def check_in(self):
        # Show title
        # Show list
        # Add a entry
        # Add button
        print()

    @staticmethod
    def main(person):
        greeting = "Hello " + person

        # Day's events
        list_events = Assistant.check_events()

        root = Tk()
        root.title("Assistant")
        root.geometry("380x120")
        frm = Frame(root)
        frm.grid()
        Label(frm, text=greeting).grid(column=1, row=0)
        Button(frm, text="Update events", command=lambda: Assistant.add_event()).grid(column=0, row=2)
        Button(frm, text="Talk to HR", command=lambda: Assistant.add_event()).grid(column=1, row=2)
        Button(frm, text="Update To-Do list", command=lambda: Assistant.add_event()).grid(column=2, row=2)
        Button(frm, text="Clocks", command=lambda: Assistant.add_event()).grid(column=0, row=3)
        Button(frm, text="Reader", command=lambda: Assistant.add_event()).grid(column=2, row=3)
        Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
        list_items = StringVar(value=list_events)
        Listbox(frm, listvariable=list_items, height=len(list_events))
        root.mainloop()



def daily_check():
    print()


if __name__ == "__main__":
    assistant = Assistant()
    boss = assistant.initialize()
    # Daily check-in

    # affirmations (questions to start the day)
    # affirmation.affirm()
    # 1 (high quality, high work)
    # 2 (low quality, high work)
    # lunch
    # 3 (low quality, low work)
    # 4 (high quality, low work)

    # add cold storage
    assistant.store()

    assistant.main(boss)
