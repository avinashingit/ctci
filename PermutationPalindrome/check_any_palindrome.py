'''
Write an efficient function that checks whether any permutation ↴ of an input
string is a palindrome.

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
'''

import unittest


def has_palindrome_permutation(the_string):

    alphabets = set()

    for character in the_string:
        if character not in alphabets:
            alphabets.add(character)
        else:
            alphabets.remove(character)

    return len(alphabets) <= 1


class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
