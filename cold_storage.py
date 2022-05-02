import os
import stat
import time
import gzip
import shutil
from pathlib import Path

# with gzip.open('/home/joe/file.txt.gz', 'rb') as f:
#     file_content = f.read()

# content = b"Lots of content here"
# with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
#     f.write(content)


# shutil.make_archive(output_filename, 'zip', dir_name)
def start_search(name):
    listOfFiles = search("/Boss")
    for file in listOfFiles:
        if name in file:
            print()
    else:
        # check cold
        with gzip.open('/Boss/cold.txt.gz', 'rb') as f:
            file_content = f.read()
        print()


def search(dirName):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    return listOfFiles


def freezer():
    print()


def thaw():
    print()


def main():
    # fetch directory files and all recursive files
    # check last use time
        # if last use is older then 2 weeks
        # gzip, store path location, and cold storage
    print()
# def main():
#     filePath = '/Boss/index.html'
#     print("**** Get File Last Access time using os.stat() ****")
#     # get the the stat_result object
#     fileStatsObj = os.stat(filePath)
#     # Get last access time
#     accessTime = time.ctime(fileStatsObj[stat.ST_ATIME])
#     print("File Last Access Time : " + accessTime)
#     print("**** Get File Creation time using os.stat() *******")
#     # get the the stat_result object
#     fileStatsObj = os.stat(filePath)
#     # Get the file creation time
#     creationTime = time.ctime(fileStatsObj[stat.ST_CTIME])
#     print("File Creation Time : " + creationTime)
#     print("**** Get File Last Access time using os.path.getatime() ****")
#     # Get last access time of file in seconds since epoch
#     accessTimesinceEpoc = os.path.getatime(filePath)
#     # convert time sinch epoch to readable format
#     accessTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(accessTimesinceEpoc))
#     print("File Last Access Time : " + accessTime)
#     print("**** Get File Last Access time using os.path.getatime() in UTC Timezone****")
#     accessTime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(accessTimesinceEpoc))
#     print("File Last Access Time : " + accessTime + ' UTC')
#     print("**** Get File creation time using os.path.getctime() ****")
#     # Get file creation time of file in seconds since epoch
#     creationTimesinceEpoc = os.path.getctime(filePath)
#     # convert time sinch epoch to readable format
#     creationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(creationTimesinceEpoc))
#     print("File Creation Time : " + creationTime)
#     print("**** Get File creation time using os.path.getctime() in UTC Timezone ****")
#     creationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(creationTimesinceEpoc))
#     print("File Creation Time : ", creationTime, ' UTC')


if __name__ == '__main__':
    main()
