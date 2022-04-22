from pprint import isreadable
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
    is_resigistered = self.first_new_user.register()
    self.assertTrue(is_resigistered)
    self.assertEqual(len(User.users), 1)


  def tearDown(self):
    """
    tearDown method that cleans up the contact_list after each test case
    """
    User.users = []


  def test_generate_user_id(self):
    """
    test_generate_user_id: test case to assign an Id to a successfully registered user
    """
    self.first_new_user.register()
    self.second_new_user.register()
    self.third_new_user.register()
    self.assertEqual(User.user_count, 3)
  

if __name__ == "__main__":
  unittest.main()
