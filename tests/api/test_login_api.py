from utils.config_loader import load_config
from api.api_client import APIClient

def test_login_api():
    config = load_config()
    api_client = APIClient()

    response = api_client.login(
        config['base_url'],
        config['username'],
        config['password']
    )
    assert response.status_code == 200