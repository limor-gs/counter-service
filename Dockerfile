FROM python:3.6
ADD counter-service.py config.py /opt/app/
WORKDIR /opt/app
RUN pip3 install flask redis
CMD ["python", "/opt/app/counter-service.py"]
