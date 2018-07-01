FROM alpine:3.7

MAINTAINER hy2900822@126.com

ENV GLIBC_VERSION=2.26-r0 \
    LANG=C.UTF-8 \
    PS1='[\u@\h \W]\$'

RUN set -ex  \
  && apk add --no-cache tzdata \
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
  && apk upgrade --update  \
  && apk add --update libstdc++ curl bash  \
  && for pkg in glibc-${GLIBC_VERSION}; do curl -sSL https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done  \
  && apk add --allow-untrusted /tmp/*.apk  \
  && rm -v /tmp/*.apk  \
  && apk del libstdc++  \
  && rm -rf /tmp/* /var/cache/apk/*
