import os
from datetime import datetime, timedelta
import shutil
import pysondb as db


def start_search(name):
    listOfFiles = search("/Filing_System")
    for file in listOfFiles:
        if name in file:
            return file

    cold = db.getDb("/Filing_System/cold.json")
    cold_list = cold.getAll()
    for item in cold_list:
        if name in item["path"]:
            thaw(item["path"])
            return item["path"]


def search(dirName):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    return listOfFiles


def freezer():
    # Go through files
    files = search("Filing_System")
    week_time = datetime.now() - timedelta(days=7)
    # Grab ones that are older than a week
    for file in files:
        file_stats = os.stat(file)
        last_access = datetime.fromtimestamp(file_stats.st_atime)
        if last_access > week_time:
            # move to cold storage folder and gzip
            if os.path.exists("Filing_System/Freezer.zip"):
                shutil.unpack_archive("Filing_System/Freezer.zip")
            else:
                 os.mkdir("Filing_System/Freezer")
            # save path location on file for putting back
            cold = db.getDb("Filing_System/cold.json")
            cold.add({"path": file})
            shutil.move(file, "Filing_System/Freezer/"+os.path.basename(file))
            shutil.make_archive("Filing_System/Freezer", 'zip', "Filing_System/Freezer")


def thaw(name):
    # Grab requested file
    cold = db.getDb("Filing_System/cold.json")
    cold_list = cold.getAll()
    file = ""
    for item in cold_list:
        if name in item["path"]:
            file = item["path"]
            cold.deleteById(pk=item["id"])
            break

    if os.path.exists("Filing_System/Freezer.zip"):
        shutil.unpack_archive("Filing_System/Freezer.zip")

    # return to path and move back to path
    shutil.move("Filing_System/Freezer"+os.path.basename(file), file)


def window(main):
    frame = Frame(main)
    frame.grid()
    Label(frame, text="Search", font=('Aerial 12')).grid(row=1, column =0)
    ent1 = Entry(frame)
    ent1.grid(row=1, column=1)
    Button(frame, text='Enter', width=25, command=lambda: start_search(ent1.get())).grid(row=1, column=2)


if __name__ == '__main__':
    freezer()
