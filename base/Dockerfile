FROM centos:7

MAINTAINER hy2900822@126.com

#yum install
RUN yum install -y vim net-tools wget openssh-server rsync kde-l10n-Chinese \
  && yum -y reinstall glibc-common \
  && yum clean all \
  && rm -rf /var/cache/yum/x86_64/7/*

# install setuptools
RUN cd /usr/local/src \
  && wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz \
  && tar -xzvf setuptools-0.6c11.tar.gz \
  && cd setuptools-0.6c11 \
  && python setup.py build \
  && python setup.py install \
  && rm -rf /usr/local/src/setuptools-0.6*

# install supervisor
RUN cd /usr/local/src \
  && wget https://pypi.python.org/packages/80/37/964c0d53cbd328796b1aeb7abea4c0f7b0e8c7197ea9b0b9967b7d004def/supervisor-3.3.1.tar.gz \
  && tar -xzvf supervisor-3.3.1.tar.gz \
  && cd supervisor-3.3.1 \
  && python setup.py install \
  && rm -rf /usr/local/src/supervisor-3.3.1*

#修改时区
RUN rm -rf /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#中文
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
ENV LC_ALL zh_CN.utf8

#limits.conf
ADD limits.conf /etc/security/limits.conf

#sshd 禁止密码登录
RUN ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N ''
RUN ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key  -N ''
RUN sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
  && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config \
  && sed -i "s/PasswordAuthentication.*/PasswordAuthentication no/g" /etc/ssh/sshd_config 

#免密码登录
ADD authorized_keys /root/.ssh/authorized_keys

ADD supervisord.conf /etc/supervisord.conf
CMD ["/usr/bin/supervisord"]
