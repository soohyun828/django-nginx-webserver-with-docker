FROM python:3.10.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
RUN pip3 install django
COPY . /code/

#RUN python manage.py migrate

#EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]