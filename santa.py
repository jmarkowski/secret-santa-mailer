class Santa(object):
    def __init__(self, name, email, wish_list=[]):
        self.name = name
        self.email = email
        self.wish_list = wish_list
        self.recipient = None

    def set_recipient(self, santa):
        self.recipient = santa

    def get_recipient(self):
        return self.recipient
