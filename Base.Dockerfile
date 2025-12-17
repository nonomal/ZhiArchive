FROM python:3.12-bookworm

COPY ./requirements.txt /opt/zhi-archive/requirements.txt
RUN pip install -r /opt/zhi-archive/requirements.txt

RUN playwright install --with-deps chromium

COPY ./ /opt/zhi-archive
WORKDIR /opt/zhi-archive
