#coding=utf-8
import time
from pic2word import picture2words
import json
import clipboard
from PIL import ImageGrab as ig;
from PIL import Image as image; 
import cStringIO

if __name__=="__main__":
    key=dict()
    settings=open('../res/settings.properties','r')
    for line in settings:
        key.update({line.split('=')[0]:line.split('=')[1]})
    settings.close()

    try:
        while True:
            picture=ig.grabclipboard()
            if image.isImageType(picture):
                buffer = cStringIO.StringIO()
                picture.save(buffer, format="JPEG")
                result=picture2words(buffer.getvalue())
                result_str=u"".encode("UTF-8")
                print(result)
                for res in json.loads(result)["words_result"]:
                    result_str+=res["words"]
                print(result_str)
                clipboard.copy(result_str)
            time.sleep(1)
    except KeyboardInterrupt:
        exit()
