class LoginPage:

    def __init__(self, page):
        self.page = page

    # URL
    url = "https://www.saucedemo.com/"

    # Selectors
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)