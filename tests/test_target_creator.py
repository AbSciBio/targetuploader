import unittest
import json
import os
from lib.target_creator import TargetCreator

here = os.path.dirname(os.path.abspath(__file__))
mock_target = os.path.join(here, "mock-target.json")
mock_user_input = os.path.join(here, "mock-user-input.json")

class TestTargetCreator(unittest.TestCase):

  def setUp(self):
    path_to_mock_target = open(mock_target)
    path_to_mock_user_input = open(mock_user_input)

    self.mock_target = json.load(path_to_mock_target)
    self.mock_user_input = json.load(path_to_mock_user_input)
    self.mock_TargetCreator = TargetCreator(self.mock_user_input)

  
  def test_parse_genes(self):
    mock_targets = self.mock_TargetCreator(self.mock_user_input)
    print('hi from parse genes')
    print(mock_targets)
