class Supervisor:
    def __init__(self, username, password, phone_number=None):
        self.username = username
        self.password = password
        self.phone_number = phone_number

    @classmethod
    def sample(cls):
        return cls("yasin", "12344")
