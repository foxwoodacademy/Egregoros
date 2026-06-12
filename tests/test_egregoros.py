import unittest
import sys
import os

# Append src path for local resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from egregoros import main

class TestEgregorosCore(unittest.TestCase):
    def setUp(self):
        self.engine = EgregorosEngine(target_id="TEST_UNIT")

    def test_initialization(self):
        self.assertEqual(self.engine.target_id, "TEST_UNIT")
        self.assertIsNotNone(self.engine.initialized_at)

    def test_missing_payload_handling(self):
        result = self.engine.harvest_prana("/tmp/non_existent_voice_file.wav")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
