FROM golang:alpine

WORKDIR /app
ADD time.go /app
RUN go build -o time .

CMD ["/app/time"]
