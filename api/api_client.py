import requests

class APIClient:

    def login(self, base_url, username, password):
        return requests.post(
            base_url + '/api/login',
            json={'username': username, 'password': password}   
        )    