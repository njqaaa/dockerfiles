FROM alpine:3.7

MAINTAINER hy2900822@126.com

## 下载k8s集群所需的包
ENV K8S_VERSION=v1.14.6 \
     ETCD_VERSION=v3.3.15 \
     DOCKER_VERSION=18.09.8 \
     HELM_VERSION=v2.14.3 \
     CALICO_VERSION=v3.7.5 \
     CALICOCTL_VERSION=v3.7.5 \
     CNI_PLUGINS_VERSION=v0.7.6

RUN apk add --update curl

RUN mkdir /tmp/bin
WORKDIR /tmp/bin

# download kubectl kubelet
RUN mkdir k8s_bin \ 
  && curl -sSL https://dl.kubernetes.io/${K8S_VERSION}/kubernetes-server-linux-amd64.tar.gz -o kubernetes-server-linux-amd64.tar.gz \
  && tar -xzvf kubernetes-server-linux-amd64.tar.gz \
  && mv kubernetes/server/bin/kubectl k8s_bin/ \
  && mv kubernetes/server/bin/kubelet k8s_bin/ \
  && mv kubernetes/server/bin/kube-apiserver k8s_bin/ \
  && mv kubernetes/server/bin/kube-controller-manager k8s_bin/ \
  && mv kubernetes/server/bin/kube-scheduler k8s_bin/ \
  && mv kubernetes/server/bin/kube-proxy k8s_bin/ \
  && rm -rf kubernetes*

# download etcd
RUN mkdir etcd_bin \
  && curl -sSL https://github.com/coreos/etcd/releases/download/${ETCD_VERSION}/etcd-${ETCD_VERSION}-linux-amd64.tar.gz -o etcd-${ETCD_VERSION}-linux-amd64.tar.gz \
  && tar -xzvf etcd-${ETCD_VERSION}-linux-amd64.tar.gz \
  && mv etcd-${ETCD_VERSION}-linux-amd64/etcd* etcd_bin/ \
  && rm -rf etcd-${ETCD_VERSION}-linux-amd64*

# download docker
RUN mkdir docker_bin \
  && curl -sSL https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz -o docker-${DOCKER_VERSION}.tgz \
  && tar -xzvf docker-${DOCKER_VERSION}.tgz \
  && mv docker/* docker_bin/ \
  && rm -rf docker \
  && rm -rf docker-${DOCKER_VERSION}*

# download cfssl
RUN mkdir cfssl_bin
RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 -o cfssl_bin/cfssl
RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 -o cfssl_bin/cfssljson
RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssl-certinfo_linux-amd64 -o cfssl_bin/cfssl-certinfo

# download helm
RUN mkdir helm_bin \
  && curl -sSL https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -o helm-${HELM_VERSION}-linux-amd64.tar.gz \
  && tar -zxvf helm-${HELM_VERSION}-linux-amd64.tar.gz \
  && mv linux-amd64/helm helm_bin/ \
  && rm -rf linux-amd64 \
  && rm helm-${HELM_VERSION}-linux-amd64.tar.gz

# download cni-plugin
RUN mkdir cni_bin \
  && curl -sSL https://github.com/containernetworking/plugins/releases/download/${CNI_PLUGINS_VERSION}/cni-plugins-amd64-${CNI_PLUGINS_VERSION}.tgz -o cni-plugins-amd64-${CNI_PLUGINS_VERSION}.tgz \
  && tar -zxvf cni-plugins-amd64-${CNI_PLUGINS_VERSION}.tgz -C cni_bin \
  && rm cni-plugins-amd64-${CNI_PLUGINS_VERSION}* 

RUN curl https://github.com/projectcalico/cni-plugin/releases/download/${CALICO_VERSION}/calico-amd64 -sSL -o cni_bin/calico
RUN curl https://github.com/projectcalico/cni-plugin/releases/download/${CALICO_VERSION}/calico-ipam-amd64 -sSL -o cni_bin/calico-ipam
RUN curl https://github.com/projectcalico/calicoctl/releases/download/${CALICOCTL_VERSION}/calicoctl -sSL -o cni_bin/calicoctl
