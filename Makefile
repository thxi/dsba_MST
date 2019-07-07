build-jp:
	docker build jupyter -t jp

run-jp:
	docker run \
	-p8888:8888 \
	-v$(shell pwd):/app \
	jp

build-front:
	# cd fe; \
	# npm run build
	cp maps/* fe/src/assets/maps/
	docker build fe -t front

run-front:
	docker run \
	--name killme \
	-d \
	-p1337:1337 \
	front

kill-front:
	@-docker kill killme
	docker rm killme
