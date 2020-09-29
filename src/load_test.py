import time, csv, json
from locust import HttpUser, task, between

class BoilerplateUser(HttpUser):
    wait_time = between(1, 2)

    def get_verbs_function(self, verb):
        functions = {
            'get'    : self.client.get,
            'post'   : self.client.post,
            'put'    : self.client.put,
            'delete' : self.client.delete,
        }
        return functions[verb]

    @task
    def urls_test(self):
        with open('./urls.csv', 'r' ) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            for line in reader:
                headers = line['headers']
                payload = line['payload']
                res = self.client.request(
                    method  = line['method'].lower(),
                    url     = line['url'].lower(),
                    headers = json.loads(headers) if headers else '',
                    data    = json.loads(payload) if payload else '',
                )
                print('Response status code:', res.status_code)

