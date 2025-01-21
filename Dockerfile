FROM python:3.12.0

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy the rest of the project
COPY . /code/