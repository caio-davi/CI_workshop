FROM python:3.6-slim-stretch

ADD requirements.txt requirements.txt

# RUN dpkg-reconfigure locales && \
#    locale-gen C.UTF-8 && \
#    /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

WORKDIR /src
COPY . .
ENV FLASK_APP /src/app.py
ENV FLASK_ENV development
EXPOSE 5000

# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

CMD ["bash"]