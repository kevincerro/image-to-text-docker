FROM python:3.8-alpine

RUN apk update && apk add --no-cache python3-dev gcc libc-dev musl-dev linux-headers

RUN mkdir /usr/src/app
WORKDIR /usr/src/app/

COPY ./app1/requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

COPY ./app1 /usr/src/app/

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASH_ENV=development
ENV FLASK_DEBUG=True
ENV IS_DOCKER=True

EXPOSE 5000

CMD ["flask", "run"]