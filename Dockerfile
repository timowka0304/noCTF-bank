FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /app
RUN python3 main.py

CMD ["./run.sh"]
