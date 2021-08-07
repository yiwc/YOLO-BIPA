import sys
import os
import cv2

sys.path.append(os.path.join(os.getcwd(), "yolov4"))


from yolov4.mymodel import *
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import base64

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


class Data(BaseModel):
    data: str



class YOLO_SERVER(object):

    def __init__(self, model_name, weight="last"):
        data_root = "/root/Fastapi/yolov4/darknet/data/{}".format(model_name)
        # data_root = "yolov4/darknet/data/{}".format(model_name)
        weight_root = "/root/Fastapi/yolov4/darknet/backup"
        self.cfgfile = os.path.join(data_root, model_name + ".cfg")
        self.weightfile = os.path.join(weight_root, "{}_{}.weights".
                                       format(model_name, weight))
        self.namesfile = os.path.join(data_root, model_name + ".names")
        self.datafile = os.path.join(data_root, model_name + ".data")

        print(3)
        self.m = Darknet(self.cfgfile)
        print(2)
        self.m.print_network()
        print(1)
        self.m.load_weights(self.weightfile)
        print('Loading weights from %s... Done!' % (self.weightfile))

        self.num_classes = self.m.num_classes
        self.class_names = load_class_names(self.namesfile)



        # a little change
        use_cuda = True
        if use_cuda:
            self.m.cuda()
        # change back if necessary



        #### client 向 server发出请求，server收到后回复，执行run函数将训练好的图片发回给client
        #### 摸清楚如何用Fastapi建立server和client之间的通讯，如何指定端口


    def send(self,item: Data):
        # while True:
        message = item.data  # message: string
        # item.name = 'name is gs'
        message_bytes = message.encode()  # message_bytes: bytes
        # img = np.frombuffer(message_bytes, dtype=np.uint8)   # bytes 转 img
        decode_img = base64.b64decode(message_bytes)
        decode_img_img = np.frombuffer(decode_img, dtype=np.uint8)
        img = np.reshape(decode_img_img, (128, 128, 3)).astype(np.uint8)
        boxes = self.gen(img)
        print(boxes)
        boxes_bytes = np.array(boxes).tobytes()  # boxes_bytes:bytes
        print(boxes_bytes)
        boxes_bytes_b64 = base64.b64encode(boxes_bytes)  # base64 bytes

        return boxes_bytes_b64.decode()  # string error:UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 3: invalid start byte

    def gen(self, img):
        assert img.dtype == np.uint8

        # img = cv2.imread(imgfile)
        sized = cv2.resize(img, (self.m.width, self.m.height))
        # sized = cv2.cvtColor(sized, cv2.COLOR_BGR2RGB)
        for i in range(2):
            start = time.time()
            boxes = do_detect(self.m, sized, 0.4, 0.6, use_cuda)

            finish = time.time()
            if i == 1:
                print('Predicted in %f seconds.' % ((finish - start)))
        print("yolo server boxxes=>", boxes)
        return boxes



# global yolo_server
import argparse


args = argparse.ArgumentParser()

# args.add_argument("-n", "--name", default='inss_v1', type=str)
# g = args.parse_args()
# yolo_server = YOLO_SERVER(g.name, weight="final")

args.add_argument("-n", "--name", default='inss_v6', type=str)
g = args.parse_args()
yolo_server = YOLO_SERVER(g.name, weight="last")


@app.post('/yolo/api')
def g(item:Data):
    global yolo_server
    return yolo_server.send(item)

if __name__ == "__main__":


    uvicorn.run(app='BS3_yolo_server:app', host="0.0.0.0", port=8081, reload=False, debug=False)
# 1


# https://fastapi.tiangolo.com/deployment/docker/

# https://stackoverflow.com/questions/63853813/how-to-create-routes-with-fastapi-within-a-class
# [[0.41609588265419006, 0.2797590494155884, 0.5823571681976318, 0.4479617476463318, 0.9808395504951477, 0.9808395504951477, 0.0], [0.4503830671310425, 0.4722556471824646, 0.6178147792816162, 0.6300875544548035, 0.993896484375, 0.993896484375, 1.0]]
