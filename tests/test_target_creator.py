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
    self.TargetCreator = TargetCreator
    self.mock_subunits_array = self.mock_target['subunits']

  
  def test_parse_genes(self):
    for subunit in range(len(self.mock_subunits_array)):
      mock_subunit = self.mock_subunits_array[subunit]
      mock_subunit_name = mock_subunit['subunit_name']
      mock_genes_array = mock_subunit['genes']
      result_genes_array = self.TargetCreator(self.mock_user_input).parse_genes(mock_subunit_name)
      self.assertEqual(result_genes_array, mock_genes_array)
    

  def test_parse_subunits(self):
    for subunit in range(len(self.mock_subunits_array)):
      result_subunit_array = self.TargetCreator(self.mock_user_input).parse_subunits(2)
      self.assertEqual(result_subunit_array[subunit], self.mock_subunits_array[subunit])

  def test_excel_reader(self):
      result_mock_target = self.TargetCreator(self.mock_user_input).targets
      self.assertEqual(result_mock_target[0], self.mock_target)
  