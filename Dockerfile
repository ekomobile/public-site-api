FROM python:3.8-alpine
WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apk update --no-cache \
    && apk add musl-dev zlib postgresql-dev libjpeg-turbo-dev libpng-dev libwebp-dev gcc\
    #&& apk add --no-cache --virtual .build-deps \
    && python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir
    #&& apk --purge del .build-deps

COPY . .
RUN chmod +x entrypoint.sh

EXPOSE 8000
EXPOSE 5432
EXPOSE 6379

ENTRYPOINT ["/api/entrypoint.sh"]
