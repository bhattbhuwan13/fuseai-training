FROM python:3.6.1-alpine
WORKDIR /project
ADD . /project
RUN apk add --no-cache cython3
RUN pip install -r requirements.txt
CMD ["python api/sentiment_predict.py"]
