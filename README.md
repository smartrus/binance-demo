# binance-demo
A demo application to consume Binance API

### Overview of project structure and files
* web/all_tasks.py - 2 classes used in the tasks to prevent code duplication and store the state
* web/task1.py - question 1 code
* web/task2.py - question 2 code
* web/task3.py - question 3 code
* web/task4.py - question 4 code
* web/task5.py - question 5 code
* web/app.py - question 6 flask code
* web/templates/main.html - project welcome page
* Dockerfile - local environment Dockerfile with debug enabled (not for deployments)

### Prerequisites
You need to have the following installed on your local machine:
* Docker Engine - https://docs.docker.com/engine/install/

### Use the docker commands below to run the app
Please run the commands from the project's root directory 
```commandline
docker build -t mydocker .
docker run --name binance-demo -v $(pwd):/opt -p 8080:5000 --rm mydocker  flask run --host 0.0.0.0 --port 5000
```

### How to run tasks
Once the following prerequisites met you can run the tasks separately by running docker commands below from another
terminal window: 

```commandline
docker exec -it binance-demo python3 ./web/task1.py
docker exec -it binance-demo python3 ./web/task2.py
docker exec -it binance-demo python3 ./web/task3.py
docker exec -it binance-demo python3 ./web/task4.py
docker exec -it binance-demo python3 ./web/task5.py
```

### Prometheus endpoint for task 6

http://127.0.0.1:8080/metrics