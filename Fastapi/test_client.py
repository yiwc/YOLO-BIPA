
import requests
import json
import time
import cv2
import base64
from pydantic import BaseModel
from PIL import Image
import numpy as np

img = cv2.imread(r'predictions.jpg')
img = cv2.resize(img, (128, 128))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# data=[1,2,3,4,5]
# data=np.frombuffer(data,dtype=np.uint8)
# print(data)
# data= data.tobytes()
data = base64.b64encode(img)  # img 转 bytes
data_str = data.decode()      # bytes 转 string
print(data_str)
print(type(data_str))
params={
    "data": data_str

}


url='http://127.0.0.1:8000/img'

time1=time.time()
html = requests.post(url, json.dumps(params))
print('发送post数据请求成功!')
print('返回post结果如下：')
print(html.text)
time2=time.time()
print('总共耗时：' + str(time2 - time1) + 's')
print(type(html.text))
