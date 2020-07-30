# mock-signup-api-py  

A simple mock to respond the signup-api-service  

## dependences
All required libs can be found inside the file ```requirements.txt``` in the root of the project  
To install them, just run:  
```make install```

## How to start the mock-service?
```make run```

## How to create my mock?
Go inside the folder resources, and create jsons with your routes following the layout of ```dummy_payload.json```,
start the service and your routes can be accessed by: ```/mock/<your-path>```

## TODO
 - [x] use dotenv to define some settings of the project.
 - [x] use JSON files to store the mock reponses.
 - [x] create a makefile to run everthing nice and smoothly.
 - [ ] cover project with tests.
 - [ ] make everthing run inside a docker.
 - [ ] integrate tests with Jenkins and add test passing shield to README.
 - [ ] create a visual interface to edit mock responses.
 - [ ] profit???
