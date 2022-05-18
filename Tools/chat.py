import random
import json

import torch

from Tools.model import NeuralNet
from Tools.nltk_utils import bag_of_words, tokenize
import tkinter as tk
from tkinter import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('Tools/intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "Tools/Chats/chat.txt"
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

class window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.frm = tk.Frame(root)
        self.frm.pack()
        self.messages = Text(self.root)
        self.messages.pack()

        self.input_user = StringVar()
        self.input_field = Entry(self.root, text=self.input_user)
        self.input_field.pack(side=BOTTOM, fill=X)

        # initial
        self.input_get = "Let's chat"
        self.messages.insert(INSERT, '%s\n' % self.input_get)
        self.input_user.set('')
        self.input_field.bind("<Return>", self.Enter_pressed)

    def Enter_pressed(self, event):
        self.input_get = self.input_field.get()
        self.messages.insert(INSERT, '%s\n' % self.input_get)
        # label = Label(root, text=input_get)
        self.input_user.set('')
        self.hr = self.main(self.input_get)
        self.messages.insert(INSERT, '%s\n' % self.hr)
        self.input_user.set('')

        # label.pack()
        return "break"

    def main(self, sentence):
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
    root = Tk()
    root.title("Times")
    root.geometry("1000x700")
    window(root)
    root.mainloop()

#     main()