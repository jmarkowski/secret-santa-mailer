class Santa(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        assert isinstance(recipient, Santa)
        self._recipient = recipient
