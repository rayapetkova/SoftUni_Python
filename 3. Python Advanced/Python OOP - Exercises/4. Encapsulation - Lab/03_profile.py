class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self.__username = value

    @password.setter
    def password(self, value):
        if len(value) < 8 or not any(el.isupper() for el in value) or not \
                any(el.isdigit() for el in value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


# Test code:

# profile_with_invalid_password = Profile('My_username', 'My-password')

# profile_with_invalid_username = Profile('Too_long_username', 'Any')

# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
