import config
from santa import Santa
import smtplib

class Letter(object):
    def __init__(self, from_name, from_email, subject, greeting, body):
        self.from_name = from_name
        self.from_email = from_email
        self.subject = subject
        self.greeting = greeting
        self.body = body

    def text(self, santa, test=False):
        if test:
            text = '{:12} -> {}\n'.format(
                       santa.name,
                       santa.get_recipient().name
                   )
        else:
            text = 'From: {} <{}>\n' \
                   'To: {} <{}>\n' \
                   'Subject: {}\n' \
                   '\n' \
                   '{}\n' \
                   '{}\n'.format(
                        self.from_name,
                        self.from_email,
                        santa.name,
                        santa.email,
                        self.subject,
                        self.greeting,
                        self.body
                    )

            text = text.replace('{santa}', santa.name)
            text = text.replace('{recipient}', santa.get_recipient().name)

        return text

    def send(self, santa):

        message = self.text(santa)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(config.smtp_user, config.smtp_pass)
            server.sendmail(self.from_email, [santa.email], message)
            server.close()

            print('Successfully mailed letter to {}!'.format(santa.name))
        except Exception as e:
            print('Error: Failed to mail letter: {}'.format(e))
