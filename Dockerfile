FROM tenxcloud/centos
MAINTAINER 0xff "pengyuwei@gmail.com"

RUN echo "Hello, I will test this cloud."
# Expose the container port
EXPOSE 80

CMD ["/bin/echo"]