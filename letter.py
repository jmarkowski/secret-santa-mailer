import smtplib

from santa import Santa


class Letter(object):
    def __init__(self, from_name, from_email, subject, body):
        self.from_name = from_name
        self.from_email = from_email
        self.subject = subject
        self.body = body

    def get_email_message(self, santa):
        message = \
            f'From: {self.from_name} <{self.from_email}>\n' \
            f'To: {santa.name} <{santa.email}>\n' \
            f'Subject: {self.subject}\n\n' \
            f'{self.body}\n'

        message = message.replace('{santa}', santa.name)
        message = message.replace('{recipient}', santa.recipient.name)

        return message

    def send(self, santa, smtp_settings):

        message = self.get_email_message(santa)

        try:
            server = smtplib.SMTP(smtp_settings['host'], smtp_settings['port'])
            server.starttls()
            server.login(smtp_settings['username'], smtp_settings['password'])
            server.sendmail(self.from_email, [santa.email], message.encode('utf-8'))
            server.close()

            print('Successfully mailed letter to {}!'.format(santa.name))
        except Exception as e:
            print('Error: Failed to mail letter: {}'.format(e))
