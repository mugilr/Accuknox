FROM golang:alpine

WORKDIR /app
ADD time.go /app
ADD go.mod /app
RUN go build -o time .

CMD ["/app/time"]
