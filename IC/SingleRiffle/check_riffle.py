'''
I figured out how to get rich: online poker.

I suspect the online poker game I'm playing shuffles cards by doing a single
riffle.

To prove this, let's write a function to tell us if a full deck of cards
shuffled_deck is a single riffle of two other halves half1 and half2.

We'll represent a stack of cards as a list of integers in the range 1..52
(since there are 52 distinct cards in a deck).
Why do I care? A single riffle is not a completely random shuffle. If I'm right
, I can make more informed bets and get rich and finally prove to my ex that I
 am not a "loser with an unhealthy cake obsession" (even though it's too late
 now because she let me go and she's never getting me back).
'''

import unittest


def is_single_riffle(half1, half2, shuffled_deck):

    top1 = 0
    top2 = 0
    for i in range(len(shuffled_deck)):
        if top1 != len(half1) and shuffled_deck[i] == half1[top1]:
            top1 += 1
        elif top2 != len(half2) and shuffled_deck[i] == half2[top2]:
            top2 += 1
        else:
            return False
    return True


class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


'''
This assumes shuffled_deck contains all 52 cards. What if we can't trust this
(e.g. some cards are being secretly removed by the shuffle)?
This assumes each number in shuffled_deck is unique. How can we adapt this to
rifling lists of random integers with potential repeats?
Our solution returns True if you just cut the deck—take one half and put it on
top of the other. While that technically meets the definition of a riffle, what
 if you wanted to ensure that some mixing of the two halves occurred?
Our solution iterates through the decks from front to back. Would our algorithm
work if we iterated from the back towards the front? Which approach is cleaner?
'''
