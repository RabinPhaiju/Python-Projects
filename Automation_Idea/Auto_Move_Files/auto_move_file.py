from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time
import datetime


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        x_date_time = datetime.datetime.now()
        current_date_time = str(x_date_time.now())
        current_date_time = current_date_time.split('.')[0]
        current_date_time = current_date_time.split(' ')
        current_date_time = str(current_date_time[0]) + "_" + str(current_date_time[1]) + "_"
        current_date_time = current_date_time.replace(':', "-")

        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            file_extension = os.path.splitext(filename)[-1][1:]
            if not os.path.isdir(folder_destination + '/' + file_extension):
                os.mkdir(folder_destination + '/' + file_extension)
            destination = folder_destination + '/' + file_extension + '/' + current_date_time + filename
            print('test')
            os.rename(src, destination)


folder_to_track = "Automation_Idea/Auto_Move_Files/test_folder"
folder_destination = "Automation_Idea/Auto_Move_Files/new_folder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

