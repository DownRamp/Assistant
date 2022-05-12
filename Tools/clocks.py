import time
import datetime
import tkinter as tk
from tkinter import *
import beepy as beep

frequency = 2500
duration = 1000

pomodoro_state = ""
pomodoro_time = ""
day_time = ""

curr = 0
t = 0


class Pomodoro:
    def __init__(self, master):
        global pomodoro_time, pomodoro_state
        pomodoro_time = tk.StringVar()
        pomodoro_state
        self.master = master
        self.frame = tk.Frame(master, padx=20, pady=50)
        self.lbl = Label(master, text="Day time")
        self.lbl.pack()
        self.message = tk.Label(self.frame, textvariable=pomodoro_time)
        self.message.pack()
        self.message_state = tk.Label(self.frame, textvariable=pomodoro_state)
        self.message_state.pack()
        self.frame.pack(expand=True)
        self.startTime(1500, master)
        self.startTime(300, master)

    # get current time
    def startTime(self, t, root):
        global pomodoro_time
        for i in range(t):
            mins = (t - i) // 60
            secs = (t - i) % 60
            timer = 'Pomodoro time {:02d}:{:02d}'.format(mins, secs)
            pomodoro_time.set(timer)
            root.update()
            time.sleep(1)
        pomodoro_time.set("END")
        beep.beep(1)


class Day:
    def __init__(self, master):
        global day_time
        day_time = tk.StringVar()
        self.master = master
        self.frame = tk.Frame(master, padx=20, pady=50)
        self.lbl = Label(master, text="Day time")
        self.lbl.pack()
        self.message = tk.Label(self.frame, textvariable=day_time)
        self.message.pack()
        self.frame.pack(expand=True)
        self.current_time(master)

    def set_current(self):
        global curr
        now = datetime.datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds = (now - midnight).seconds
        curr = 86400 - seconds

    def current_time(self, root):
        self.set_current()
        global curr, day_time
        for i in range(curr):
            curr_hours = (curr-i)//3600
            curr_mins = (curr-i)//60 - (curr_hours*60)
            curr_secs = (curr-i)%60
            curr_timer = 'Time left in day {:02d}:{:02d}:{:02d}'.format(curr_hours, curr_mins, curr_secs)
            day_time.set(curr_timer)
            root.update()
            time.sleep(1)
        day_time.set("END")


class MainWindow():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, padx=20, pady=50)
        self.lbl = Label(master, text="Time selection")
        self.lbl.pack()
        self.btn1 = Button(master, text="Start Pomodoro", command=self.command1)
        self.btn1.pack()
        self.btn2 = Button(master, text="Start Day", command=self.command2)
        self.btn2.pack()
        self.frame.pack(expand=True)

    def command1(self):
        self.newWindow = tk.Toplevel(self.master)
        Pomodoro(self.newWindow)

    def command2(self):
        self.newWindow = tk.Toplevel(self.master)
        Day(self.newWindow)


def main():
    root = Tk()
    root.title("Times")
    root.geometry("350x100")
    win = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.title("Times")
    root.geometry("350x100")
    win = MainWindow(root)
    root.mainloop()
