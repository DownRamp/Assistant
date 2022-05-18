import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv
load_dotenv()

source_dir = os.environ.get("source")
dest_dir_sfx = os.environ.get("sfx")
dest_dir_music = os.environ.get("music")
dest_dir_video = os.environ.get("video")
dest_dir_image = os.environ.get("image")
dest_dir_pdf = os.environ.get("pdf")
dest_dir_zip = os.environ.get("zip")
dest_dir_excel = os.environ.get("excel")

## ADD MORE TYPES

def makeUnique(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    ## IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path

def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry,dest)

#class MoverHandler(FileSystemEventHandler):
class MoverHandler:
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.wav') or name.endswith('.mp3'):
                    if entry.stat().st_size < 25000000 or "SFX" in name:
                        dest = dest_dir_sfx
                    else:
                        dest = dest_dir_music
                    move(dest, entry, name)
                elif name.endswith('.mov') or name.endswith('.mp4'):
                    dest = dest_dir_video
                    move(dest, entry, name)
                elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png'):
                    dest = dest_dir_image
                    move(dest, entry, name)
                elif name.endswith('.pdf') or name.endswith('.txt') or name.endswith('.doc'):
                    dest = dest_dir_pdf
                    move(dest, entry, name)
                elif name.endswith('.zip') or name.endswith('.tar') or name.endswith('.7zip'):
                    dest = dest_dir_zip
                    move(dest, entry, name)
                elif name.endswith('.xlsx'):
                    dest = dest_dir_excel
                    move(dest, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()

    #observer = Observer()
    #observer.schedule(event_handler, path, recursive=True)
    #observer.start()
    #try:
    #    while True:
    #        time.sleep(10)
    #except KeyboardInterrupt:
    #    observer.stop()
    #observer.join()