
FROM python:3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    rm -rf /var/lib/apt/lists/*


COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]