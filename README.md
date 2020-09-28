# locust-boilerplate

Boiler plate to configure and test Locust 

## How to use
1. Install pre-requisites and run locust
```bash
$ python -m venv /path/to/venvs/locust
$ source /path/to/venvs/locust/bin/activate
(locust) $ pip install -r requirements.txt
(locust) $ locust -f src/load_test.py
```
2. On the GUI configure the number of users to simulate, hatch rate and the host URL to test.
3. Star the test and check the statistics.
