FROM python:slim

WORKDIR /opt/app
COPY . /opt/app
RUN pip install bottle

EXPOSE 8080

CMD ["python", "app.py"]