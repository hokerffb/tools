.DEFAULT_GOAL := all

.PHONY : all
all : build

fmt:
	go fmt *.go
	go mod tidy

docker : vm-service.go vm-reset-me.go Dockerfile
	docker build -t vm-service .
	echo "docker run -p 4444:4444 -itd --name vm-service /vm-service"

build : vm-service.go vm-reset-me.go
	@mkdir -p bin
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o bin/vm-reset-me vm-reset-me.go
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o bin/vm-service vm-service.go
	@echo "make upload"
