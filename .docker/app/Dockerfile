###########
# BUILDER #
###########

FROM python:3.11 as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

FROM python:3.11

RUN mkdir -p /home/app
RUN addgroup --system app && adduser --system --group app

ENV APP_HOME=/home/app
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/migrations
RUN mkdir $APP_HOME/tests
RUN mkdir $APP_HOME/locale
WORKDIR $APP_HOME

# COPY ./migrations/ $APP_HOME/migrations
# COPY ./tests/ $APP_HOME/tests
# COPY ./locale/ $APP_HOME/locale

RUN apt-get update
RUN apt install -y netcat-traditional && apt-get -y install gettext
COPY --from=builder /usr/src/app/wheels /wheels
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY ./.docker/app/entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

COPY ./app/ $APP_HOME
RUN chown -R app:app $APP_HOME
USER app

ENTRYPOINT ["/home/app/entrypoint.sh"]


