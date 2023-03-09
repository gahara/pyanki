FROM python:3.8.5

RUN mkdir /code

COPY requirements.txt /code
COPY .flaskenv /code

RUN pip install -r /code/requirements.txt

COPY . /code
WORKDIR /code

CMD ["gunicorn", "-b", ":5000", "--log-level=info ", "pyanki:app"]