FROM python:3.6-slim-stretch

ADD requirements.txt requirements.txt

ADD requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt 

WORKDIR /src
COPY . .
EXPOSE 8888

# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

ENTRYPOINT  ["jupyter-notebook","--ip=0.0.0.0","--allow-root"]
