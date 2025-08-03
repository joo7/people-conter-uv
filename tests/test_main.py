import unittest
from main import create_df
class TestMain(unittest.TestCase):
    def test_example(self):
        print("Running test_example")
        df = create_df([1, 2, 3])
        self.assertEqual(len(df), 3)
        print("DataFrame created successfully:", df)    