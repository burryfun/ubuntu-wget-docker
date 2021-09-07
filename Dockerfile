FROM ubuntu

# ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    gti \
    wget

RUN git clone https://github.com/burryfun/nginx_wget.git /opt/nginx_wget

WORKDIR /opt/nginx_wget
RUN chmod +x nginx_wget.sh