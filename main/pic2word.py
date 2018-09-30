# encoding:utf-8
import urllib, urllib2, base64
import os
import json
from token import getToken

def pic2word(pic_location):
    # getToken key
    key=dict()
    keyFile=open('../res/keys.properties','r')
    for line in keyFile:
        key.update({line.split('=')[0]:line.split('=')[1]})
    access_token=getToken(key["APIKey"].strip('\n'),key["SecretKey"].strip('\n'))
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + json.loads(access_token)['access_token']
    # 二进制方式打开图文件
    f = open(pic_location, 'rb')
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.urlencode(params)
    request = urllib2.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        return content
    return 
