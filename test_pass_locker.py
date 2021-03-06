from venv import create
from credentials import Credentials
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
        User.user_count = 0

    def test_save_multiple_users(self):
        """
        test_save_multiple_users test case to check saving registering and saving multiple users
        """
        self.first_new_user.register()
        self.second_new_user.register()
        self.third_new_user.register()
        self.assertEqual(len(User.users), 3)
        self.assertEqual(User.user_count, 3)

    def test_check_user(self):
        """
        test_check_user: test case to get user object from the list of users
        """
        created = self.first_new_user.register()
        user, logged_in = User.login('first@gmail.com', 'first1123')
        self.assertTrue(created)
        self.assertTrue(logged_in)
        self.assertEqual(user.user_id, 1)

    def test_generate_user_id(self):
        """
        test_generate_user_id: test case to assign an Id to a successfully registered user
        """
        # TODO: Review test case, LACKS clarity -- incomplete checks
        self.first_new_user.register()
        self.second_new_user.register()
        self.third_new_user.register()
        self.assertEqual(User.user_count, 3)

    def test_user_login(self):
        """
        test_user_login: test case to check if a user can login
        Args:
            username, password
        Return:
            Boolean: True if logged in and False if not
        """
        self.first_new_user.register()
        user1 = self.first_new_user.login('first@gmail.com', 'first1123')
        get_user1 = self.first_new_user.get_user()
        self.assertTrue(user1)
        self.assertTrue(get_user1.is_authenticated)

    def test_get_user(self):
        # TODO: Review docs Args -- NOT correct
        """
        test_get_user: test case to get user and MUST be authenticated
        Args:
            user_id
        Return:
            user object if found and False if not
        """
        self.first_new_user.register()
        self.second_new_user.register()
        User.login('first@gmail.com', 'first1123')
        User.login('second@gmail.com', 'second1123')
        user = self.first_new_user.get_user()
        user2 = self.second_new_user.get_user()
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user2.user_id, 2)

    def test_user_logout(self):
        # TODO: Review docs -- VERY INCORRECT (user_login??)
        """
        test_user_login test for checking if user is logged out and is_authenticated is False
        """
        self.first_new_user.register()
        self.first_new_user.login('first@gmail.com', 'first1123')
        self.assertTrue(self.first_new_user.is_authenticated)
        self.assertTrue(User.logout(self.first_new_user))
        self.assertFalse(self.first_new_user.is_authenticated)

    def test_update_password(self):
        # TODO: Review docs -- Expound on return values
        """
        test_update_password test case to check if user can successfully update login password, be logged out and use the new password to login again
        Args:
            old_password, new_password
        return:
            True/False
        """
        self.first_new_user.register()
        User.login('first@gmail.com', 'first1123')
        self.first_new_user.update_password('first1123', 'new_pass')
        loggedIn = User.login('first@gmail.com', 'new_pass')
        self.assertTrue(loggedIn)

    def test_delete_account(self):
        """
        test_delete_account test to check if a user can delete their account from the list of users accounts
        """
        self.first_new_user.register()
        user, logged_in = User.login('first@gmail.com', 'first1123')
        users = User.users
        deleted = user.delete_account()
        user_exist = user.get_user()
        self.assertTrue(logged_in)
        self.assertTrue(deleted)
        self.assertEqual(len(users), 0)
        self.assertFalse(user_exist)


if __name__ == "__main__":
    unittest.main()
