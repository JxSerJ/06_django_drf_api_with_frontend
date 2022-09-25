FROM python:3.10-slim

WORKDIR /src

RUN apt update && apt install mc nmap -y  # for debug

ENV PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.2.1

RUN pip install -U pip setuptools
RUN pip install "poetry==$POETRY_VERSION"
#RUN pip install Django djangorestframework Pillow drf-spectacular django-cors-headers  \
#    python-dotenv phonenumbers django-phonenumber-field djoser gunicorn psycopg2-binary


COPY poetry.lock pyproject.toml /src/
RUN POETRY_VIRTUALENVS_CREATE=false poetry install -vv

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "skymarket.wsgi:application"]
