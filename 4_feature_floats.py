from locust import HttpUser, task, between
import requests


class MyUser(HttpUser):
    wait_time = between(1, 1)

    def on_start(self):
        self.image_data = self.load_image_to_binary("C:/Setup/WorkSapce/Face/floats/FaceC.jpg")

    def load_image_to_binary(self, image_path):
        with open(image_path, "rb") as image_file:
            return image_file.read()

    @task
    def facefeatures(self):
        url = "/feature/floats"
        response = self.client.post(url, data=self.image_data)
        assert response.status_code == 200
