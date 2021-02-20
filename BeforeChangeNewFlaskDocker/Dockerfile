# sudo -i
# sudo chmod 666 /var/run/docker.sock
# docker login --username jt75611
# cd /home/jerry/develop/createRecipeWebpage
# docker build -t test .
# docker run --rm -ti test bash -c 'which python && python --version && which pip && pip --version'

#docker run -ti --rm \
#   -e DISPLAY=$DISPLAY \
#   -v /tmp/.X11-unix:/tmp/.X11-unix \
#   main

# push to dockerhub

# docker build --tag createrecipewebpage .
# docker tag createrecipewebpage:latest jt75611/createrecipewebpage:latest
# docker push  jt75611/createrecipewebpage:latest


FROM python:3.8

ARG appPath=./createRecipeWebpage/

COPY main.py ${appPath}main.py
COPY globalUtils.py ${appPath}globalUtils.py
COPY requirements.txt ${appPath}requirements.txt

RUN : \
    && apt-get update \
    && pip install Pillow \
    && pip install python-resize-image \
    && pip install matplotlib \
    && mkdir -p etc/sudoers.d \

#    && pip install -r ${appPath}requirements.txt \
#    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
#        software-properties-common \
#    && add-apt-repository -y ppa:deadsnakes \
#    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \

    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/* \
    && :
#ENV DISPLAY :0
#RUN python3.8 -m venv /venv
#ENV PATH=/venv/bin:$PATH
#RUN python createRecipeWebpage/main.py


RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
#    mkdir -p /etc/sudoers && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer

CMD ["python", "./createRecipeWebpage/main.py", "-flag"]


##__EOF__
#XSOCK=/tmp/.X11-unix
#XAUTH=/tmp/.docker.xauth
#xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -
#docker run -ti -v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH main.py

#FROM ubuntu:14.04
#
#RUN apt-get update && apt-get install -y firefox

# Replace 1000 with your user / group id
#RUN export uid=1000 gid=1000 && \
#    mkdir -p /home/developer && \
#    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
#    echo "developer:x:${uid}:" >> /etc/group && \
#    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
#    chmod 0440 /etc/sudoers.d/developer && \
#    chown ${uid}:${gid} -R /home/developer
#
#USER developer
#ENV HOME /home/developer
#CMD /usr/bin/firefox





#xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f /tmp/.docker.xauth nmerge - && docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth -e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=$DISPLAY xeyes





