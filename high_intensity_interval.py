#!/usr/bin/env python
import time
import vlc
import sounddevice as sd
import soundfile as sf
import threading

def explain():
    print("HIIT training (High intensity interval training, is a condensed form of workout\n")
    print("It is recommended to do it 2-3 times a week")
    print("According to google it will burn more calories then cardio")
    print("Follow along with the timer and the music")

exercise_list= ["Jog in place", "Mountain climbers", "Burpees no jumping", "High side plank raise", 
"Russian twists", "Switch lunges", "Side-to-side pushups", "Jumping jacks", "In and outs", "Side-to-side jump squats"]

filename1 = "music/hyp.mp3"
filename2 = "music/relax.mp3"
filename3 = "music/cooldown.mp3"

pos1 = 0
pos2 = 0
def video(source, ticker, type):
    global pos1, pos2
    pos = 0
    if type == 1:
        pos = pos1
    else:
        pos = pos2
    vlc_instance = vlc.Instance()
     
    player = vlc_instance.media_player_new()
     
    media = vlc_instance.media_new(source)
     
    player.set_media(media)
    player.set_position(pos)
    player.play()
    for i in range(ticker): 
        time.sleep(1)
    player.stop()
    if type == 1:
        pos1 = player.get_position()
    else:
        pos2 = player.get_position()

def startTime(t, action):
    print(action)
    secs = t
    if action == "rest":
        print("BREATH")
        threading.Thread(target=video, args =(filename2,t))
    else:
        threading.Thread(target=video, args = (filename1,t))
        print("Good job!")

    while t:
        timer = '{:02d}'.format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t -=1
    print("End of time")

def workout(username):
# set intervals
    print(f"Welcome {username}")
    stretch = input("Would you like to stretch first?(y/n)")
    if stretch == "y":
        print()
    print("Let's begin. Goodluck!")
    exercise = 1
    while(exercise < len(exercise_list)):
        startTime(45, "workout")
        startTime(15, "rest")
        exercise +=1

def cooldown(username):
    print()

if __name__ == "__main__":
    explain()
    username = input("What's your name?")
    workout(username)
    # cooldown / guided meditation
    cool = input("Would you like to do a cooldown?(y/n)")
    if cool == "y":
        cooldown(username)
    print("Great workout. Let's make today a great day")