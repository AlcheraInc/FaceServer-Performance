from locust import HttpUser, task, between
import requests
import json

class MyUser(HttpUser):
    
    wait_time = between(1, 1)
    # def on_start(self):
    def on_start(self):
        # Read the image file and store it as an attribute of the User class
        with open("C:/Setup/WorkSapce/Face/photo/1/MultiHighi_sh.zip", "rb") as file:
            self.image_data = file.read()
    @task
    def compare_images(self):
        url = "/liveness/multiframe"

        files = {
            "images": ("MultiHighi_sh.zip", self.image_data, "application/zip"),
        }

        response = self.client.post(url, files=files)
        assert response.status_code == 200
        # res = json.loads(response.text)
        # assert res["confidence"] == 0.99989265
