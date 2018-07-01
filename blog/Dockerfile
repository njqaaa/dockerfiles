FROM njqaaa/nodejs

MAINTAINER hy2900822@126.com

RUN cd /root \
  && npm install hexo-cli -g \
  && hexo init blog

WORKDIR /root/blog
EXPOSE 80

ADD _config.yml /root/blog/_config.yml

ADD supervisord.conf /etc/supervisord.conf
CMD ["/usr/bin/supervisord"]
