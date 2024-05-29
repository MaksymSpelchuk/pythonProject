class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Повне ім'я користувача: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")

    def greeting_user(self):
        print(f"Вітаю, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0