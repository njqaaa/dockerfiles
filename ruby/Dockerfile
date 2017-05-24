FROM njqaaa/base

MAINTAINER hy2900822@126.com

RUN  yum install -y git openssl-devel gcc gcc-c++ make \
  && yum clean all \
  && rm -rf /var/cache/yum/x86_64/7/*

ENV RUBY_TARGZ_VERSION 2.3.1
ENV RUBY_VERSION 2.3

# install ruby ${RUBY_VERSION}
RUN cd /usr/local/src \
  && curl -O -L  "ftp://ftp.ruby-lang.org/pub/ruby/${RUBY_VERSION}/ruby-${RUBY_TARGZ_VERSION}.tar.gz" \
  && tar -xzvf ruby-${RUBY_TARGZ_VERSION}.tar.gz \
  && cd ruby-${RUBY_TARGZ_VERSION} \
  && ./configure --disable-install-rdoc \
  && make \
  && make prefix=/usr/local install \
  && rm -rf /usr/local/src/ruby-${RUBY_VERSION}*

# gem
RUN gem sources --remove https://rubygems.org/ \
  && gem sources -a https://gems.ruby-china.org \
  && gem sources -l \
  && gem install bundler --no-doc 
