import unittest


def find_rotation_point(words):

    start_index = 0
    end_index = len(words)-1

    while start_index <= end_index:
        midpoint = int((start_index + end_index)/2)
        if start_index+1 == end_index:
            return end_index
        if words[midpoint] >= words[0]:
            start_index = midpoint
        else:
            end_index = midpoint


actual = find_rotation_point(['a', 'b', 'c'])
print(actual)


class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
