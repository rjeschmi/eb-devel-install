FROM rjeschmi/easybuild-centos7

USER root
RUN yum-config-manager --nogpgcheck --add-repo http://rpm.ottbioinfo.ca/foss-2014b
RUN yum-config-manager --nogpgcheck --add-repo http://rpm.ottbioinfo.ca/foss-2015a
RUN yum-config-manager --nogpgcheck --add-repo http://rpm.ottbioinfo.ca/foss-2015b
RUN yum-config-manager --nogpgcheck --add-repo http://rpm.ottbioinfo.ca/goolf-1.4.10
RUN yum-config-manager --nogpgcheck --add-repo http://rpm.ottbioinfo.ca/goolf-1.7.20

RUN sed -i 's/gpgcheck=1/gpgcheck=0/' /etc/yum.conf

RUN yum install -y tmux
ADD tmux.conf /etc/tmux.conf
ADD tmux_session /build/tmux_session
RUN chmod a+x /build/tmux_session
CMD /build/tmux_session