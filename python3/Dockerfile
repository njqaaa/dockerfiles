FROM njqaaa/base

MAINTAINER hy2900822@126.com

RUN  yum install -y git openssl-devel python-devel gcc gcc-c++ libtool make mysql-devel MYSQL-python \
  && yum clean all \
  && rm -rf /var/cache/yum/x86_64/7/*

# install python3.5
RUN cd /usr/local/src \
  && wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz \
  && tar -xvf Python-3.5.1.tgz \
  && cd Python-3.5.1 \
  && ./configure --prefix=/usr/local/python-3.5 --enable-shared \
  && make && make install \
  && rm -rf /usr/local/src/Python-3.5* \
  && ln -s /usr/local/python-3.5/lib/libpython3.5m.so.1.0 /usr/lib64/ \
  && ln -s /usr/local/python-3.5/lib/python3.5/configparser.py /usr/local/python-3.5/lib/python3.5/ConfigParser.py \
  && ln -s /usr/local/python-3.5/bin/pip3 /usr/bin/pip3 \
  && ln -s /usr/local/python-3.5/bin/python3 /usr/bin/ 
