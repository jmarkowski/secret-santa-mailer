class Santa(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.recipient = None

    def __str__(self):
        if isinstance(self.recipient, Santa):
            return f'{self.name:12} -> {self.recipient.name}'

        return f'{self.name:12}'
