build-jp:
	docker build jupyter -t jp

run-jp:
	docker run \
	-p8888:8888 \
	-v$(shell pwd):/app \
	jp
