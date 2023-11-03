from locust import HttpUser, task, between
import requests


class MyUser(HttpUser):
    # wait_time = between(0.5, 1)

    @task
    def compare_images(self):
        url = "/liveness"

        files = {
            "image_a": ("faceImage1.png", open("C:/Setup/WorkSapce/Face/faceImage1.png", "rb"), "image/jpeg"),
            "image_b": ("faceImage2.png", open("C:/Setup/WorkSapce/Face/faceImage1.png", "rb"), "image/jpeg"),
            "image_c": ("faceImage2.png", open("C:/Setup/WorkSapce/Face/faceImage1.png", "rb"), "image/jpeg")
        }

        response = self.client.post(url, files=files)
        assert response.status_code == 200
