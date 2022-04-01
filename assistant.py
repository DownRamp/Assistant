import logging
from pathlib import Path
from tkinter import *
from tkinter import ttk

# if data present then greet else create
def initialize():
    logging.debug("Intitializing")
    file = "filing_system/boss.txt"
    my_file = Path(file)
    if my_file.exists():
        f = open(file, "r")
        return(f.read())
    else:
        boss = input("Please enter your name: ")
        f = open(file, "w")
        f.write(boss)
        return boss

def main(person):
    greeting = "Hello "+person

    # Day's events
    listEvents = check_events()

    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text=greeting).grid(column=0, row=0)
    ttk.Button(frm, text="Add an event", command=lambda:add_event()).grid(column=0, row=2)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
    list_items = StringVar(value=listEvents)
    ttk.Listbox(frm, listvariable = list_items, height = len(listEvents))

    root.mainloop()

def add_event():
    logging.debug("Event created")
    create_google_event()

def check_events():
    logging.debug("Events checked")
    file = "filing_system/events.txt"
    my_file = Path(file)
    if my_file.exists():
        f = open(file, "r")
        return f.read().split(',')
    else:
        return []

def send_emails():
    logging.debug("Emails sent")

def create_google_event():
    logging.debug("Google calendar event created")

def cleaning_schedule():
    logging.debug("Cleaning time")

def find_file():
    logging.debug("Looking for file")

# Put into store folder, then input new location
def store():
    logging.debug("Storing file")

if __name__ == "__main__":
    boss = initialize()
    main(boss)
