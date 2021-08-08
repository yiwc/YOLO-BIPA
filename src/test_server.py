# from fastapi import FastAPI
#
# # app= FastAPI()
# #
# # @app.get("/")
# # async def root():
# #     return {"message": "Hello World, I am here"}
#
# app = FastAPI()
#
#
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
#
# import uvicorn
# from fastapi import FastAPI
# from PIL import Image
# import numpy as np
#
#
# image_dir = r'~/Documents/Fastapi/giraffe.jpg'

#
# print(data)
#
# app = FastAPI()
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# if __name__ == '__main__':
#     ## server 的 ip 127.0.0.1, 端口8000
#     uvicorn.run(app='test:app', host="127.0.0.1", port=8000, reload=True, debug=True)
import uvicorn
from fastapi import FastAPI
# from f_cao_function import *
from pydantic import BaseModel
# 创建数据模型
import numpy as np

class Data(BaseModel):
    data: str
    # rec: str='receive'

app = FastAPI()


# @app.get("/img")
# async  def root():
#     return 'Hello World!'


@app.post("/img")
async def Send(item: Data):

    if item.data:
        # item.data =np.frombuffer(item.data,dtype=np.uint8)
        item.data ='123'+item.data
        # item.data=np.array(item.data)

        ## update() 将 括号内的键值对添加到item_dict这个字典中
        return item.data
        # return item


if __name__ == '__main__':
    # uvicorn.run(app='test_server:app')
    uvicorn.run(app='test_server:app', host="127.0.0.1", port=8000, reload=True, debug=True)
    # pass