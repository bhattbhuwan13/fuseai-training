FROM tiangolo/uwsgi-nginx-flask:python3.6
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
RUN python nltk_downloader.py
WORKDIR /project
#CMD ["python"]
CMD python api/sentiment_predict.py
