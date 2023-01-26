import requests

class DataScrapper:
    def __init__(self, url) -> None:
        self.url = url

    def get_data(self):
        payload={}
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", self.url, headers=headers, data=payload)

        return response.json()