import speech_recognition as sr
import os

# command2mp3 = "ffmpeg -i racecar.mp4 racecar.mp3"
# command2wav = "ffmpeg -i racecar.mp3 racecar.wav"
#
# os.system(command2mp3)
# os.system(command2wav)

r = sr.Recognizer()
audio = sr.AudioFile('racecar.wav')
f = open("demofile2.txt", "a+")

# Read in video
with audio as source:
    value = r.record(source, duration=100)
    r.recognize_google(value, key=None, language="en-US", show_all=False)
    f.write("Now the file has more content!")

f.close()
    # print(r.recognize_google(audio))
# Create subtitles
# Save to file
