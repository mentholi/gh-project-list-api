FROM python:3.8

ENV PYTHONUNBUFFERED=1

ADD requirements.txt requirements.txt
ADD gh_project_list/ /app

RUN pip install -r requirements.txt

WORKDIR /app

CMD python
