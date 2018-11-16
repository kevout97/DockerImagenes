FROM python:3

RUN apt-get update -y && apt-get upgrade -y &&\
    pip install virtualenv

RUN virtualenv --python=python3 /usr/src/proyects-django

WORKDIR /usr/src/proyects-django

RUN /bin/bash -c "source bin/activate"

RUN /bin/bash -c "pip install django==2.0.5"

RUN /bin/bash -c "django-admin startproject example"

EXPOSE 8000

CMD ["python", "/usr/src/proyects-django/example/manage.py", "runserver", "0.0.0.0:8000"]
