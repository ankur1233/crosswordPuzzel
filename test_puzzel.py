import unittest
from SearchAlgorithm import SearchAlgorithm


class test_puzzel(unittest.TestCase):

    def setUp(self):
        self.ROWS = 6
        self.COLS = 8
        self.testpzz = SearchAlgorithm(self.COLS, self.ROWS)

    def test_getWordsSet(self):
        """
        test to check inValid data inside list
        """
        filename = 'Listwords.txt'
        self.testpzz.getAllWords(filename)

        self.expectedResult = {'a', 'ccc', 'ddd', '0', ' '}
        self.assertNotEqual(self.expectedResult, self.testpzz.wordSet)

    def test_grid(self):
        """
        test to verify grid size with rows and cols
        """
        self.testpzz.grid()
        rows = len(self.testpzz.board)
        cols = len(self.testpzz.board[0])
        # Success
        self.assertEqual(self.ROWS, rows)
        self.assertEqual(self.COLS, cols)


if __name__ == "__main__":
    unittest.main()
