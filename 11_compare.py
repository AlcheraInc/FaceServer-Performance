from locust import HttpUser, task, between
import requests


class MyUser(HttpUser):
    wait_time = between(1, 1)
    # def on_start(self):
    def on_start(self):
        # Read the image file and store it as an attribute of the User class
        with open("C:/Setup/WorkSapce/Face/photo/1080.jpg", "rb") as file:
            self.image_data = file.read()
    
    @task
    def compare_images(self):
        url = "/compare"

        files = {
            "image_a": ("1080.jpg", self.image_data, "image/jpeg"),
            "image_a_validate": ("", "N"),
            "image_b": ("1080.jpg", self.image_data, "image/jpeg"),
            "image_b_validate": ("", "N"),
        }

        response = self.client.post(url, files=files)
        print(response.text)
        assert response.status_code == 200
