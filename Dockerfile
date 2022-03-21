FROM python:3

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./boot-dev.sh boot-dev.sh
RUN chmod u+x ./boot-dev.sh
CMD ["./boot-dev.sh"]
