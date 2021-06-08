FROM python:3.8.10-alpine3.13

ENV FLASK_APP application.py
COPY ./ /tmp/
WORKDIR /tmp/
RUN apk add curl
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
