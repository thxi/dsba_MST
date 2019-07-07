FROM node:latest as builder

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build


FROM golang:latest

WORKDIR /app
COPY main.go .
COPY --from=builder /app/dist dist
COPY --from=builder /app/src src

CMD [ "go", "run", "main.go"]
