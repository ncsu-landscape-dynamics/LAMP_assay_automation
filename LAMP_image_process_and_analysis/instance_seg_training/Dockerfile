# syntax=docker/dockerfile:1

FROM python:3.9.7-bullseye

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "train_instance_seg.py" ]