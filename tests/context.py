import importlib
import os
import sys

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

# Need to use importlib because the filename contains a hyphen
sendletters = importlib.import_module('send-letters')
