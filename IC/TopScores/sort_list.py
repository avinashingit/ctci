import unittest


def sort_scores(unsorted_scores, highest_possible_score):

    integer_list = [0] * (highest_possible_score+1)
    sorted_list = []

    for i in range(len(unsorted_scores)):
        integer_list[unsorted_scores[i]] += 1

    for i in range(len(integer_list)-1, -1, -1):
        for j in range(integer_list[i]):
            sorted_list.append(i)

    return sorted_list


class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
