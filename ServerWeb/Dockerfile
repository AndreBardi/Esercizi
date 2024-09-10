FROM python:3.10-alpine
ADD server.py .

RUN mkdir templates
ADD ./templates/index.html ./templates

RUN pip install flask

CMD ["python","./server.py"]