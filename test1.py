import unittest
import moj_program

class Test1TDD(unittest.TestCase):

    def test_100(self):
        wynik = moj_program.zwroc_100()
        self.assertEqual(100, wynik)

    def test_zwroc_parametr(self):
        self.(moj_program.zwroc_parametr('olek'), 'olek')

if __name__ == '__main__':
    unittest.main()
