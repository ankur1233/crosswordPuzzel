import datetime
import argparse
from SearchAlgorithm import SearchAlgorithm


class Puzzel(object):
    """
    Test class for WordSearch
    """

    def __init__(self, file, cols, rows):
        """
       Init rows , clos ,fileName
        """
        self.rows = rows
        self.cols = cols
        self.file = file

    def start(self):
        self.pzz = SearchAlgorithm(self.cols, self.rows)
        self.pzz.getAllWords(self.file)
        self.pzz.grid()
        result = self.getResults()
        print("total %d words found -" % (len(result)))
        print(sorted(result))

    def getResults(self):
        return self.pzz.getWords()


def play(rows_=15, cols_=15, filename_="Listwords.txt"):
    """
    Program Entry Point.
    :return:
    """
    rows = rows_
    cols = cols_
    ce = Puzzel(filename_, cols, rows)
    ce.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int)
    parser.add_argument("--cols", type=int)
    parser.add_argument("--fileName")
    args = parser.parse_args()
    play(args.rows, args.cols, args.fileName)
