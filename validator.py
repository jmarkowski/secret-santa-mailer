import re


email_regex = r'[^@\s]+@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9]+)+$'


class ValidateError(Exception):
    pass


def validate_email(email):
    if not re.match(email_regex, email):
        raise ValidateError('Invalid email: {}'.format(email))
