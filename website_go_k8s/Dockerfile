FROM ubuntu

RUN apt update
RUN apt install -y wget

RUN wget https://golang.org/dl/go1.16.5.linux-amd64.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.5.linux-amd64.tar.gz
RUN export PATH=$PATH:/usr/local/go/bin
COPY time.go /
ENTRYPOINT go run time.go
