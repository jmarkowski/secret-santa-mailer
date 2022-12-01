#!/usr/bin/env python3
import argparse
import random
import re
import smtplib
from functools import total_ordering


class ConfigError(Exception):
    pass


@total_ordering
class Santa():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.recipient = None

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    def __str__(self):
        if self.recipient:
            return f'{self.name:12} -> {self.recipient.name}'

        return f'{self.name:12}'


class Mailer():
    def __init__(self,
            from_name,
            from_email,
            subject,
            body,
            smtp_settings,
            dry_run=False,
        ):
        self.from_name = from_name
        self.from_email = from_email
        self.subject = subject
        self.body = body
        self.smtp = smtp_settings
        self.dry_run = dry_run

    def render_email_message(self, santa):
        message = \
            f'From: {self.from_name} <{self.from_email}>\n' \
            f'To: {santa.name} <{santa.email}>\n' \
            f'Subject: {self.subject}\n\n' \
            f'{self.body}\n'

        message = message.replace('{santa}', santa.name)
        message = message.replace('{recipient}', santa.recipient.name)

        return message

    def send_email(self, santa):
        message = self.render_email_message(santa)

        if self.dry_run:
            return

        try:
            server = smtplib.SMTP(self.smtp['host'], self.smtp['port'])
            server.starttls()
            server.login(self.smtp['username'], self.smtp['password'])
            server.sendmail(self.from_email, [santa.email], message.encode('utf-8'))
            server.close()

            print(f'Successfully mailed letter: {santa.name} ({santa.email})')
        except Exception as e:
            print(f'Failed to mail letter: {e}\n' \
                    '(Verify that the SMTP settings are correct.)')


def is_santa_list_compatible(santas_lst, incompatibles):
    for k in range(len(santas_lst)):
        a = k % len(santas_lst)
        b = (k + 1) % len(santas_lst)

        santa, recipient = santas_lst[a].name, santas_lst[b].name

        if santa in incompatibles and \
                recipient in incompatibles[santa]:
            return False

    return True


def send_letter(mailer, config, santa):
    with open(config['secret_santa_record_file'], 'a') as f:
        message = mailer.render_email_message(santa)
        f.write(message)
        f.write('*' * 80 + '\n')

    mailer.send_email(santa)


def set_recipients(santas):
    for k in range(len(santas) - 1):
        santas[k].recipient = santas[k+1]

    santas[-1].recipient = santas[0]


def is_email_valid(email):
    email_regex = r'[^@\s]+@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9]+)+$'

    return re.match(email_regex, email)


def check_emails(santas):
    for santa in santas:
        if not is_email_valid(santa.email):
            raise ConfigError(
                    f'{santa.name} has an invalid email: {santa.email}.')


def check_compatibilities(santas, incompatibles):
    santa_names = tuple(map(lambda s: s.name, santas))

    for name in incompatibles:
        if name not in santa_names:
            raise ConfigError(
                    f'Unknown santa in incompatible list: {name}. ' \
                     'Please check spelling.')

        for incompatible_recipient in incompatibles[name]:
            if incompatible_recipient not in santa_names:
                raise ConfigError(
                        f'Unknown incompatible recipient for {name}: ' \
                        f'{incompatible_recipient}. Please check spelling.')


        if not isinstance(incompatibles[name], tuple):
            raise ConfigError(
                    f'The incompatible list for {name} must be a tuple.')

        num_incompatible_recipients = len(incompatibles[name])
        num_possible_recipients = len(santas) - 1 - num_incompatible_recipients

        if num_possible_recipients == 0:
            raise ConfigError(
                    f'{name} has no option for a recipient! Check the ' \
                    '\'incompatibles\' list in the configuration file.')


def send_secret_santa_emails(mailer, config):
    santas = list(map(lambda s: Santa(s[0], s[1]), config['santas'].items()))

    check_emails(santas)
    check_compatibilities(santas, config['incompatibles'])

    # Clear contents of the file
    open(config['secret_santa_record_file'], 'w').close()

    while True:
        random.shuffle(santas)

        if is_santa_list_compatible(santas, config['incompatibles']):
            break

    set_recipients(santas)

    if mailer.dry_run:
        print('>>> TESTING: Performing a sample dry-run ...')
    else:
        print('>>> Officially sending all secret santa emails ...\n')

    for k in sorted(santas):
        send_letter(mailer, config, k)

    print('\nMail record saved to: {}' \
          .format(config['secret_santa_record_file']))


def send_test_email(mailer, to_email):
    test_santa = Santa('Test Santa', to_email)
    test_santa.recipient = Santa('Test Recipient', None)

    mailer.send_email(test_santa)


def read_config(file_path):
    config = dict()

    try:
        with open(file_path, mode='rb') as f:
            exec(compile(f.read(), file_path, 'exec'), config)
    except FileNotFoundError as e:
        raise ConfigError(
                f'The configuration file "{file_path}" was not found.')

    return config


def parse_arguments():
    parser = argparse.ArgumentParser(
              description='Secret Santa Mailer')

    parser.add_argument('--official',
        dest='official',
        action='store_true',
        help='Officially send out all the secret santa emails')

    parser.add_argument('--send-test-email',
        dest='email',
        type=str,
        help='Send a test email to EMAIL to check if SMTP settings ' \
                'are correctly configured')

    return parser.parse_args()


def main():
    args = parse_arguments()

    config = read_config('config.py')

    mailer = Mailer(
        from_name=config['email_template']['from_name'],
        from_email=config['email_template']['from_email'],
        subject=config['email_template']['subject'],
        body=config['email_template']['body'],
        smtp_settings=config['smtp'],
        dry_run=(not args.official and not args.email),
    )

    if args.email:
        send_test_email(mailer, args.email)
    else:
        send_secret_santa_emails(mailer, config)


if __name__ == '__main__':
    try:
        main()
    except ConfigError as e:
        print(f'Configuration error:\n{e}')
