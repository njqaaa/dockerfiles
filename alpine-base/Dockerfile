FROM alpine:3.6

MAINTAINER hy2900822@126.com

ENV GLIBC_VERSION=2.25-r0 \
    LANG=C.UTF-8

RUN set -ex  \
  && apk upgrade --update  \
  && apk add --update libstdc++ curl ca-certificates bash  \
  && for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done  \
  && apk add --allow-untrusted /tmp/*.apk  \
  && rm -v /tmp/*.apk  \
  && ( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true )  \
  && echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh  \
  && /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib  \
  && apk del curl glibc-i18n  \
  && rm -rf /tmp/* /var/cache/apk/*  \
  && echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf
