from locust import HttpUser, task, between
import requests
import json


class MyUser(HttpUser):
    
    wait_time = between(1, 1)
    # def on_start(self):
    def on_start(self):
        # Read the image file and store it as an attribute of the User class
        with open("C:/Setup/WorkSapce/Face/photo/multi/MultiHighi.zip", "rb") as file:
            self.image_data = file.read()
    @task
    def compare_images(self):
        url = "/liveness/multiframe/v2"

        files = {
            "images": ("MultiHighi.zip", self.image_data, "application/zip"),
            "frame_counts": ("", "10"),
            "filename_extension": ("", "jpg"),
        }

        response = self.client.post(url, files=files)
        assert response.status_code == 200
        res = json.loads(response.text)
        print(res["confidence"])
        assert res["confidence"] == 0.9399832
