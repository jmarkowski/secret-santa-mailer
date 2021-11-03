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
    Santa('Jan',        'jan@example.com'),
    Santa('Alisha',     'alisha@example.com'),
    Santa('Pam',        'pam@example.com'),
    Santa('Mark',       'mark@example.com'),
    Santa('Nick',       'nick@example.com'),
    Santa('Erica',      'erica@example.com'),
    Santa('Luke',       'luke@example.com'),
    Santa('Sidney',     'sidney@example.com'),
    Santa('Brittany',   'brittany@example.com'),
]

################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
################################################################################
incompatibles = {
    'Jan': ('Alisha',), # Do not allow Jan to be santa for Alisha
    'Alisha': ('Jan',), # Do not allow Alisha to be santa for Jan
    'Pam': ('Mark', 'Alisha',), # Do not allow Pam to be santa for Mark or Alisha
}

################################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
record_file = 'secret-santa-email-record.txt'
