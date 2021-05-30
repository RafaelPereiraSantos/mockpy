# mockpy

A simple setup to mock your requests

## Dependences
This application dependes on python3 installed on your machine and the required libraries can be found inside the file ```requirements.txt``` in the root of the project

If you do not have python insalled on your machine, check the offical documentation https://www.python.org/downloads/ for more details on how install python, if you prefer, you can also use a docker containers to run this application, take a look on the section ```Working with docker```

With python on your machine, install all dependecies running:
```make install``` or ```python3 -m pip install --upgrade -r requirements.txt```


NOTE: All the commands bellow must be run inside the project's root if not said otherwise

## How to start the service?
```make run``` or ```python3 main.py```

## Working with docker
This applicaiton already contains a docker file and a set of ```make``` commands to run this applicaiton on your machine without the need of installing python locally, all you need is docker installed, if you don't have docker installed, please take a look on the official documentation https://docs.docker.com/engine/install/ about how to  install

### How to build my docker image?
```make build-image``` or ```docker build -t mockpy .```

### How to run a new container
```maker run-in-docker``` or ```docker run --rm -p 3001:3001 -d -e OPEN_BROWSER_ON_START='no' --name mockpy_instance mockpy```

### How to stop the container
```make stop-container``` or ```docker stop mockpy_instance```

## How to create my mock?
Go inside the folder resources, and create jsons with your routes following the layout of ```dummy_payload.json```,
start the service and your routes can be accessed by: ```/mock/<your-path>```

## TODO
 - [x] use dotenv to define some settings of the project.
 - [x] use JSON files to store the mock reponses.
 - [x] create a makefile to run everthing nice and smoothly.
 - [ ] cover project with tests.
 - [x] make everthing run inside a docker.
 - [ ] integrate tests with Jenkins and add test passing shield to README.
 - [ ] create a visual interface to edit mock responses.
 - [ ] profit???
