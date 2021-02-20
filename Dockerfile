# sudo chmod 666 /var/run/docker.sock
# docker login --username jt75611
# cd /home/jerry/develop/createRecipeWebpage

# push to dockerhub
# docker build --tag createrecipewebpage .
# docker tag createrecipewebpage:latest jt75611/createrecipewebpage:latest
# docker push  jt75611/createrecipewebpage:latest


FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "demo.py" ]
