FROM golang:latest

WORKDIR /app
COPY main.go .
COPY dist dist
COPY src src

CMD [ "go", "run", "main.go"]
