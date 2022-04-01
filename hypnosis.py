import sounddevice as sd
import soundfile as sf
import sys
from scipy.io.wavfile import write

def instructions():
    print("Music selection:")
    print("1 - Flowing Stream")
    print("2 - Lake noises")

def play_song(selection,repeats):
    filename1 = "music/Flowing-Stream-1.wav"
    filename2 = "music/St-Marys-Loch.wav"
    filename = ""
    if(selection == 1):
        filename = filename1
    elif(selection == 2):
        filename = filename2
    else:
        print("Currently unavailble")
        sys.exit
    data, fs = sf.read(filename, dtype='float32') 
    count = 0

    while(count < repeats):
        sd.play(data, fs)
        sd.wait()
        count+=1

    print("End of track")

def record():
    fs = 44100
    seconds = 3
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write('output.wav', fs, myrecording)
    
if __name__ == '__main__':
    instructions()
    selection = input("Input selection: ")
    repeats = input("Amount of repeats: ")
    try:
        play_song(int(selection),int(repeats))
    
    except:
        print("Incorrect input caused error:"+e)
        sys.exit