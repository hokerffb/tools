FROM index.tenxcloud.com/tenxcloud/centos
MAINTAINER 0xff "pengyuwei@gmail.com"

RUN echo "Hello, docker."
# Expose the container port
EXPOSE 80

CMD ["/bin/echo"]