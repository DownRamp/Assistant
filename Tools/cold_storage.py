import os
import gzip
from datetime import datetime, timedelta
import shutil
import pysondb as db


def start_search(name):
    listOfFiles = search("/Boss")
    for file in listOfFiles:
        if name in file:
            return file
    else:
        # check cold
        with gzip.open('/Boss/cold.txt.gz', 'rb') as f:
            file_content = f.read()
            for file in file_content:
                if name in file:
                    thaw(file)
                    return file


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
        if last_access < week_time:
            # move to cold storage folder and gzip
            if os.path.exists("Filing_System/Freezer.zip"):
                shutil.unpack_archive("Filing_System/Freezer.zip")
            # save path location on file for putting back
            cold = db.getDb("Filing_System/cold.json")
            cold.add({"path": file})
            shutil.move(file, "Filing_System/Freezer"+os.path.basename(file))
            shutil.make_archive("Filing_System/Freezer", 'zip', "Filing_System/Freezer")


def thaw(name):
    # Grab requested file
    # get file path
    # return to path and move back to path
    print()


if __name__ == '__main__':
    freezer()
