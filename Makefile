install:
	cp .env-template .env
	python3 -m pip install --upgrade -r requirements.txt
run:
	python3 main.py
