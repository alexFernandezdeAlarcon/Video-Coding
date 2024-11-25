
FROM python:3.9

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    ffmpeg && \
    apt-get clean


COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
