import unittesting

from pytestpackage.core.core import Core

class CoreUnitTest(unittesting.TestCase):

    def test_core(self):

        c = Core()
        
        self.assertEqual(True, True)
