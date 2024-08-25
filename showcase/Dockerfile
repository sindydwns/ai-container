FROM python:3.12-alpine3.20

RUN apk update
RUN apk add git vim sudo curl gcc make dumb-init

RUN pip install --upgrade pip
RUN pip install gradio

WORKDIR /app
COPY . .

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["gradio", "srcs/main.py"]
