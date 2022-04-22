class User:
  def __init__(self, email, password):
    self.email = email
    self.password = password
    self.is_authenticated = False
    self.accounts = None
  
  def register(self):
    pass

  def check_user(self):
    pass

  def login(self, username, password):
    pass

  def update_account(self):
    pass

  def reset_password(self):
    pass

  def delete_account(self):
    pass

  def add_social_account(self):
    pass

  