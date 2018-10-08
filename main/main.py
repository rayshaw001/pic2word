# encoding:utf-8
from pic2word import pic2word
import sys
import json
import winclipboard
locatioin='../res/Capture.JPG'
result=pic2word(locatioin).decode('utf-8').encode(sys.getfilesystemencoding())
result_str=''
for res in json.loads(result)["words_result"]:
    result_str+=res["words"]

print(result_str)
winclipboard.empty_clipboard()
winclipboard.set_clipboard(result_str)