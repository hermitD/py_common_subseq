"""Unit tests for the calc_acs_dp all common subsequences mini-module.

@author: A. Samuel Pottinger
@license: MIT
"""

import unittest

import py_common_subseq

ALL_SHARED_1 = 'est'
ALL_SHARED_2 = 'est time'

PARTIALLY_SHARED_1 = 'qwer'
PARTIALLY_SHARED_2 = 'qewr'

NONE_SHARED_1 = 'mine'
NONE_SHARED_2 = 'yours'


class TestCalcACS(unittest.TestCase):
    """Test suite for the py_common_subseq mini-module."""

    def test_count_common_subsequences(self):
        """Test counting the number of subsequences without listing them."""
        no_shared = py_common_subseq.count_common_subsequences(NONE_SHARED_1,
            NONE_SHARED_2)
        self.assertEqual(no_shared, 1)

        partially_shared = py_common_subseq.count_common_subsequences(
            PARTIALLY_SHARED_1, PARTIALLY_SHARED_2)
        self.assertEqual(partially_shared, 12)

        all_shared = py_common_subseq.count_common_subsequences(ALL_SHARED_1,
            ALL_SHARED_2)
        self.assertEqual(all_shared, 8)

    def test_find_common_subsequences(self):
        """Test getting a list of subseqeunces between two sequences."""
        no_shared = py_common_subseq.find_common_subsequences(NONE_SHARED_1,
            NONE_SHARED_2)
        self.assertEqual(no_shared, set(['']))

        partially_shared = py_common_subseq.find_common_subsequences(
            PARTIALLY_SHARED_1, PARTIALLY_SHARED_2)
        components = ['', 'qer', 'wr', 'qwr', 'er', 'qr', 'e', 'qw', 'q', 'r',
            'qe', 'w']
        self.assertEqual(partially_shared, set(components))

        all_shared = py_common_subseq.find_common_subsequences(ALL_SHARED_1,
            ALL_SHARED_2)
        components = ['', 'e', 's', 't', 'es', 'st', 'et', 'est']
        self.assertEqual(all_shared, set(components))


if __name__ == '__main__':
    unittest.main()