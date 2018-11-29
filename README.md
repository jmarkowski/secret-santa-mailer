# Secret Santa

This is a secret Santa script that will automatically "pull from a hat" a
recipient for each secret Santa, and then send an email to each secret Santa of
who they have.


# Requirements

*  Python3
*  A gmail account for automatic emailing


# Installation

```
git clone https://github.com/jmarkowski/secret-santa.git
```


# Usage

## Enable Automatic Emailing

*Note: Currently, the secret Santa script only works if you have a gmail account
available.*

In order to allow your gmail account to be "used by the script" to automatically
send emails, you must allow "less secure apps" to login:

1.  Log into the gmail account that will be used to automatically send the
emails.
2.  Visit https://www.google.com/settings/security/lesssecureapps
3.  Set the "Allow less secure apps" option to ON.


## Configuration

Open the `config.py` file and modify it for you and your circle of Santas.


## Test the Script

```
$ ./send-letters.py
```

This will read the `config.py` script and do a "dry run" of the various
pairings between secret Santas and recipients. It will generate an output file
as specified in `config.py` (`record_file`).

If it runs without any errors, then you're ready to send the secret Santa
emails.


## Send the emails!

```
$ ./send-letters.py --official
```

This will send out the emails and record what it sent into the file specified by
the `record_file` variable in `config.py`. Don't look at this (unless you want
to know who everyone's secret Santa is).

It will sequentially send emails to everyone.

Enjoy and have a Merry Christmas!


# Wish List

This quickly coded for fun to meet the "demands of Christmas". There are things
that I would like to improve (or perhaps anyone else who would like to
contribute?)

*  Make the configuration file a standard input file format such as an INI or
   JSON (i.e. Don't make it a python configuration file)
*  Make it compatible with non-gmail accounts
*  Allow the email configuration to be tested
