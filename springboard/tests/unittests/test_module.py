import unittest
from springboard.module import covered


class Test(unittest.TestCase):

    def test_module(self):
        import springboard
        print('springboard_package:', springboard)
        assert covered() is not None


if __name__ == '__main__':
    unittest.main()
