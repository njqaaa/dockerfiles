FROM alpine:3.8
MAINTAINER <hy2900822@126.com>

ENV \
    GLIBC_VERSION="2.29-r0" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8" \
    TIMEZONE="Asia/Shanghai"

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/' /etc/apk/repositories

RUN set -ex \
    && apk update \
    && apk upgrade \
    && apk add --no-cache \
           bash \
           tzdata \
           tini \
           curl \
           ca-certificates \
           libstdc++ \
    && curl -o /etc/apk/keys/sgerrand.rsa.pub "https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub" \
    && for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done \
    && apk add --allow-untrusted /tmp/*.apk \
    && ( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true ) \
    && /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 "$LANG" || true  \
    && /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 C.UTF-8 || true  \
    && echo "export LANG=$LANG" > /etc/profile.d/locale.sh \
    && /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib \
    && echo "${TIMEZONE}" > /etc/TZ \
    && ln -sf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
    && rm -v /tmp/* \
    && echo "${TIMEZONE}" > /etc/TZ \
    && ln -sf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
    && echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf \
    && find /usr/share/zoneinfo/ -type d -name Asia | xargs rm -rf \
    && find /usr/share/zoneinfo/ -type f ! -name Shanghai | xargs rm \
    && find /usr/glibc-compat/share/i18n -type f  ! -name UTF-8.gz ! -name GB2312.gz ! -name en_US | xargs rm \
    && cat /dev/null > /lib/apk/db/installed \
    && rm -rf /usr/share/terminfo \
    && mkdir /opt \
    && rm -rf /var/cache/apk/*
