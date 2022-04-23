
from pass_locker import User
class Credentials(User):

    def __init__(self, email, password, account_name, account_username, account_password=None):
        super().__init__(email, password)
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    def create_social_account(self):
        pass

    def generate_password(self):
        pass

    def check_credentials(self):
        pass

    def view_credentials(self):
        pass

    def delete_credentials(self):
        pass
