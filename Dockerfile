FROM nvidia/cuda:11.2.0-base-ubuntu18.04

MAINTAINER GuoSheng<Gs1997XX@163.com>

RUN apt -y update \
    && apt install -y software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt install -y python3.8

RUN apt install -y python3-pip

RUN apt install -y python-pip

RUN pip3 install fastapi && pip3 install uvicorn[standard]

RUN pip3 install scikit-build

RUN apt install -y vim
  
RUN pip3 install pydantic && pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

#RUN echo 'export PYTHONPATH="/usr/local/lib/python3.6/dist-packages:/usr/local/lib/#python2.7/dist-packages:$PYTHONPATH"' >> ~/.zshrc && . ~/.zshrc

RUN apt install -y git && pip install gdown

WORKDIR /root/Downloads

RUN cd /root/Downloads && git clone https://github.com/yiwc/YOLO-BIPA.git

WORKDIR /root/Downloads/YOLO-BIPA/Fastapi/yolov4/darknet/backup

RUN cd /root/Downloads/YOLO-BIPA/Fastapi/yolov4/darknet/backup && gdown https://drive.google.com/uc?id=1MfC8k49viHghsfqM3jxqcgAMlTKlliGe

WORKDIR /root/Downloads/YOLO-BIPA/Fastapi/yolov4/darknet/build/darknet/x64

RUN cd /root/Downloads/YOLO-BIPA/Fastapi/yolov4/darknet/build/darknet/x64 && gdown https://drive.google.com/uc?id=1V1U7MVe8xlvkpVQ3g8AwXsnrgLj357rT

RUN apt-get update 

RUN apt-get install -y cmake

RUN pip install --upgrade pip && pip3 install --upgrade pip && apt-get install -y libsm6 libxrender1 libfontconfig1 && apt-get install -y libxrender-dev && apt-get install -y ffmpeg

RUN exec bash && echo 'export PYTHONPATH="/usr/local/lib/python3.6/dist-packages:/usr/local/lib/python2.7/dist-packages:$PYTHONPATH"' >> ~/.bashrc && . ~/.bashrc

RUN pip install opencv-python && pip install numpy

EXPOSE 8081

ENTRYPOINT ["python3","/root/Downloads/YOLO-BIPA/Fastapi/BS3_yolo_server.py"]
## change the python path in mymodel.py file

#### log

#pip install --upgrade pip

#apt-get install libsm6 libxrender1 libfontconfig1

#apt-get install -y libxrender-dev


#echo 'export PYTHONPATH="/usr/local/lib/python3.6/dist-packages:/usr/local/lib/python2.7/#dist-packages:$PYTHONPATH"' >> ~/.bashrc && . ~/.bashrc

#pip install opencv-python

#pip install numpy

#RUN apt-get update
#RUN apt-get install -y ffmpeg

#/root/Downloads/YOLO-BIPA/Fastapi/yolov4/mymodel.py





















































































































































































































































































































































































































































































































































