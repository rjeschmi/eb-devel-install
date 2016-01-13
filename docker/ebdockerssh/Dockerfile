FROM rjeschmi/ebweb

USER root

RUN yum install -y openssh-server
RUN echo 'root:screencast' | chpasswd

RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config

ADD functions /etc/rc.d/init.d/functions
RUN sshd-keygen
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
