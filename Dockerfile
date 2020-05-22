FROM tiangolo/uwsgi-nginx-flask:python3.6
WORKDIR /project
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD . /project
RUN python nltk_downloader.py
WORKDIR /project
#CMD ["python"]
#CMD python api/sentiment_predict.py
