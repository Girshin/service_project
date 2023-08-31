FROM python:latest
WORKDIR /app
COPY service_progect.py /app
RUN pip install flask

EXPOSE 5000
CMD ["python", "service_progect.py"]
