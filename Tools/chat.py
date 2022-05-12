import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from Tkinter import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "Chats/chat.txt"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "HR"

def window():
    window = Tk()

    messages = Text(window)
    messages.pack()

    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)

    # initial
    input_get = "Let's chat"
    messages.insert(INSERT, '%s\n' % input_get)
    input_user.set('')

    def Enter_pressed(event):
        input_get = input_field.get()
        messages.insert(INSERT, '%s\n' % input_get)
        # label = Label(window, text=input_get)
        input_user.set('')
        hr = main(sentence)
        messages.insert(INSERT, '%s\n' % hr)
        input_user.set('')

        # label.pack()
        return "break"

    frame = Frame(window)  # , width=300, height=300)
    input_field.bind("<Return>", Enter_pressed)
    frame.pack()

    window.mainloop()

def main(sentence):
    # sentence = "do you use credit cards?"
    if sentence == "quit":
        return ""

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        return(f"{bot_name}: I do not understand...")

if __name__ == '__main__':
    window()
#     main()