FROM njqaaa/base

MAINTAINER hy2900822@126.com

#version
ENV JDK_DOWNLOAD_NAME 8u131
ENV JDK_VERSION 1.8.0_131
ENV TOMCAT_VERSION 8.5.15

# Install JDK 8
RUN cd /usr/local/src/ \
  && curl -OL "http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-${JDK_DOWNLOAD_NAME}-linux-x64.tar.gz" -H 'Cookie: oraclelicense=accept-securebackup-cookie' \
  && tar -xzvf jdk-${JDK_DOWNLOAD_NAME}-linux-x64.tar.gz \
  && mkdir /usr/local/java \
  && mv jdk${JDK_VERSION} /usr/local/java/jdk1.8.0 \
  && rm -rf jdk-${JDK_DOWNLOAD_NAME}-linux-x64.tar.gz

# Get Tomcat
RUN cd /usr/local/src \
  &&  wget --quiet --no-cookies http://apache.rediris.es/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O tomcat.tar.gz \
  && mkdir /data/ \
  && tar -xzvf tomcat.tar.gz -C /data/ \
  && mv /data/apache-tomcat-${TOMCAT_VERSION} /data/tomcat \
  && rm tomcat.tar.gz \
  && rm -rf /data/tomcat/webapps/* \
  && mkdir /data/tomcat/webapps/ROOT \
  && find /data/tomcat/bin -name \*.bat|xargs rm \
  && rm -rf /usr/local/src/tomcat.tar.gz

# ENV
ENV JAVA_HOME /usr/local/java/jdk1.8.0
ENV CATALINA_HOME /data/tomcat
ENV PATH $PATH:$CATALINA_HOME/bin

WORKDIR /data/tomcat

CMD ["/data/tomcat/bin/catalina.sh", "run"]

