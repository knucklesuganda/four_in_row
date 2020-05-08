import unittest
import numpy as np
from main import Main


class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = []

        for i in range(5):
            line = [1] * 5
            line[i] = 0
            is_good = i == 0 or i == 4

            self.lines.append((line, is_good))

    def test_line_check(self):
        for i in range(len(self.lines)):
            print(self.lines[i][0], self.lines[i][1])
            self.assertEqual(Main()._check_line(self.lines[i][0]), self.lines[i][1])

    def test_vertical_line_creation(self):
        field = np.random.rand(5, 5)
        print(field, "\n\n\n")

        for i in range(field.shape[0]):
            vertical_line = [field[0][i]]

            for j in range(1, field.shape[0]):
                vertical_line.append(field[j][i])
            print(".", vertical_line)


if __name__ == '__main__':
    unittest.main()
