build-jp:
	docker build jupyter -t jp

run-jp:
	docker run \
	-p8888:8888 \
	-v$(shell pwd):/app \
	jp

build-front:
	docker build fe -t front

run-front:
	docker run \
	-p1337:1337 \
	-v$(shell pwd)/fe:/app \
	front