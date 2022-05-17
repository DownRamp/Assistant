import logging
from pathlib import Path
import tkinter
from pysondb import db
from datetime import date
from datetime import datetime
import customtkinter
import filemanager

from Tools import events, affirmation, clocks, cold_storage, daily_check, password_gen, email_sender, reader
    # hypnosis, chat

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


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
        logging.debug("Events Schedule")
        events = db.getDb("Events/events.json")
        event_list = events.getAll()
        build_list = []
        for item in event_list:
            build_list.append(item["name"] + " " + item["time"])
        return build_list

    @staticmethod
    def check_daily():
        events = db.getDb("ToDo/daily.json")
        event_list = events.getAll()
        build_list = []
        for item in event_list:
            build_list.append(f'{item["task"]}, {item["quad"]}')
        return build_list

    @staticmethod
    def check_chores():
        chores = []
        logging.debug("Events checked")

        for i in db.getDb("Chores/daily.json").getAll():
            chores.append(i["name"])

        for i in db.getDb("Chores/weekly.json").getAll():
            if i["time"] == datetime.today().weekday():
                chores.append(i["name"])

        for i in db.getDb("Chores/monthly.json").getAll():
            week = datetime.now().day / 7
            if i["time"] == week:
                chores.append(i["name"])

        for i in db.getDb("Chores/quarterly.json").getAll():
            quarter = datetime.now().month % 3
            if i["time"] == quarter:
                chores.append(i["name"])

        for i in db.getDb("Chores/yearly.json").getAll():
            quarter = datetime.now().month / 3
            if i["time"] == week:
                chores.append(i["name"])

        return chores

    @staticmethod
    def send_email():
        email_sender.email()

    @staticmethod
    def ebook_reader(main):
        audio = reader.EbookToAudio()
        audio.window(main)

    @staticmethod
    def main(root, person):
        greeting = "Hello " + person

        # Day's events
        list_events = Assistant.check_events()
        list_daily = Assistant.check_daily()
        list_chores = Assistant.check_chores()

        frm = customtkinter.CTkFrame(master=root, corner_radius=15)
        frm.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        customtkinter.CTkLabel(master=frm, justify=tkinter.LEFT, text=greeting).grid(column=1, row=0, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkButton(master=frm, text="Add events", command=lambda: events.add_event(tkinter.Toplevel(root))).grid(column=0, row=2, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkButton(master=frm, text="Update events", command=lambda: events.update_event(tkinter.Toplevel(root))).grid(column=1, row=2, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkButton(master=frm, text="Add To-Do list", command=lambda: daily_check.add_todo(tkinter.Toplevel(root))).grid(column=2, row=2, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkButton(master=frm, text="Update To-Do list", command=lambda: daily_check.update_todo(tkinter.Toplevel(root))).grid(column=3, row=2, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkButton(master=frm, text="Clocks", command=lambda: clocks.MainWindow(tkinter.Toplevel(root))).grid(column=0, row=3, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkButton(master=frm, text="Password generator", command=lambda: password_gen.main(tkinter.Toplevel(root))).grid(column=1, row=3, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkButton(master=frm, text="Reader", command=lambda: Assistant.ebook_reader(tkinter.Toplevel(root))).grid(column=2, row=3, padx=20, pady=20, sticky="nsew")
        # customtkinter.CTkButton(master=frm, text="Hypnosis", command=lambda: hypnosis.main(tkinter.Toplevel(root))).grid(column=0, row=4, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkButton(master=frm, text="Search", command=lambda: cold_storage.window(tkinter.Toplevel(root))).grid(column=1, row=4, padx=20, pady=20, sticky="nsew")
        # customtkinter.CTkButton(master=frm, text="Talk to HR", command=lambda: chat.main(tkinter.Toplevel(root))).grid(column=2, row=4, padx=20, pady=20, sticky="nsew")


        customtkinter.CTkButton(master=frm, text="Quit", fg_color=("gray75", "gray30"), command=root.destroy).grid(column=1, row=5, padx=20, pady=20, sticky="nsew")
        customtkinter.CTkLabel(master=frm,
                  text="Upcoming Events",
                  text_font=("Roboto Medium", -16)).grid(column = 0, row = 6)
        list_items = tkinter.StringVar(value=list_events)
        tkinter.Listbox(frm, listvariable=list_items, height=len(list_events)).grid(column=0, row=7, padx=20, pady=20, sticky="nsew")

        customtkinter.CTkLabel(master=frm,
                  text="Today's Chores",
                  text_font=("Roboto Medium", -16)).grid(column = 1, row = 6)
        list_ch = tkinter.StringVar(value=list_chores)
        tkinter.Listbox(frm, listvariable=list_ch, height=len(list_chores)).grid(column=1, row=7, padx=20, pady=20, sticky="nsew")

        customtkinter.CTkLabel(master=frm,
                  text="Daily ToDo",
                  text_font=("Roboto Medium", -16)).grid(column = 2, row = 6)
        list_todo = tkinter.StringVar(value=list_daily)
        tkinter.Listbox(frm, listvariable=list_todo, height=len(list_daily)).grid(column=2, row=7, padx=20, pady=20, sticky="nsew")
        root.mainloop()

        def change_mode(self):
            if self.switch_2.get() == 1:
                customtkinter.set_appearance_mode("dark")
            else:
                customtkinter.set_appearance_mode("light")

        def on_closing(self, event=0):
            self.destroy()

        def start(self):
            self.mainloop()


if __name__ == "__main__":
    daily_check.delete_plan()
    filemanager.MoverHandler()
    # start day
    # affirmation.affirm()
    root = customtkinter.CTk()
    root.title("Assistant")
    root.geometry("1000x700")
    # Daily check-in
    daily_check.day_plan(tkinter.Toplevel(root))
    # start assistant
    assistant = Assistant()
    # Boss name check
    boss = assistant.initialize()
    # Run cold storage check
    cold_storage.freezer()
    # Start main functions
    assistant.main(root, boss)
