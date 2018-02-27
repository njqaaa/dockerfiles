FROM njqaaa/alpine-base:3.7

MAINTAINER hy2900822@126.com

ENV JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=162 \
    JAVA_VERSION_BUILD=12 \
    JAVA_PACKAGE=jdk \
    JAVA_SHA1=0da788060d494f5095bf8624735fa2f1 \
    ES_VERSION=6.2.2 \
    PACKAGE_DIR=/usr/local/src/

RUN mkdir ${PACKAGE_DIR} \
    && cd ${PACKAGE_DIR} \
    && curl -OL "http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_SHA1}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz" -H 'Cookie: oraclelicense=accept-securebackup-cookie' \
    && curl -OL "https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz"
