FROM python:3.9
WORKDIR /classEmo
COPY ./requirements.txt /classEmo/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /classEmo/requirements.txt

COPY ./app /classEmo/app
COPY ./model /classEmo/model

ENV PYTHONPATH "${PYTHONPATH}:/classEmo"

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]