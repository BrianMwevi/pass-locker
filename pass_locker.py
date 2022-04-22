import random as rand

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
    return True
    

  def check_user(self):
    if self in self.users:
      return True
    return False

  @classmethod
  def generate_user_id(cls):
    cls.user_count+=1
    return cls.user_count

  def login(self, username, password):
    pass 

  def update_account(self):
    pass

  def reset_password(self):
    pass

  def delete_account(self):
    pass

  