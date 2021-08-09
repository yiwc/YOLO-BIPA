FROM nvidia/cuda:11.2.0-base-ubuntu18.04

MAINTAINER GuoSheng<Gs1997XX@163.com>

## ENV Build

RUN apt -y update \
    && apt-get update \
    && apt install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa

RUN apt install -y python3.8 python3-pip python-pip vim git cmake

RUN apt-get install -y libsm6 libxrender1 libfontconfig1 && apt-get install -y libxrender-dev && apt-get install -y ffmpeg

RUN exec bash && echo 'export PYTHONPATH="/usr/local/lib/python3.6/dist-packages:/usr/local/lib/python2.7/dist-packages:$PYTHONPATH"' >> ~/.bashrc && . ~/.bashrc

## ENV Build


WORKDIR /root/Downloads/YOLO-BIPA

COPY src ./src

COPY BS3_yolo_client.py .

COPY BS3_yolo_server.py .

COPY requirements.txt .


## Dependencies Install

WORKDIR /root/Downloads/YOLO-BIPA

RUN pip install --upgrade pip && pip3 install --upgrade pip

RUN pip3 install -r requirements.txt 

## Dependencies Install


WORKDIR /root/Downloads/YOLO-BIPA/src/yolov4/darknet/backup

RUN cd /root/Downloads/YOLO-BIPA/src/yolov4/darknet/backup && gdown https://drive.google.com/uc?id=1MfC8k49viHghsfqM3jxqcgAMlTKlliGe

WORKDIR /root/Downloads/YOLO-BIPA/src/yolov4/darknet/build/darknet/x64

RUN cd /root/Downloads/YOLO-BIPA/src/yolov4/darknet/build/darknet/x64 && gdown https://drive.google.com/uc?id=1V1U7MVe8xlvkpVQ3g8AwXsnrgLj357rT


EXPOSE 8081

ENTRYPOINT ["python3","/root/Downloads/YOLO-BIPA/BS3_yolo_server.py"]
