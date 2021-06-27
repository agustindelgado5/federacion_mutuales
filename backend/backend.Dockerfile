FROM python:3.9-buster


ENV PYTHONUNBUFFERED=1


WORKDIR /usr/src/backend


COPY requirements.txt .


RUN pip install  --no-cache-dir -r requirements.txt


EXPOSE 8002


ENTRYPOINT [ "/usr/src/backend/docker-entrypoint.sh" ]