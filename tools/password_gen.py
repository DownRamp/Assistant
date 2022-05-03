import datetime
import random
import array
from pysondb import db
import string
from tkinter import *
from tkinter import messagebox


def gen_string():
    S = 10
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    return str(ran)


def password(pass_len, reason):
    # print("Input length of password: ")
    # pass_len = int(input())
    #
    # print("Input reason for password: ")
    # reason = input()

    # check length
    UCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    'Z']

    LCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z']

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '|', '~', '>',
    '*', '(', ')']

    # number of different characters
    ucase_amount = random.randint(1, pass_len-3)
    lcase_amount = random.randint(1, pass_len-2-ucase_amount)
    digit_amount = random.randint(1, pass_len-1-ucase_amount-lcase_amount)
    symbols_amount = pass_len - ucase_amount-lcase_amount-digit_amount

    temp = ""
    for i in range(ucase_amount):
        temp = temp + random.choice(UCASE)
        temp_list = array.array('u', temp)
        random.shuffle(temp_list)

    for i in range(lcase_amount):
        temp = temp + random.choice(LCASE)
        temp_list = array.array('u', temp)
        random.shuffle(temp_list)

    for i in range(digit_amount):
        temp = temp + random.choice(DIGITS)
        temp_list = array.array('u', temp)
        random.shuffle(temp_list)

    for i in range(symbols_amount):
        temp = temp + random.choice(SYMBOLS)
        temp_list = array.array('u', temp)
        random.shuffle(temp_list)

    password = ""
    for x in temp_list:
        password = password + x
    store(reason, password)


def store(reason, password):
    key = gen_string()
    date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    messagebox.showinfo('Secret', f"Please remember your password: {password}")
    a = db.getDb("../Secrets/password.json")
    b = db.getDb("../Secrets/hash.json")

    encMessage, key = encrypt(password, key)
    a.add({"reason": reason, "date": date, "password": encMessage})
    b.add({"reason": reason, "date": date, "key": key})


def retrieve(reason):
    query = {"reason": reason}
    a = db.getDb("../Secrets/password.json")
    hash = a.getByQuery(query=query)
    b = db.getDb("../Secrets/hash.json")

    key = b.getByQuery(query=query)

    decMessage = decrypt(hash[0]["password"], key[0]["key"])
    print(f"Password: {decMessage}")


def encrypt(password, key):
    l = 1
    encPass = ""
    for i in range(2, 8):
        if (i*i) >len(password):
            l = i
            break

    grid = [["" for i in range(l)] for j in range(l)]
    count = 0
    left = (l*l) - len(password)
    key = key[0:left]
    password = password + key
    for i in range(l):
        for j in range(l):
            grid[i][j] = password[count]
            count += 1

    for i in range(l):
        for j in range(l):
            encPass = encPass + grid[j][i]
    return encPass, key


def decrypt(password, key):
    l = 1
    decPass = ""
    for i in range(2, 8):
        if (i * i) == len(password):
            l = i

    grid = [["" for i in range(l)] for j in range(l)]
    count = 0
    real = (l*l) - len(key)

    for i in range(l):
        for j in range(l):
            grid[i][j] = password[count]
            count += 1

    for i in range(l):
        for j in range(l):
            decPass = decPass+grid[j][i]

    return decPass[0:real]


def main(root):
    lbl1 = Label(root, text="Enter length of password: ")
    lbl1.pack()
    enteryPassLen = Entry(root, width=30)
    enteryPassLen.insert(END, "10")
    enteryPassLen.pack()
    lbl2 = Label(root, text="Enter reason for password: ")
    lbl2.pack()
    enteryReason = Entry(root, width=30)
    enteryReason.pack()
    btn = Button(root, text="Enter", command=lambda: password(int(enteryPassLen.get()), enteryReason.get()))
    btn.pack()
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.title("Times")
    root.geometry("350x200")
    main(root)
    # password(10, "test")
    # retrieve("test")
