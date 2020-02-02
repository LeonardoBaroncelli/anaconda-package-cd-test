import unittest

from pytestpackage.core.core import Core

class CoreUnitTest(unittest.TestCase):

    def test_core(self):

        c = Core()

        self.assertEqual(True, True)

if __name__ == "__main__":

    unittest.main()
