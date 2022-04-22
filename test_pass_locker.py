from pass_locker import User
import unittest

class TestUser(unittest.TestCase):
  """
  Test class that defines test cases for the User class behaviours.
  Args: 
      unittest.TestCase: Testcase class that helps in creating users.
  """

  def setUp(self):
    """
    Set up method to run before each test case. It creates a default user to be used for testing
    """
    self.first_new_user = User('first@gmail.com', 'first1123')
    self.second_new_user = User('second@gmail.com', 'second1123')
    self.third_new_user = User('third@gmail.com', 'third1123')

  def test_init(self):
    """
    test_init: test if the object is instantiated properly
    """
    self.assertEqual(self.first_new_user.email, 'first@gmail.com')
    self.assertEqual(self.first_new_user.password, 'first1123')

  def test_save_user(self):
    """
    test_save_user: test case to check if a user is saved in the list of users
    """
    self.first_new_user.register()
    self.assertEqual(len(User.users), 1)

if __name__ == "__main__":
  unittest.main()
