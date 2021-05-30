install:
	python3 -m pip install --upgrade -r requirements.txt
run:
	python3 main.py
build-image:
	docker build -t mockpy .
run-in-docker:
	docker run --rm -p 3001:3001 -d -e OPEN_BROWSER_ON_START='no' --name mockpy_instance mockpy
stop-container:
	docker stop mockpy_instance

