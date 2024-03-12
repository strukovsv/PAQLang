FROM python:3.11

ENV PYTHONPATH="/app"
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
  && apt-get install -y --no-install-recommends python3-pip unzip libaio1 locales tzdata \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/* \
  && ln -snf "/usr/share/zoneinfo/$TZ" /etc/localtime \
  && echo "$TZ" > /etc/timezone \
  && sed -i -e 's/# \(en_US\.UTF-8 .*\)/\1/' /etc/locale.gen  \
  && locale-gen

ENV LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8

COPY instantclient-basic-linux.x64-19.6.0.0.0dbru.zip /tmp/

WORKDIR /opt/oracle

RUN unzip /tmp/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip \
  && rm /tmp/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip \
  && echo /opt/oracle/instantclient_19_6 >/etc/ld.so.conf.d/oracle-instantclient.conf \
  && ldconfig

# Перейти в рабочий директорий
WORKDIR /tests
WORKDIR /app

# Установить зависимости
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir --upgrade pip \
  && pip install --verbose --no-cache-dir -r requirements.txt

# Скопировать выполняемый код
COPY ./src/. ./

CMD ["python", "-m", "main"]

