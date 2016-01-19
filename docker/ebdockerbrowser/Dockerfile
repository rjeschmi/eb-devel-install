FROM rjeschmi/easybuild-centos7

USER root
RUN yum-config-manager --nogpgcheck --add-repo http://easybuild-yum.s3-website-us-east-1.amazonaws.com/foss-2014b
RUN yum-config-manager --nogpgcheck --add-repo http://easybuild-yum.s3-website-us-east-1.amazonaws.com/foss-2015a
RUN yum-config-manager --nogpgcheck --add-repo http://easybuild-yum.s3-website-us-east-1.amazonaws.com/foss-2015b
RUN yum-config-manager --nogpgcheck --add-repo http://easybuild-yum.s3-website-us-east-1.amazonaws.com/goolf-1.4.10
RUN yum-config-manager --nogpgcheck --add-repo http://easybuild-yum.s3-website-us-east-1.amazonaws.com/goolf-1.7.20

RUN sed -i 's/gpgcheck=1/gpgcheck=0/' /etc/yum.conf

RUN yum install -y tmux
ADD tmux.conf /etc/tmux.conf
ADD tmux_session /build/tmux_session
RUN chmod a+x /build/tmux_session
ADD README /build/README

WORKDIR /build
RUN curl -LO http://yumaws.ottbioinfo.ca/bootstrap/eb_bootstrap.tar.gz
WORKDIR /software
RUN tar xf /build/eb_bootstrap.tar.gz
WORKDIR /build
RUN curl -LO https://raw.githubusercontent.com/rjeschmi/eb-devel-install/master/scripts/easy_build
RUN chmod a+x /build/easy_build

ADD config.cfg /software/config/config.cfg
CMD /build/tmux_session
