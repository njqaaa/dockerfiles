FROM njqaaa/alpine-java:1.8.0_161

MAINTAINER hy@2900822@126.com

ENV TOMCAT_MAJOR=8 \
    TOMCAT_VERSION=8.5.9 \
    TOMCAT_HOME=/opt/tomcat \
    CATALINA_HOME=/opt/tomcat \
    CATALINA_OUT=/dev/null

RUN mkdir /opt/ \
    && curl -o /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz -OL "http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz" \
    && tar -xzvf /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz -C /opt \
    && rm -rf /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz \
    && ln -s /opt/apache-tomcat-${TOMCAT_VERSION} ${TOMCAT_HOME} \
    && rm -rf ${TOMCAT_HOME}/webapps/* \ 
    && rm -rf ${TOMCAT_HOME}/bin/*\.bat \ 
    && mkdir ${TOMCAT_HOME}/webapps/ROOT \
    && apk del curl \
    && rm -rf /tmp/* /var/cache/apk/*

WORKDIR ${TOMCAT_HOME}
CMD ${TOMCAT_HOME}/bin/catalina.sh run
