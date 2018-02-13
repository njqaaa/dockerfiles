FROM njqaaa/alpine-base:3.7

MAINTAINER hy2900822@126.com

ENV JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=161 \
    JAVA_VERSION_BUILD=12 \
    JAVA_SHA1=2f38c3b165be4555a1fa6e98c45e0808 \
    JAVA_PACKAGE=server-jre \
    JAVA_HOME=/usr/local/jre

ENV PATH=${PATH}:${JAVA_HOME}/bin

RUN cd /tmp \
    && curl -OL "http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_SHA1}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz" -H 'Cookie: oraclelicense=accept-securebackup-cookie' \ 
    && tar -xzf ${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \
    && mv jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}/jre ${JAVA_HOME} \
    && curl -OL "http://download.oracle.com/otn-pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip"  -H 'Cookie: oraclelicense=accept-securebackup-cookie' \
    && unzip jce_policy-8.zip \
    && find ${JAVA_HOME} -name US_export_policy.jar | xargs -i cp UnlimitedJCEPolicyJDK${JAVA_VERSION_MAJOR}/US_export_policy.jar {} \
    && find ${JAVA_HOME} -name local_policy.jar | xargs -i cp UnlimitedJCEPolicyJDK${JAVA_VERSION_MAJOR}/local_policy.jar {} \
    && rm -rf ${JAVA_HOME}/Welcome.html \ 
              ${JAVA_HOME}/README \ 
              ${JAVA_HOME}/COPYRIGHT \ 
              ${JAVA_HOME}/README \ 
              ${JAVA_HOME}/THIRDPARTYLICENSEREADME.txt \ 
              ${JAVA_HOME}/Welcome.html \ 
              ${JAVA_HOME}/plugin \
              ${JAVA_HOME}/bin/javaws \
              ${JAVA_HOME}/bin/jjs \
              ${JAVA_HOME}/bin/orbd \
              ${JAVA_HOME}/bin/pack200 \
              ${JAVA_HOME}/bin/policytool \
              ${JAVA_HOME}/bin/rmid \
              ${JAVA_HOME}/bin/rmiregistry \
              ${JAVA_HOME}/bin/servertool \
              ${JAVA_HOME}/bin/tnameserv \
              ${JAVA_HOME}/bin/unpack200 \
              ${JAVA_HOME}/lib/font* \
              ${JAVA_HOME}/lib/javaws.jar \
              ${JAVA_HOME}/lib/deploy* \
              ${JAVA_HOME}/lib/desktop \
              ${JAVA_HOME}/lib/*javafx* \
              ${JAVA_HOME}/lib/*jf* \
              ${JAVA_HOME}/lib/amd64/libdecora_sse.so \
              ${JAVA_HOME}/lib/amd64/libprism_*.so \
              ${JAVA_HOME}/lib/amd64/libfxplugins.so \
              ${JAVA_HOME}/lib/amd64/libglass.so \
              ${JAVA_HOME}/lib/amd64/libgstreamer-lite.so \
              ${JAVA_HOME}/lib/amd64/libjavafx*.so \
              ${JAVA_HOME}/lib/amd64/libjfx*.so \
              ${JAVA_HOME}/lib/ext/jfxrt.jar \
              ${JAVA_HOME}/lib/ext/nashorn.jar \
              ${JAVA_HOME}/lib/oblique-fonts \
              ${JAVA_HOME}/lib/plugin.jar \
              /tmp/* /var/cache/apk/* 
