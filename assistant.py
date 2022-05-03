import logging
from pathlib import Path
from tkinter import *
from pysondb import db
from datetime import date

from Assistant.tools import affirmation, clocks, cold_storage, daily_check, password_gen, email_sender, reader
    # hypnosis, chat


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
    def update_event():
        print()

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
        # Filter through each one and pick relevent data
        # Day
        # Week
        # Month
        # Quarter
        logging.debug("Events checked")
        chores.append(db.getDb("Chores/daily.json").getAll())
        chores.append(db.getDb("Chores/weekly.json").getAll())
        chores.append(db.getDb("Chores/monthly.json").getAll())
        chores.append(db.getDb("Chores/quarterly.json").getAll())
        chores.append(db.getDb("Chores/yearly.json").getAll())
        return chores

    @staticmethod
    def send_email():
        email_sender.email()

    @staticmethod
    def create_google_event():
        logging.debug("Google calendar event created")

    @staticmethod
    def fetch_google_event():
        logging.debug("Google calendar event created")

    @staticmethod
    def ebook_reader():
        audio = reader.EbookToAudio()
        audio.main()

    @staticmethod
    def main(root, person):
        greeting = "Hello " + person

        # Day's events
        list_events = Assistant.check_events()
        print(list_events)
        frm = Frame(root)
        frm.grid()

        Label(frm, text=greeting).grid(column=1, row=0)
        Button(frm, text="Add events", command=lambda: Assistant.add_event(Toplevel(root))).grid(column=0, row=2)
        Button(frm, text="Update events", command=lambda: Assistant.update_event(Toplevel(root))).grid(column=1, row=2)
        Button(frm, text="Add To-Do list", command=lambda: daily_check.add_todo(Toplevel(root))).grid(column=2, row=2)
        Button(frm, text="Update To-Do list", command=lambda: daily_check.update_todo(Toplevel(root))).grid(column=3, row=2)
        Button(frm, text="Clocks", command=lambda: clocks.MainWindow(Toplevel(root))).grid(column=0, row=3)
        Button(frm, text="Password generator", command=lambda: password_gen.password(Toplevel(root))).grid(column=1, row=3)
        Button(frm, text="Reader", command=lambda: Assistant.ebook_reader(Toplevel(root))).grid(column=2, row=3)
        # Button(frm, text="Hypnosis", command=lambda: hypnosis.main(Toplevel(root))).grid(column=0, row=4)
        Button(frm, text="Search", command=lambda: cold_storage.search(Toplevel(root))).grid(column=1, row=4)
        # Button(frm, text="Talk to HR", command=lambda: chat.main(Toplevel(root))).grid(column=2, row=4)

        Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
        list_items = StringVar(value=list_events)
        Listbox(frm, listvariable=list_items, height=len(list_events)).grid(column=1, row=7)
        root.mainloop()


if __name__ == "__main__":
    # start day
    affirmation.affirm()
    root = Tk()
    root.title("Assistant")
    root.geometry("600x400")
    # Daily check-in
    daily_check.day_plan(Toplevel(root))
    # start assistant
    assistant = Assistant()
    # Boss name check
    boss = assistant.initialize()
    # Run cold storage check
    cold_storage.freezer()
    # Start main functions
    assistant.main(root, boss)
