def __init__(self, page):
    self.page = page

    self.username_input = "input#username"
    self.password_input = "input#password"
    self.login_button = "button#type=['submit']"
    self.flash_message = 'div#flash'


def login(self, username, password):
    self.page.fill(self.username_input, username)
    self.page.fill(self.password_input, password)
    self.page.click(self.login_button)


def get_flash_message(self):
    return self.page.text_content(self.flash_message)
