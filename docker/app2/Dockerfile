FROM python:3.8-alpine

RUN apk update && apk add --no-cache python3-dev gcc libc-dev musl-dev linux-headers tesseract-ocr tesseract-ocr-data-spa zlib-dev jpeg-dev

WORKDIR /var/www

COPY ./app2/requirements.txt /var/www/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /var/www/requirements.txt

COPY ./app2 /var/www

EXPOSE 5050

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]