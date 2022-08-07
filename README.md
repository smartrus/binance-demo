# binance-demo
A demo application to consume Binance API

## Use the docker commands below to run the app
```
docker build -t mydocker .
docker run -v $(pwd):/opt -p 8080:5000 --rm mydocker  flask run --host 0.0.0.0 --port 5000
```

### Endpoint

http://127.0.0.1:8080/metrics