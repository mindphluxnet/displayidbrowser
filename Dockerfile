FROM python:3.10-alpine
RUN mkdir /app
RUN mkdir /app/templates
RUN mkdir /app/static
WORKDIR /app
ADD requirements.txt /app
ADD application.py /app
ADD static/ /app/static
ADD templates/ /app/templates
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "./application.py"]