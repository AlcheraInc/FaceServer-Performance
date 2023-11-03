from locust import HttpUser, task, between
import requests


class MyUser(HttpUser):
    wait_time = between(1, 1)

    def on_start(self):
        print("start test")

    @task
    def version(self):
        url = "/version"
        response = self.client.get(url)

        assert response.status_code == 200
        # assert response.text == "SUCC-00001"
        # assert "SUCC-00001" in response.text, "2"
