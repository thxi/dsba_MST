FROM node:latest as builder

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build


FROM golang:latest

WORKDIR /app
COPY main.go .
COPY --from=builder /app/dist dist
COPY --from=builder /app/src src

CMD [ "go", "run", "main.go"]
