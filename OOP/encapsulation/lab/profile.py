class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 >= len(value) or len(value) >= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        is_correct_len = len(value) >= 8
        contains_uppercase = len([i for i in value if i.isupper()]) > 0
        contains_digit = len([i for i in value if i.isdigit()]) > 0

        if is_correct_len and contains_digit and contains_uppercase:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'




profile_with_invalid_password = Profile('My_username', 'My-password')

