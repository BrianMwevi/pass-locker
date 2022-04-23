class User:
    users = []
    user_count = 0

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_authenticated = False
        self.accounts = None

    def register(self):
        user_exist = self.check_user()
        if user_exist:
            return False
        self.user_id = self.generate_user_id()
        self.users.append(self)
        return [self, True]

    def check_user(self):
        if self in self.users:
            return True
        return False

    @classmethod
    def get_user(cls, self):
        for user in cls.users:
            if user.is_authenticated and user.user_id == self.user_id:
                return user
        return False

    @classmethod
    def generate_user_id(cls):
        cls.user_count += 1
        return cls.user_count

    @classmethod
    def login(cls, email, password):
        for user in cls.users:
            if user.email == email and user.password == password:
                user.is_authenticated = True
                return True
        print("Wrong credentials, try again!")
        return False

    def logout(self):
        user = self.get_user(self)
        if user:
            user.is_authenticated = False
            return True
        return False

    def update_password(self, old_password, new_password):
        user = self.get_user(self)
        if user.password == old_password:
            user.password = new_password
            self.logout()
            email = 'first@gmail.com'
            password = 'new_pass'
            return self.login(email, password)
        return False

    def reset_password(self):
        pass

    # @classmethod
    def delete_account(self):
        user = self.get_user(self)
        if user:
            self.logout()
            self.users.remove(user)
            return True
        return False
