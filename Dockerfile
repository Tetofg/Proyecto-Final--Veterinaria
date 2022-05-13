FROM python:3.9

ENV PYTHONUNBUFFERED 1
RUN mkdir /code 

WORKDIR /code
COPY . /code/

RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN pip install -r requirements.txt


CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "Proyecto_Vet", "Proyecto_Vet.wsgi:application"]