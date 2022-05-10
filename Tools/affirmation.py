import pyttsx3
import time

# Ask a series of questions
questions = ["Why are you working so hard?",
             "What is your dream?",
             "What are you grateful for?",
             "How will you work towards your goals today?",
             "How are you proud of yourself?",
             "Will you be proud of yourself?"]


def affirm():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # I like this one more (7)
    engine.setProperty('voice', voices[17].id)
    engine.say("Good Morning!")
    engine.runAndWait()
    for i in questions:
        engine.say(i)
        engine.runAndWait()
        time.sleep(5)
    engine.say("Make it a great day")
    engine.runAndWait()
    engine.stop()


if __name__ == '__main__':
    affirm()
