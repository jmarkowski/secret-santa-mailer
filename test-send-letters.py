#!/usr/bin/env python3
import importlib
import unittest

sendletters = importlib.import_module('send-letters')


class EmailTests(unittest.TestCase):

    def test_valid_basic(self):
        email = 'valid@email.com'
        sendletters.validate_email(email)

    def test_valid_with_plus(self):
        email = 'john+doe@email.com'
        sendletters.validate_email(email)

    def test_valid_complex(self):
        email = 'john.doe+lab777@some-where.com'
        sendletters.validate_email(email)

    def test_valid_domain(self):
        email = 'john.DOE+lab777@ABC-GO-NOW.AI'
        sendletters.validate_email(email)

    def test_valid_tree_sufix(self):
        email = 'valid@email.co.uk'
        sendletters.validate_email(email)

    def test_invalid_basic(self):
        email = 'invalidemail.com'
        with self.assertRaises(sendletters.SecretSantaError):
            sendletters.validate_email(email)

    def test_invalid_bad_chars(self):
        email = 'invalid email here@email.com'
        with self.assertRaises(sendletters.SecretSantaError):
            sendletters.validate_email(email)

    def test_invalid_tld(self):
        email = 'invalid-email@bad{}.com'
        with self.assertRaises(sendletters.SecretSantaError):
            sendletters.validate_email(email)

if __name__ == '__main__':
    unittest.main()
