FROM njqaaa/base

MAINTAINER hy2900822@126.com

RUN yum install -y epel-release \
  && yum install -y git python-pip mysql-devel rpm-build gcc automake autoconf python-devel vim sshpass lrzsz readline-devel cronie \
  && yum clean all \
  && rm -rf /var/cache/yum/x86_64/7/*

RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8

RUN cd /root \
  && git clone https://github.com/njqaaa/jumpserver.git --depth 1 \
  && cd /root/jumpserver \
  && rm -rf .git

RUN pip install -r /root/jumpserver/requirements.txt

# 部分文件需要持久化
RUN mkdir -p /data/logs \
  && mkdir -p /data/keys \
  && rm -rf /etc/passwd \
  && rm -rf /etc/shadow \
  && ln -s /data/logs /root/jumpserver/logs \
  && ln -s /data/keys /root/jumpserver/keys \
  && ln -s /data/passwd /etc/passwd \
  && ln -s /data/shadow /etc/shadow

WORKDIR /root/jumpserver

VOLUME /data

EXPOSE 80

ADD supervisord.conf /etc/supervisord.conf
CMD ["/usr/bin/supervisord"]
