#coding=utf-8
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from pic2word import pic2word
import sys
import json
import os
import clipboard

class FileCreatedHandler(FileSystemEventHandler):
    filePath=''
    def on_created(self,event):
        locatioin=event.src_path
        if locatioin.endswith('.jpg') or locatioin.endswith('.JPG') or locatioin.endswith('.png') or locatioin.endswith('.PNG'):
            result=pic2word(locatioin)
            result_str=u"".encode("UTF-8")
            for res in json.loads(result)["words_result"]:
                result_str+=res["words"]
            clipboard.copy(result_str)

if __name__=="__main__":
    key=dict()
    settings=open('../res/settings.properties','r')
    for line in settings:
        key.update({line.split('=')[0]:line.split('=')[1]})
    settings.close()
    path=os.getcwd()+'/'+key["location"].strip('\n')
    event_handler = FileCreatedHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()