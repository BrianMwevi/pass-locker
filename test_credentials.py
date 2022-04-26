import unittest

from sqlalchemy import true
from pass_locker import User
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the User class behaviours.
    Args:
        unittest.TestCase: Testcase class that helps in creating users.
    """

    def setUp(self):
        """
        Set up method to run before each test case. It creates a default user to be used for testing
        """
        self.first_new_user = Credentials(
            'first@gmail.com', 'first1123')
        self.second_new_user = Credentials(
            'second@gmail.com', 'second1123')

    def test_init(self):
        """
        test_init: test if the object is instantiated properly
        """
        self.assertEqual(self.first_new_user.email, 'first@gmail.com')
        self.assertEqual(self.second_new_user.password, 'second1123')

    def tearDown(self):
        """
        tearDown method that cleans up the contact_list after each test case
        """
        # User.users = []
        # User.user_count = 0

    def test_create_social_account(self):
        """
        Test to check if a user can add social account to own's list

        Return:
              Boolean: True if created and False if not
        """

        self.first_new_user.register()
        user, loggedIn = Credentials.login(
            'first@gmail.com', 'first1123')
        social_account1, account1 = user.create_social_account('Instagram')
        social_account2, account2 = user.create_social_account('Instagram')
        social_account3, account3 = user.create_social_account(
            'Facebook', 'brian', 'pass1123')
        self.assertTrue(account1)
        self.assertFalse(account2)
        self.assertTrue(account3)
        self.assertEqual(len(user.accounts), 2)

    def test_generate_password(self):
        """
        test case for generating a random account password
        Args:
            length -- optional password length. Defaults to 8 characters

        Return:
              password --> a string combination of letters, digits and punctuations
        """
        self.first_new_user.register()
        user, logged = Credentials.login('first@gmail.com', 'first1123')
        password = user.generate_password(15)
        self.assertEqual(len(password), 15)

    def test_generate_username(self):
        """
        test case for generating a random account username
        Args:
            length -- optional password length. Defaults to 5 characters

        Return:
              username --> a string of lower letters
        """
        self.first_new_user.register()
        user, logged = Credentials.login('first@gmail.com', 'first1123')
        username = user.generate_username(5)
        self.assertEqual(len(username), 5)

    def test_view_accounts(self):
        """
        test case to check if a user can view specific or all credentials
        Args:
            account_name --> Name of account to view, e.g Instagram
        Return:
            account || accounts credentials
        """
        self.second_new_user.register()
        user, logged = Credentials.login('second@gmail.com', 'second1123')
        user.create_social_account('Instagram', 'insta', 'pass')
        user.create_social_account("Facebook", 'fb', 'pass')
        user.create_social_account("Medium", 'med', 'pass')
        user_account = user.view_accounts()
        true_account = user.view_accounts('Instagram')
        false_account = user.view_accounts('Twitter')
        self.assertTrue(user_account)
        self.assertEqual(len(user.accounts), 3)
        self.assertTrue(true_account)
        self.assertFalse(false_account)

    def test_delete_account(self):
        self.second_new_user.register()
        user, logged = Credentials.login('second@gmail.com', 'second1123')
        user.create_social_account("Facebook")
        accounts, deleted = user.delete_account('Facebook')
        self.assertTrue(deleted)
        self.assertEqual(len(accounts), 0)


if __name__ == "__main__":
    unittest.main()
