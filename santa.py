class Santa(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.recipient = None

    def set_recipient(self, santa):
        self.recipient = santa

    def get_recipient(self):
        return self.recipient
