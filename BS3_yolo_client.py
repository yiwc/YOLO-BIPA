# import zmq
import numpy as np
import requests
import json
import base64
# import httpx


class YOLO_CLIENT():
    def __init__(self):
        pass
        # ip="localhost" if self.dgx==False else "172.16.127.89"
        # self.context = zmq.Context()
        # self.skt = self.context.socket(zmq.REQ)
        # self.skt.connect("tcp://{}:{}".format(ip,self.pt))
        ###
        # params = {
        #     "data": data
        #
        # }
        # url = 'http://127.0.0.1:8000/img'
        ###

    ## 未执行
    def gen(self, img):
        # assert img.dtype==np.uint8
        #
        # self.skt.send(img.tobytes())
        # message = self.skt.recv()
        # boxes=np.frombuffer(message,dtype=np.float).reshape(-1,7).tolist()
        # # print("yolo client get boxes=>",boxes)
        # return boxes

        ###
        assert img.dtype == np.uint8

        data = base64.b64encode(img)  # img 转 bytes
        data_str = data.decode()  # bytes 转 string
        name= 'name'
        params = {
            "data": data_str  # string

        }
        #print(params)
        #print(type(params))
        url = 'http://127.0.0.1:8081/yolo/api/'
        html = requests.post(url, json.dumps(params))
        # html = httpx.post(url,data=params)
        #print(html.text)
        #print(type(html.text))  # string
        ######
        html_text_byte_b64 = html.text.encode()  # base64 bytes
        #print(html_text_byte_b64)
        #print(base64.b64decode(html_text_byte_b64))
        html_text_byte = base64.b64decode(html_text_byte_b64)  # bytes
        #print(html_text_byte)
        boxes = np.frombuffer(html_text_byte, dtype=np.float64).reshape(-1, 7).tolist() # array

        return boxes
        #######
        # return html.text
        # print(html_text_byte)
        # boxes = np.frombuffer(html_text_byte, dtype=np.float).reshape(-1, 7).tolist()
        # # print("yolo client get boxes=>",boxes)
        # return boxes


if __name__ == "__main__":
    a = YOLO_CLIENT()

    img = np.random.randint(0, 255, [128, 128, 3]).astype(np.uint8)
    import cv2

    # img = cv2.imread("yolov4_1/testbolt4.png")
    img = cv2.imread(r'predictions.jpg')
    img = cv2.resize(img, (128, 128))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(a.gen(img))
    pass
