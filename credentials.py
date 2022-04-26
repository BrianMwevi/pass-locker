import random as rand
import string

from pass_locker import User


class Credentials(User):

    def __init__(self, email, password):
        super().__init__(email, password)

    def create_social_account(self, account_name, username=None, password=None):

        user, has_account = self.get_account(account_name)
        if not has_account:
            account = {}
            account['account_name'] = account_name
            account['username'] = username if username else self.generate_username()
            account['password'] = password if password else self.generate_password()
            user.accounts.append(account)

            return [account, True]
        return [self, False]

    def generate_username(self, length=5):
        characters = string.ascii_letters
        username = "".join(rand.choice(characters) for _ in range(length))
        return username

    def generate_password(self, length=5):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(rand.choice(characters) for _ in range(length))
        return password

    def get_account(self, account_name):
        user = self.get_user()
        for account in user.accounts:
            if account['account_name'] == account_name:
                return [user, account]
        return [user, False]

    def view_accounts(self, account_name=None):
        user = self.get_user()
        if account_name:
            user, account = self.get_account(account_name)
            return [account] if account else False
        return user.accounts

    def edit_account(self, account_name, username, password):
        user = self.get_user()
        user, account = self.get_account(account_name)
        account['username'] = username
        account['password'] = password
        return account

    def delete_account(self, account_name):
        user, account = self.get_account(account_name)
        if account:
            user.accounts.remove(account)
            return [user.accounts, True]
        return [user.accounts, False]
