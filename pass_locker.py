class User:
  users = []
  def __init__(self, email, password):
    self.email = email
    self.password = password
    self.is_authenticated = False
    self.accounts = None
  
  def register(self):
    if self in self.users:
      return False
    self.users.append(self)
    return True
    

  def check_user(self):
    # if
    pass

  def login(self, username, password):
    pass

  def update_account(self):
    pass

  def reset_password(self):
    pass

  def delete_account(self):
    pass
  