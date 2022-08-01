#FROM
FROM python:3.8.13

#switch script spaces
WORKDIR /usr/src/app
COPY . .

#安装依赖
# RUN python -m pip install -r tracking-server-requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python -m pip install -r tracking-server-requirements.txt

# entrypoint
ENTRYPOINT ["/bin/sh","start-tracking-server.sh"]