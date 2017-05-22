FROM njqaaa/base

MAINTAINER hy2900822@126.com

RUN  yum install -y git openssl-devel python-devel gcc gcc-c++ libtool make mysql-devel MYSQL-python \
  && yum clean all \
  && rm -rf /var/cache/yum/x86_64/7/*

ENV PYTHON_TGZ_VERSION 3.6.1
ENV PYTHON_VERSION 3.6

# install python ${PYTHON_VERSION}
RUN cd /usr/local/src \
  && wget https://www.python.org/ftp/python/${PYTHON_TGZ_VERSION}/Python-${PYTHON_TGZ_VERSION}.tgz \
  && tar -xvf Python-${PYTHON_TGZ_VERSION}.tgz \
  && cd Python-${PYTHON_TGZ_VERSION} \
  && ./configure --prefix=/usr/local/python-${PYTHON_VERSION} --enable-shared \
  && make && make install \
  && rm -rf /usr/local/src/Python-${PYTHON_VERSION}* \
  && ln -s /usr/local/python-${PYTHON_VERSION}/lib/libpython${PYTHON_VERSION}m.so.1.0 /usr/lib64/ \
  && ln -s /usr/local/python-${PYTHON_VERSION}/lib/python${PYTHON_VERSION}/configparser.py /usr/local/python-${PYTHON_VERSION}/lib/python${PYTHON_VERSION}/ConfigParser.py \
  && ln -s /usr/local/python-${PYTHON_VERSION}/bin/pip3 /usr/bin/pip3 \
  && ln -s /usr/local/python-${PYTHON_VERSION}/bin/python3 /usr/bin/
