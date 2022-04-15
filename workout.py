#!/usr/bin/env python
import time
import threading
from pygame import mixer
import pyttsx3

# spotify api


def explain():
    print("HIIT training (High intensity interval training, is a condensed form of workout\n")
    print("It is recommended to do it 2-3 times a week\n")
    print("According to google it will burn more calories then cardio\n")
    print("Follow along with the timer and the music\n")


exercise_list = []
cooldown_list = []
stretch_list = []

filename1 = "music/hyp.mp3"
filename2 = "music/relax.mp3"
filename3 = "music/cooldown.mp3"

workout1 = "workouts/workout.txt"
workout2 = "workouts/stretch.txt"
workout3 = "workouts/cooldown.txt"

query = ""
signal1 = ["p1", "s1", "q1"]
signal2 = ["p2", "s2", "q2"]


def fetch_workout():
    global exercise_list, stretch_list, cooldown_list
    exercises = open(workout1, "r")
    for exercise in exercises:
        exercise.strip()
        exercise_list.append(exercise)

    stretches = open(workout2, "r")
    for stretch in stretches:
        stretch.strip()
        stretch_list.append(stretch)

    cooldownies = open(workout3, "r")
    for cooldown in cooldownies:
        cooldown.strip()
        cooldown_list.append(cooldown)


def video(source, signals):
    global query

    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load(source)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()

    # infinite loop
    while True:

        if query == signals[0]:

            # Pausing the music
            mixer.music.pause()
        elif query == signals[1]:

            # Resuming the music
            mixer.music.unpause()
        elif query == signals[2]:

            # Stop the mixer
            mixer.music.stop()
            break


def start_time(t, action):
    global query, signal1, signal2
    if action == "rest":
        query = "s2"
    else:
        query = "s1"
    while t:
        timer = '{:02d}'.format(t)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    if action == "rest":
        query = "p2"
    else:
        query = "p1"


def extra(username, action, engine):
    line = ""
    action_list = []
    if action == "cooldown":
        line = f"Let us relax {username}"
        action_list = cooldown_list
    else:
        line = f"Let us loosen up {username}"
        action_list = stretch_list
    engine.say(line)
    engine.runAndWait()
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load(filename3)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()
    t = 60

    for action in action_list:
        print(f"Current exercise: {action}")
        while t:
            timer = '{:02d}'.format(t)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    mixer.music.stop()


def workout(username, engine):
    global query, signal1, signal2
    # set intervals
    stretch_val = input("Would you like to stretch first?(y/n)")
    # stretch
    if stretch_val == "y":
        extra(username, "stretch", engine)
    engine.say(f"Let us begin. Good luck!")
    engine.runAndWait()
    # workout
    workout_time = input("Enter a workout time:")
    rest_time = input("Enter a rest time")

    threading.Thread(target=video, args=(filename1, signal1))
    query = "p1"
    threading.Thread(target=video, args=(filename2, signal2))
    query = "p2"

    for exercise in exercise_list:
        print(f"Current exercise: {exercise}")
        start_time(workout_time, "workout")
        start_time(rest_time, "rest")

    # cooldown / guided meditation
    engine.say(f"You did great {username}. Good Job!")
    engine.runAndWait()
    cool = input("Would you like to do a cooldown?(y/n)")
    if cool == "y":
        extra(username, "cooldown", engine)
    engine.say(f"Great workout {username}. Let us make today a great day")
    engine.runAndWait()
    query = "q1"
    query = "q2"


if __name__ == "__main__":
    explain()
    username = input("What's your name? ")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # change to 0 for male voice. I like this one more (turn to 7 on macs)
    engine.setProperty('voice', voices[1].id)
    # engine.setProperty('voice', voices[7].id)

    engine.say(f"Hello {username} lets have a great workout")
    engine.runAndWait()
    fetch_workout()
    workout(username, engine)
    engine.stop()

