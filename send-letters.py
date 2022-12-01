#!/usr/bin/env python3
import argparse
import random
import re

from santa import Santa
from letter import Letter


class SecretSantaError(Exception):
    pass


def is_santa_list_compatible(santas_lst, incompatibles):
    for k in range(len(santas_lst)):
        a = k % len(santas_lst)
        b = (k + 1) % len(santas_lst)

        santa, recipient = santas_lst[a].name, santas_lst[b].name

        if santa in incompatibles and \
                recipient in incompatibles[santa]:
            return False

    return True


def send_letter(config, santa, dry_run):
    letter = Letter(
        from_name=config['letter']['from_name'],
        from_email=config['letter']['from_email'],
        subject=config['letter']['subject'],
        body=config['letter']['body'],
    )

    with open(config['record_file'], 'a') as f:
        message = letter.get_email_message(santa)
        f.write(message)
        f.write('*' * 80 + '\n')

    if not dry_run:
        letter.send(santa, smtp_settings=config['smtp'])


def set_recipients(santas):

    for k in range(len(santas) - 1):
        santas[k].recipient = santas[k+1]

    santas[-1].recipient = santas[0]


def parse_arguments():
    parser = argparse.ArgumentParser(
              description='Auto-send Secret Santa letters!')

    parser.add_argument('--official',
        dest='official',
        action='store_true',
        help='Actually send the secret santa emails (for real!)')

    parser.add_argument('--send-test-email',
        dest='email',
        type=str,
        help='Send a test email to EMAIL to check if SMTP settings ' \
                'are correctly configured')

    return parser.parse_args()


def is_email_valid(email):
    email_regex = r'[^@\s]+@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9]+)+$'

    return re.match(email_regex, email)


def check_emails(santas):
    for santa in santas:
        if not is_email_valid(santa.email):
            raise SecretSantaError(
                    f'{santa.name} has an invalid email: {santa.email}')


def check_compatibilities(santas, incompatibles):
    santa_names = tuple(map(lambda s: s.name, santas))

    for name in incompatibles:
        if name not in santa_names:
            raise SecretSantaError(
                    f'Unknown santa in incompatible list: {name}. ' \
                     'Please check spelling')

        for incompatible_recipient in incompatibles[name]:
            if incompatible_recipient not in santa_names:
                raise SecretSantaError(
                        f'Unknown incompatible recipient for {name}: ' \
                        f'{incompatible_recipient}. Please check spelling.')


        if not isinstance(incompatibles[name], tuple):
            raise SecretSantaError(
                    f'The incompatible list for {name} must be a tuple')

        num_incompatible_recipients = len(incompatibles[name])
        num_possible_recipients = len(santas) - 1 - num_incompatible_recipients

        if num_possible_recipients == 0:
            raise SecretSantaError(
                    f'{name} has no option for a recipient! Check the ' \
                    '\'incompatibles\' list in the configuration file.')


def send_secret_santa_emails(config, args):
    santas = list(map(lambda s: Santa(s[0], s[1]), config['santas'].items()))

    check_emails(santas)
    check_compatibilities(santas, config['incompatibles'])

    # Clear contents of the file
    open(config['record_file'], 'w').close()

    while True:
        random.shuffle(santas)

        if is_santa_list_compatible(santas, config['incompatibles']):
            break

    set_recipients(santas)

    dry_run = not args.official

    if dry_run:
        print('>>> TESTING: Performing a sample dry-run ...')
    else:
        print('>>> Officially sending all secret santa emails ...\n')

    for k in sorted(santas):
        send_letter(config, k, dry_run)

    print('\nMail record saved to: {}'.format(config['record_file']))


def send_test_email(config, to_email):
    test_santa = Santa('Test Santa', to_email)
    test_santa.recipient = Santa('Test Recipient', None)

    letter = Letter(
        from_name=config['letter']['from_name'],
        from_email=config['letter']['from_email'],
        subject=config['letter']['subject'],
        body=config['letter']['body'],
    )

    letter.send(test_santa, smtp_settings=config['smtp'])


def read_config(file_path):
    config = dict()

    try:
        with open(file_path, mode='rb') as f:
            exec(compile(f.read(), file_path, 'exec'), config)
    except FileNotFoundError as e:
        print(f'Configuration file ({config_path}) missing')
        raise

    return config


def main():
    args = parse_arguments()

    config = read_config('config.py')

    if args.email:
        send_test_email(config, args.email)
    else:
        send_secret_santa_emails(config, args)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Uh oh, something failed: {}'.format(e))
