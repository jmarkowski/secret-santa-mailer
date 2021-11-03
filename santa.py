from functools import total_ordering


@total_ordering
class Santa(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.recipient = None

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    def __lt__(self, other):
        assert isinstance(other, Santa)
        return self.name.lower() < other.name.lower()

    def __str__(self):
        if isinstance(self.recipient, Santa):
            return f'{self.name:12} -> {self.recipient.name}'

        return f'{self.name:12}'
