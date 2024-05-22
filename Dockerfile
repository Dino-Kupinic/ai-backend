FROM python:3.12

ARG PORT
ENV PORT $PORT

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /app/src

CMD fastapi run src/main.py --port $PORT
