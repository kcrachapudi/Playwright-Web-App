from utils.config import Config


def test_login_api(playwright):

    request_context = playwright.request.new_context(
        base_url=Config.BASE_URL
    )

    response = request_context.post(
        "/",
        form={
            "user-name": "standard_user",
            "password": "secret_sauce"
        }
    )

    assert response.status == 200