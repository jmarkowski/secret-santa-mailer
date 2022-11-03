from letter import Letter
from santa import Santa

################################################################################
# This is the email address that is going to be used to dispatch all the secret
# santa letters.
#
# WARNING: These emails will appear in the "Sent" folder of the email... So be
# careful to either (a) not look in your sent folder, or (b) use an email that
# you're not planning to login with.
################################################################################
smtp_user = 'the_email_used_to_send_letters@gmail.com'
smtp_pass = 'password'
smtp_host = 'smtp.gmail.com'
smtp_port = 465

################################################################################
# This the secret santa letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automatically replaced by the secret
# santa's name, and his/her recipient of their gift.
################################################################################
letter = Letter(
    from_name='Secret Santa',
    from_email=smtp_user,
    subject='Family Christmas',
    body="""
Ho Ho Ho!

{santa}, you are {recipient}'s secret Santa!

Merry Christmas!
"""
)

################################################################################
# The complete list of all the secret santa's and their email addresses.
################################################################################
santas = [
    Santa('James',      'james@example.com'),
    Santa('Mary',       'mary@example.com'),
    Santa('Nancy',      'nancy@example.com'),
    Santa('John',       'john@example.com'),
    Santa('Michael',    'michael@example.com'),
    Santa('Lisa',       'lisa@example.com'),
    Santa('David',      'david@example.com'),
    Santa('Linda',      'linda@example.com'),
]

################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
################################################################################
incompatibles = {
    # Do not allow James to be santa for Mary
    'James': ('Mary',),

    # Do not allow Mary to be santa for James
    'Mary': ('James',),

    # Do not allow Nancy to be santa for John or Mary
    'Nancy': ('John', 'Mary',),

    # Something like below is bad, Linda can't be a secret santa for anyone!
#   'Linda': ('James', 'Mary', 'Nancy', 'John', 'Michael', 'Lisa', 'David'),
}

################################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
record_file = 'secret-santa-email-record.txt'
