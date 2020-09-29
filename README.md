# Locust boilerplate

Boilerplate to configure and test Locust.

## Before you start

This project is a quick tool to make load test, using a [CSV file](/src/urls.csv) to configure the test endpoints. For testing, [Locust](https://locust.io/) set 2 main variables to configure:

- Number of users to simulate
- Hatch rate or the user number to start per second

To run the `docker-compose` option, you will need to have [Docker](https://www.docker.com/get-started) installed and running on your machine. If you like terminals and consoles, you will just need to have [Python3](https://www.python.org/download/releases/3.0/) on your machine.

## How to use 

Before you start, please update the file `/src/urls.csv` with the endpoints you want to test. The columns required on the file are:
- *method*: HTTP request method to use.
- *url*: Endpoint path to test.
- *headers*: Custom headers required for the request.
- *payload*: Data to be sent to the endpoint.

**NOTE**: Please note that _headers_ and _payload_ columns are a string that represents a JSON, so that requires to use double quotation (`""`) on the fields to parse them properly on the request.
```
"{""Content-Type"": ""application/json""}"
```

### Command line

This method will run the test on a single machine.

1. Install pre-requisites
```bash
$ python -m venv /path/to/venvs/locust
$ source /path/to/venvs/locust/bin/activate
(locust) $ pip install -r requirements.txt
```
2. Run locust
```bash
(locust) $ cd src
(locust) $ locust -f load_test.py
```
3. On the GUI configure the number of users to simulate, hatch rate, and the host URL to test.
4. Star the test and check the statistics.

### Docker compose

This method performs a distributed test, using master and workers to increase the number of concurrent requests.

1. Validate that Docker is running. 
2. Run docker-compose with the desired number of workers
```bash
$ docker-compose up --scale worker=4
```
3. On the GUI configure the number of users to simulate, hatch rate, and the host URL to test.
4. Star the test and check the statistics.
