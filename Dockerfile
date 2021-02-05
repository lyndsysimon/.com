FROM python:3.9-alpine AS builder

RUN apk add --update --no-cache make

RUN mkdir /src
WORKDIR /src

COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY src .

RUN make html


FROM nginx:1.19-alpine

RUN mkdir /etc/nginx/templates
COPY templates /etc/nginx/templates

COPY --from=builder /src/output /usr/share/nginx/html
