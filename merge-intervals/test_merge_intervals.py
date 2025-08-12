import unittest
from main import merge_intervals


class TestMergeIntervals(unittest.TestCase):
    """Test cases for the merge_intervals function."""

    def test_empty_list(self):
        """Test merging an empty list of intervals."""
        self.assertEqual(merge_intervals([]), [])

    def test_single_interval(self):
        """Test merging a single interval."""
        intervals = [[1, 3]]
        expected = [[1, 3]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_two_overlapping_intervals(self):
        """Test merging two overlapping intervals."""
        intervals = [[1, 3], [2, 6]]
        expected = [[1, 6]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_two_non_overlapping_intervals(self):
        """Test merging two non-overlapping intervals."""
        intervals = [[1, 3], [8, 10]]
        expected = [[1, 3], [8, 10]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_multiple_overlapping_intervals(self):
        """Test merging multiple overlapping intervals."""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_adjacent_intervals(self):
        """Test merging adjacent intervals (touching but not overlapping)."""
        intervals = [[1, 3], [3, 6], [6, 10]]
        expected = [[1, 10]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_completely_overlapping_intervals(self):
        """Test merging intervals where one completely contains another."""
        intervals = [[1, 10], [2, 5], [3, 4]]
        expected = [[1, 10]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_with_negative_numbers(self):
        """Test merging intervals with negative numbers."""
        intervals = [[-5, -2], [-3, 1], [0, 4]]
        expected = [[-5, 4]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_with_zero(self):
        """Test merging intervals that include zero."""
        intervals = [[-2, 0], [0, 3], [2, 5]]
        expected = [[-2, 5]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_unsorted_intervals(self):
        """Test that the function works with unsorted intervals."""
        intervals = [[8, 10], [1, 3], [15, 18], [2, 6]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_with_same_start(self):
        """Test merging intervals that have the same start value."""
        intervals = [[1, 3], [1, 5], [1, 7]]
        expected = [[1, 7]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_with_same_end(self):
        """Test merging intervals that have the same end value."""
        intervals = [[1, 5], [2, 5], [3, 5]]
        expected = [[1, 5]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_single_point_intervals(self):
        """Test merging single point intervals."""
        intervals = [[1, 1], [2, 2], [3, 3]]
        expected = [[1, 1], [2, 2], [3, 3]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_mixed_single_point_and_regular_intervals(self):
        """Test merging a mix of single point and regular intervals."""
        intervals = [[1, 1], [2, 4], [3, 3], [5, 7]]
        expected = [[1, 1], [2, 4], [5, 7]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_large_numbers(self):
        """Test merging intervals with large numbers."""
        intervals = [[1000000, 2000000], [1500000, 2500000], [3000000, 4000000]]
        expected = [[1000000, 2500000], [3000000, 4000000]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_with_float_like_integers(self):
        """Test that the function works with intervals that could represent floats."""
        intervals = [[0, 100], [50, 150], [200, 300]]
        expected = [[0, 150], [200, 300]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_edge_case_minimal_overlap(self):
        """Test minimal overlap between intervals."""
        intervals = [[1, 2], [2, 3], [3, 4]]
        expected = [[1, 4]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_edge_case_maximal_overlap(self):
        """Test maximal overlap where all intervals overlap significantly."""
        intervals = [[1, 100], [2, 99], [3, 98], [4, 97]]
        expected = [[1, 100]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_reverse_sorted_intervals(self):
        """Test that the function works with reverse sorted intervals."""
        intervals = [[15, 18], [8, 10], [2, 6], [1, 3]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_duplicate_intervals(self):
        """Test merging duplicate intervals."""
        intervals = [[1, 3], [1, 3], [2, 6], [2, 6]]
        expected = [[1, 6]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_with_very_small_gaps(self):
        """Test intervals with very small gaps between them."""
        intervals = [[1, 3], [4, 6], [7, 9]]
        expected = [[1, 3], [4, 6], [7, 9]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_with_large_gaps(self):
        """Test intervals with large gaps between them."""
        intervals = [[1, 3], [100, 200], [1000, 2000]]
        expected = [[1, 3], [100, 200], [1000, 2000]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_boundary_case_exact_overlap(self):
        """Test exact boundary overlap."""
        intervals = [[1, 5], [5, 10], [10, 15]]
        expected = [[1, 15]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_boundary_case_no_overlap(self):
        """Test no overlap at boundaries."""
        intervals = [[1, 4], [5, 8], [9, 12]]
        expected = [[1, 4], [5, 8], [9, 12]]
        self.assertEqual(merge_intervals(intervals), expected)


if __name__ == "__main__":
    unittest.main()
