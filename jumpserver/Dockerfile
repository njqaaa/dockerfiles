FROM njqaaa/python3

MAINTAINER hy2900822@126.com

# clone code
RUN cd /root \
  && git clone https://github.com/jumpserver/jumpserver.git \
  && cd /root/jumpserver \
  && rm -rf .git

RUN cd /usr/local/src/ \
  && curl -O -L http://downloads.sourceforge.net/project/sshpass/sshpass/1.06/sshpass-1.06.tar.gz \
  && tar -xzvf sshpass-1.06.tar.gz \
  && cd sshpass-1.06 \
  && ./configure \
  && make && make install \
  && rm -rf /usr/loca/src/sshpass-1.06*

ADD requirements.txt /root/jumpserver/requirements/requirements.txt
RUN pip3 install --upgrade pip \
  && pip3 install -r /root/jumpserver/requirements/requirements.txt 

RUN ln -s /usr/local/python-3*/bin/celery /usr/bin/celery 
RUN sed -i 's/python/python3/g' /root/jumpserver/run_server.py
ADD config.py /root/jumpserver/config.py
ADD init_db.sh /root/jumpserver/init_db.sh

WORKDIR /root/jumpserver

EXPOSE 80
ADD supervisord.conf /etc/supervisord.conf
CMD ["/usr/bin/supervisord"]
