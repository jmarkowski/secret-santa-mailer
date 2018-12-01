from santa import Santa
from letter import Letter

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
    greeting="{santa}, you are {recipient}'s secret Santa!",
    body=""
)

################################################################################
# The complete list of all the secret santa's and their email addresses.
################################################################################
santas = [
    Santa('Jan',        'jan@someemail.com'),
    Santa('Alisha',     'alisha@someemail.com'),
    Santa('Pam',        'pam@someemail.com'),
    Santa('Mark',       'mark@someemail.com'),
    Santa('Nick',       'nick@someemail.com'),
    Santa('Erica',      'erica@someemail.com'),
    Santa('Luke',       'luke@someemail.com'),
    Santa('Sidney',     'sidney@someemail.com'),
    Santa('Brittany',   'brittany@someemail.com'),
]

################################################################################
# This contains a list of people that you do NOT want to be paired together...
# for whatever reason (either because they're going to gossip to each other of
# who they have as their recipient, or they just plainly can't stand the thought
# of giving each other a gift).
#
# If there are no incompatibles, leave it empty.
################################################################################
incompatibles = (
    ('Jan', 'Alisha'),
    ('Pam', 'Mark'),
    ('Nick', 'Erica'),
    ('Luke', 'Sidney'),
)

################################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
record_file = 'secret-santa-list.txt'
