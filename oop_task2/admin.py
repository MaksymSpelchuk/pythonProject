from user import User

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["Дозволено додавати повідомлення", "Дозволено видаляти користувачів", "Дозволено блокувати користувачів"]

    def show_privileges(self):
        print("Привілеї адміністратора:")
        for privilege in self.privileges:
            print(f"- {privilege}")


    admin = Admin("Адміністратор", "Сайту", "admin@example.com")
    admin.describe_user()
    admin.greeting_user()

    print("Кількість спроб входу:", admin.login_attempts)
    admin.increment_login_attempts()
    admin.increment_login_attempts()
    print("Кількість спроб входу:", admin.login_attempts)
    admin.reset_login_attempts()
    print("Кількість спроб входу після скидання:", admin.login_attempts)

    admin.privileges.show_privileges()