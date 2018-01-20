FROM ubuntu:17.10

MAINTAINER zhanghai <zhanghhd@163.com>

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN bash ./install.sh
RUN pip install pipenv -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 
RUN pipenv install 

CMD ["python", "robot.py"]

