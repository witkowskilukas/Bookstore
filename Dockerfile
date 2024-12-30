from python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --deploy --system
#RUN pip install --no-cache-dir pipenv && pipenv install --deploy --ignore-pipfile
	
COPY . /code/