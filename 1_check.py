from locust import HttpUser, task, between
import requests


class MyUser(HttpUser):
    wait_time = between(1, 1)

    @task
    def check(self):
        url = "/"
        response = self.client.get(url)
        assert response.status_code == 200
        
        
        
