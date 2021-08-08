# from enum import Enum
# from fastapi import FastAPI
#
#
# class Hjx_Class_name(str, Enum):
#     Name = 'huangjunx'
#     Year = 18
#     Id = '20153201072'
#     student = True
#
#
# app = FastAPI()
#
#
# @app.get('/hjx/{hjx_man}')
# def root(hjx_man: Hjx_Class_name):
#     return {'status': hjx_man}

# from enum import Enum
#
# from fastapi import FastAPI
#
#
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
#
# app = FastAPI()
#
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}

import json
from PIL import Image
import numpy as np
import cv2
import base64
import httpx

img = cv2.imread(r'predictions.jpg')
img = cv2.resize(img, (128, 128))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img)

# img_b=img.tobytes()  # img 转 bytes
# print(img_b)
#
# img_b_s=img_b.decode() # bytes 转string
# print(img_b_s)


#
# assert img.dtype == np.uint8
#
# data = base64.b64encode(img)  # img 转 bytes
# data_str = data.decode()  # bytes 转 string
# params = {
#     "data": data_str  # string
#
# }
# print(type(params))
# url = 'http://127.0.0.1:8000/img/yolo'
# print(json.dumps(params))
# html = httpx.post(url, data=params)
# print(html.text)
# print(type(html.text))




# data = img.tobytes()
# print(data)

# img 转 byte
encode_img=base64.b64encode(img)
print(encode_img)           # bytes   b'e4B5dnt0dHt0dXt3cnt4b3h3bXd4b3l6b3h3cXp5dH59d4GAd4OBdoKAcoCAc39/d3yCcnd7dnx6foV9hIZ7lJKDysK17+
print(encode_img.decode())  # string  e4B5dnt0dHt0dXt3cnt4b3h3bXd4b3l6b3h3cXp5dH59d4GAd4OBdoKAcoCAc39/
print(type(encode_img))
print(img.tobytes())    # bytes

print(str(img.tobytes()))  # string
print(type(str(img.tobytes())))   # string

img_ss=str(img.tobytes())
img_ss_b=img_ss.encode()
print(img_ss_b)
print(type(img_ss_b))
print(1)


# # bytes 转 img
print('bytes to img')
print(encode_img)     # base64 bytes
decode_img=base64.b64decode(encode_img)
print(decode_img)     # bytes
decode_img_encode=base64.b64encode(decode_img)
print(decode_img_encode)
print(decode_img_encode.decode())

decode_img_img=np.frombuffer(decode_img,dtype=np.uint8)
print(decode_img_img)
img = np.reshape(decode_img_img, (128, 128, 3)).astype(np.uint8)
print(img)


# with open("D:\\redis.png", 'rb') as f:
#     encode_img = base64.b64encode(f.read())
#     file_ext = os.path.splitext("D:\\redis.png")[1]
#     print('data:image/{};base64,{}'.format(file_ext[1:], encode_img.decode()))
#     f.close()
# # 解码
# with open("D:\\redis2.png", 'wb') as f:
#     f.write(base64.b64decode(encode_img))
#     f.close()

# byte 转 string
encode_img_decode=encode_img.decode()
print(encode_img_decode)               # e4B5dnt0dHt0dXt3cnt4b3h3bXd4b3l6b3h3cXp
# print(encode_img)
print(type(encode_img_decode))         # string

#string 转 byte
encode_img_decode_encode=encode_img_decode.encode()
print(encode_img_decode_encode)        # b'e4B5dnt0dHt0dXt3cnt4b3h3bXd4b3l6b3h3c
print(type(encode_img_decode_encode))  # bytes

# string 转 img
# nparr=np.fromstring(encode_img_decode,np.uint8)
# img_restore=cv2.imdecode(nparr,cv2.IMREAD_COLOR)
# print(img_restore)
# print(1)

# string 转 numpy array
# img_data=base64.b64decode(encode_img_decode_encode)
# nparr=np.fromstring(img_data,np.uint8)
# img_np=cv2.imdecode(nparr,cv2.IMREAD_COLOR)
# print(img_np)


# # bytes 转 img
# with open("D:\\redis.png", 'rb') as f:
#     encode_img = base64.b64encode(f.read())
#     file_ext = os.path.splitext("D:\\redis.png")[1]
#     print('data:image/{};base64,{}'.format(file_ext[1:], encode_img.decode()))
#     f.close()
# # 解码
# with open("D:\\redis2.png", 'wb') as f:
#     f.write(base64.b64decode(encode_img))
#     f.close()




# byte 转 img
# img_new = np.frombuffer(encode_img_decode_encode, dtype=np.uint8)
# print(img_new)
# print(type(img_new))
#
# encode_img_decode_encode_img=base64.b64decode(encode_img_decode_encode)
# print(encode_img_decode_encode_img)
# print(type(encode_img_decode_encode_img))
#
#
# print('#######')
#
# img = cv2.imread('predictions.jpg')
# img_str = cv2.imencode('.jpg', img)[1].tostring()  # 将图片编码成流数据，放到内存缓存中，然后转化成string格式
# print(img_str)
# print(type(img_str))
#
# b64_code = base64.b64encode(img_str)  # 编码成base64
# print(b64_code)
# print(type(b64_code))
#
# # 从base64编码恢复OpenCV图像
# str_decode = base64.b64decode(b64_code)
# # print(str_decode.decode(type=base64))
# # print(type(str_decode.decode(dtype=base64)))
#
# nparr = np.fromstring(str_decode, np.uint8)
# # img_restore = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR) for python 2
# img_restore = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# print(img_restore)
#
# print('#######################')
# img = cv2.imread('giraffe.jpg')
# print(img)
# print(1)
# img_str = cv2.imencode('.jpg', img)[1].tostring()  # 将图片编码成流数据，放到内存缓存中，然后转化成string格式
# b64_code = base64.b64encode(img_str)  # 编码成base64
#
# # 从base64编码恢复OpenCV图像
# str_decode = base64.b64decode(b64_code)
# nparr = np.fromstring(str_decode, np.uint8)
# # img_restore = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR) for python 2
# img_restore = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# print(img_restore)


# # byte 转
# decode_encode_img = base64.decodebytes(encode_img)
# decode_decode_encode_img=decode_encode_img.decode()
# print(decode_decode_encode_img)
# print(type(decode_decode_encode_img))



# encode_img_str_img=base64.decodebytes(encode_img_str)
# print(encode_img_str_img.decode())
# print(type(encode_img_str_img))

# image_dir = r'giraffe.jpg'
#
# x = Image.open(image_dir)  # 打开图片
# data = np.asarray(x)
#
# print(data.shape)
# print(data)

# data.tolist()
# print(data)


# data=data.tostring()
# print(data)
#
# data=data.decode()
# print(data)
# data=np.frombuffer(data,dtype=np.uint8)# data=np.frombuffer(data,dtype=np.uint8)
#
# data=data.tolist()
# print(data)
# print(type(data))
#
# data=np.array(data)
# data.reshape((500,500,3))
# print(data)
# print(type(data))
#



# data=np.array(data)
#
# print(data)



# data = data.tobytes()
# print(data)
#
# ndarray = cv2.imdecode(np.frombuffer(data, np.uint8))
# print(ndarray)


#
# data=np.asarray(data)
# print(data)
# data = {
#     'name' : 'myname',
#     'age' : 100,
# }
# json_str = json.dumps(data)
# print(json_str)
