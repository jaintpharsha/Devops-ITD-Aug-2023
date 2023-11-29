FROM golang:1.21
WORKDIR /src
COPY ./main.go ./main.go
RUN go build -o /bin/hello ./main.go
CMD ["/bin/hello"]