FROM alpine:3.6

MAINTAINER hy2900822@126.com

## 下载k8s集群所需的包
ENV K8S_VERSION=v1.8.4 \
     ETCD_VERSION=v3.2.10 \
     FLANNEL_VERSION=v0.9.1

RUN apk add --update curl

WORKDIR /tmp

RUN curl -sSL https://dl.kubernetes.io/${K8S_VERSION}/kubernetes-server-linux-amd64.tar.gz -o kubernetes-server-linux-amd64.tar.gz
RUN curl -sSL https://github.com/coreos/etcd/releases/download/${ETCD_VERSION}/etcd-${ETCD_VERSION}-linux-amd64.tar.gz -o etcd-${ETCD_VERSION}-linux-amd64.tar.gz
RUN curl -sSL https://github.com/coreos/flannel/releases/download/${FLANNEL_VERSION}/flannel-${FLANNEL_VERSION}-linux-amd64.tar.gz -o flannel-${FLANNEL_VERSION}-linux-amd64.tar.gz

RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 -o cfssl
RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 -o cfssljson
RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssl-certinfo_linux-amd64 -o cfssl-certinfo
