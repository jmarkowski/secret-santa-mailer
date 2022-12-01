# Secret Santa Mailer

This python-based script will automatically "pull from a hat" a recipient for
every secret santa and send a notification email to each santa's inbox
of who their gift recipient is.

It ensures that no one knows who their secret santa is... **not even you**! (That
is, unless you really want to know).


# Requirements

*  Python
*  SMTP server used to automatically send emails


# Instructions

## 1. Get The Script

```
git clone https://github.com/jmarkowski/secret-santa.git
```

## 2. Modify the Configuration File

Make your desired modifications to the `config.py` configuration file.

In it, you must specify:

*  The SMTP settings as specified by your SMTP host.
*  An email template.
*  The list of secret santas.
*  Optionally a lookup of anyone who should not be someone elses santa.


## 3. Perform a Dry Run

```
$ ./secret-santa-mailer.py
```

This will read the configuration file and perform a "dry run" of the various
pairings between secret Santas and recipients. It will generate an output file
as specified by the `secret_santa_record_file` setting in `config.py`.

This record file is saved as `secret-santa-record-file.txt` by default.


## 4. Configure the SMTP settings

This script relies on a simple SMTP method of sending emails, and the SMTP
settings in `config.py` will depend on your preferred service to use.

Various SMTP server options are available. A few popular options include:

* [Sendinblue](https://www.sendinblue.com/) - Free 300 emails/day
* [Mailjet](https://www.mailjet.com/) - Free 200 emails/day
* [SendGrid](https://sendgrid.com) - Free 100 emails/day
* [Amazon SES](https://aws.amazon.com/ses/)


### Test Your SMTP configuration

Send a test email to confirm that the SMTP configuration is set up correctly:

```
$ ./secret-santa-mailer.py --send-test-email you@example.com
```

If it runs without any errors, then you're ready to send the secret Santa
emails.


## 5. Send the emails!

```
$ ./secret-santa-mailer.py --official
```

This will dispatch the emails and record what emails it sent to the file
specified by the `secret_santa_record_file` setting in `config.py`.

*Don't look at the contents of this file, unless you want to know who everyone's
secret Santa is.*

It will sequentially send emails to everyone.

Enjoy and have a Merry Christmas!


# Wish List

*  Add support for allowing a recipient to have a gift "wish list" that may be
   added in an email.
