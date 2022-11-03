# Secret Santa

This secret santa script will automatically "pull from a hat" a recipient for
each secret santa and send a notification email to each santa's inbox
of who their gift recipient is.

It ensures that no one knows who their secret santa is... **not even you**! (That
is, unless you really want to know).


# Requirements

*  Python3
*  Gmail mail account (used to send the email notifications)

*NOTE: Currently, the script and these instructions only support working with a
Gmail account.*


# Instructions

## 1. Get The Script

```
git clone https://github.com/jmarkowski/secret-santa.git
```

## 2. Modify the Configuration File

Make your desired modifications to the `config.py` configuration file.

In it, you specify:

*  The list of secret santas.
*  The email template.
*  Optionally a lookup of anyone who should not be someone elses santa.


## 3. Test the Script

```
$ ./send-letters.py
```

This will read the configuration file and perform a "dry run" of the various
pairings between secret Santas and recipients. It will generate an output file
as specified by the `record_file` setting in `config.py` (by default
it is `secret-santa-email-record.txt`).


## 4. Enable Automatic Emailing

In order to allow this script to send emails using a Gmail account,
you must enable "less secure app" access:

1.  Log into the Gmail account that will be used to send the emails.
2.  Go to Gmail's [Less Secure App Access](https://www.google.com/settings/security/lesssecureapps)
3.  Set the *Allow less secure apps* option to ON.


## 5. Test SMTP configuration

Send a test email to confirm that the SMTP configuration is set up correctly:

```
$ ./send-letters.py --send-test-email you@example.com
```

If it runs without any errors, then you're ready to send the secret Santa
emails.


## 6. Send the emails!

```
$ ./send-letters.py --official
```

This will send out the emails and record what emails it sent into the file
specified by the `record_file` setting in `config.py`.

*Don't look at the contents of this file, unless you want to know who everyone's
secret Santa is!*

It will sequentially send emails to everyone.

Enjoy and have a Merry Christmas!


# Wish List

*  Add support for allowing a recipient to have a gift "wish list" that may be
   added in an email.
