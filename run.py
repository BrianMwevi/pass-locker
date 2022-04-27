#!/usr/bin/env python3.8
import os
import sys
from time import sleep
from credentials import Credentials


def create_user():
    email = request('Enter email address')
    password = request('Enter password')
    new_user = Credentials(email, password)
    print_message("Registration successful...\n")
    return new_user.register()


def user_login():
    email = request("Email")
    password = request("Password", True)
    os.system('cls|clear')
    print("Authenticating", end='')
    print_message("..................")
    sleep(0.8)
    user, logged_in = Credentials.login(email, password)
    if logged_in:
        print_message(
            '\nLogin successful!\n\n ')
        sleep(1)
        return [user, logged_in]
    else:
        print("\nWrong email or password, please try again")
        return user_login()


def create_credentials(user, platform, username=None, password=None):
    if username and password:
        new_account, created = user.create_social_account(
            platform, username, password)
        if created:
            print_message("\nAccount created successfully!\n")
            print_account(new_account)
    else:
        new_account, created = user.create_social_account(
            platform)
        if created:
            print_message("\nAccount created successfully!\n")
            print_message("Username and password are auto-generated\n")
            print_account(new_account)
    return new_account


def ask_username_and_password(user, account_name):
    action = request(
        f"\nDo you want to provide username and password for {account_name}? [N/y]").lower()
    if action == "" or action == 'n':
        create_credentials(user, account_name)
    elif action == 'y':
        username = request("Enter login username")
        password = request("Enter login password")
        create_credentials(user, account_name, username, password)


def edit_account(user, count_error=0):
    account_name = request("Which account do you want to edit?")
    print(count_error)

    user, account = user.get_account(account_name)
    if account:
        username = request(f"Enter new username for {account_name}")
        password = request(f"Enter new password {account_name}")

        new_account = user.edit_account(account_name, username, password)
        print_message("Account updated successfully!\n")
        return print_account(new_account)

    else:
        print("No such account, try again\n")
        show_accounts()
        return edit_account(user, count_error=+1)


def show_accounts(user):
    accounts = user.view_accounts()
    if not accounts:
        print_message("\nYou have no accounts\n\n")
        action = request("Do you want to create one? [Y/n]")
        if action == 'y' or action == '':
            return create_credentials(user, request("Enter name of the account"))
        else:
            return False
    else:
        print_message(f"\nYou've {len(accounts)} accounts\n")
        for account in accounts:
            print_account(account)
        return True


def print_account(account, speed=0.03):
    print_message(f'Account: {account["account_name"]}\n', '', speed)
    print_message(f'Username: {account["username"]}\n', '', speed)
    print_message(f'Password: {account["password"]}\n\n', '', speed)


def get_acccount(user, account_name):
    return user.get_account(account_name)


def logout(user):
    return user.logout()


def update_password(user, old_password, new_password):
    return user.update_password(old_password, new_password)


def delete_account(user, account_name):
    account_name = request("Enter account name to delete")
    accounts, deleted = user.delete_account(account_name)
    if deleted:
        print_message(
            f"{account_name} account deleted successfully!\n")
        show_accounts(user)
    else:
        print_message("No such account, please try again")
        show_accounts(user)
        return delete_account(user, account_name)


def request(ask, hide_input=False):
    return input(f'{ask}: ') if hide_input else input(f'{ask}: ')


def print_message(ask, prefix='', speed=0.04):
    print(prefix, end='')
    for i in range(len(ask)):
        sys.stdout.flush()
        print(ask[i], end='')
        sleep(speed)
    return sleep(0.3)


def show_codes(speed=0.04):
    print_message("Create account: c\n", '>>> ', speed)
    print_message("Show accounts: s\n",  '>>> ', speed)
    print_message("Edit account: e\n",  '>>> ', speed)
    print_message("Delete account: d\n",  '>>> ', speed)
    print_message("Change user password: cup\n",  '>>> ', speed)
    print_message("Quit app: q\n",  '>>> ', speed)
    print_message("Show navigation: nav\n",  '>>> ', speed)
    return request('\nEnter action to perform')


def main():
    os.system('cls|clear')
    sleep(0.8)
    print_message("Hello! ")
    sleep(0.8)
    print_message("Welcome to Pass Locker App\n")
    sleep(0.8)
    print_message('Please register below\n\n')
    create_user()
    print("\nPlease login...")

    user, logged_in = user_login()
    os.system('cls|clear')
    print_message('Use below shortcodes to navigate the app\n\n')
    speed = 0.04
    while True:
        action = show_codes(speed).lower()
        speed = 0
        if action == "c":
            os.system('cls|clear')
            sleep(0.8)
            account_name = request("Enter name of account")
            ask_username_and_password(user, account_name)

        elif action == 's':
            os.system('cls|clear')
            show_accounts(user)

        elif action == 'e':
            os.system('cls|clear')
            has_account = show_accounts(user)
            if has_account:
                edit_account(user)
        elif action == 'd':
            has_account = show_accounts(user)
            if has_account:
                delete_account(user, account_name)

        elif action == "nav":
            show_codes()
        elif action == 'cup':
            print_message("Functionality will be available soon\n\n", '', 0.03)
            sleep(0.8)
        elif action == "q":
            os.system('cls|clear')
            print("\n" * 17)
            print_message("It was nice sticking around!")
            print_message(
                "\n______________________________________ See You Soon, Bye ______________________________________\n")
            break
        else:
            print("\nPlease select an action from below shortcodes")


if __name__ == "__main__":
    main()
