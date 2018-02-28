FROM debian:stretch-slim

MAINTAINER hy2900822@126.com

ARG DEBIAN_FRONTEND=noninteractive

ENV KIBANA_VERSION=6.2.2 \
    KIBANA_PATH=/opt/kibana/

COPY clean-apt /usr/bin
COPY clean-install /usr/bin

RUN clean-install curl

RUN cd /tmp \
    && mkdir -p ${KIBANA_PATH} \
    && curl -OLk "http://artifacts.elastic.co/downloads/kibana/kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz" \
    && tar -xzf kibana-${KIBANA_VERSION}-linux-x86_64.tar.gz \
    && mv kibana-${KIBANA_VERSION}-linux-x86_64/* ${KIBANA_PATH} \
    && rm -rf /tmp/*

CMD ["/opt/kibana/bin/kibana"]
