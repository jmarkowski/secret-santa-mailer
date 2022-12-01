import importlib
import os
import sys

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

# Need to use importlib because the filename contains a hyphen
secret_santa_mailer = importlib.import_module('secret-santa-mailer')
