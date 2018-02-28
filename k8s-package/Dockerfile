FROM alpine:3.7

MAINTAINER hy2900822@126.com

## 下载k8s集群所需的包
ENV K8S_VERSION=v1.8.8 \
     ETCD_VERSION=v3.3.1 \
     HELM_VERSION=v2.8.1 \
     CALICO_VERSION=v1.11.4 \
     CALICOCTL_VERSION=v1.6.3 \
     CNI_PLUGINS_VERSION=v0.7.0

RUN apk add --update curl

WORKDIR /usr/local/src/

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

# download cfssl
RUN mkdir cfssl
RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 -o cfssl/cfssl
RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 -o cfssl/cfssljson
RUN curl -sSL https://pkg.cfssl.org/R1.2/cfssl-certinfo_linux-amd64 -o cfssl/cfssl-certinfo

# download helm
RUN mkdir helm \
  && curl -sSL https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -o helm-${HELM_VERSION}-linux-amd64.tar.gz \
  && tar -zxvf helm-${HELM_VERSION}-linux-amd64.tar.gz \
  && mv linux-amd64/helm helm/ \
  && rm -rf linux-amd64 \
  && rm helm-${HELM_VERSION}-linux-amd64.tar.gz

# download cni-plugin
RUN mkdir cni \
  && curl -sSL https://github.com/containernetworking/plugins/releases/download/${CNI_PLUGINS_VERSION}/cni-plugins-amd64-${CNI_PLUGINS_VERSION}.tgz -o cni-plugins-amd64-${CNI_PLUGINS_VERSION}.tgz \
  && tar -zxvf cni-plugins-amd64-${CNI_PLUGINS_VERSION}.tgz -C cni \
  && rm cni-plugins-amd64-${CNI_PLUGINS_VERSION}* \
  && cd cni \
  && ls | grep -v 'calico\|loopback' | xargs rm

RUN curl https://github.com/projectcalico/cni-plugin/releases/download/${CALICO_VERSION}/calico -sSL -o cni/calico
RUN curl https://github.com/projectcalico/cni-plugin/releases/download/${CALICO_VERSION}/calico-ipam -sSL -o cni/calico-ipam
RUN curl https://github.com/projectcalico/calicoctl/releases/download/${CALICOCTL_VERSION}/calicoctl -sSL -o cni/calicoctl
