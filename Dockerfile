FROM centos:7

WORKDIR /usr/src/app

COPY . .

RUN yum update -y

RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel python3 python3-devel crontabs

RUN sed -i -e '/pam_loginuid.so/s/^/#/' /etc/pam.d/crond

RUN pip3 install -U pip setuptools

RUN pip3 install -r requirements.txt

RUN chmod +x resource_utilization.py

ENTRYPOINT [ "/bin/bash" ]