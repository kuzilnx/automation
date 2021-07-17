FROM python:3.7
#created by: Kuzilnx
ENV PYTHONUNBUFFERED 1
WORKDIR /opt
COPY . /opt/
RUN pip3 install --requirement requirements.txt
EXPOSE 5090
CMD ["python", "app.py"]
