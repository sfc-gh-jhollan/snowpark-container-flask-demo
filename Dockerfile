FROM python:3.10
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

CMD [ "python", "-m", "flask", "--app", "api", "run", "--host=0.0.0.0" ]