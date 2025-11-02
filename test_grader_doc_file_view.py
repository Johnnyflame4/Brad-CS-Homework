"""Unit tests for doc_file_view.py functions
"""

import unittest
import sys
import re
import os

import doc_file_view    # type: ignore


clean_spaces = lambda string: re.sub(r"\s+", "", string)


class TestGraderDocFileView(unittest.TestCase):
    """Test cases for doc_file_view.py functions"""

    def test_stats_to_json_basic(self) -> None:
        """Test stats_to_json with basic input"""
        result = doc_file_view.stats_to_json((1, 2, 3, 4, 5))
        expected = '{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'
        self.assertEqual(clean_spaces(result), clean_spaces(expected))

    def test_stats_to_json_zeros(self) -> None:
        """Test stats_to_json with all zeros"""
        result = doc_file_view.stats_to_json((0, 0, 0, 0, 0))
        expected = '{"lines": 0, "words": 0, "vowels": 0, "palindromes": 0, "sentence_palindromes": 0}'
        self.assertEqual(clean_spaces(result), clean_spaces(expected))

    def test_stats_to_json_large_numbers(self) -> None:
        """Test stats_to_json with large numbers"""
        result = doc_file_view.stats_to_json((100, 1000, 500, 25, 5))
        expected = '{"lines": 100, "words": 1000, "vowels": 500, "palindromes": 25, "sentence_palindromes": 5}'
        self.assertEqual(clean_spaces(result), clean_spaces(expected))

    def test_write_json_file_basic(self) -> None:
        """Test write_json_file creates correct output"""
        test_stats = (3, 15, 20, 2, 1)
        test_filename = "test_grader_output.json"
        
        doc_file_view.write_json_file(test_stats, test_filename)
        
        # Verify file was created and has correct content
        self.assertTrue(os.path.exists(test_filename))
        
        with open(test_filename, "r") as f:
            content = f.read()
        
        expected = '{"lines": 3, "words": 15, "vowels": 20, "palindromes": 2, "sentence_palindromes": 1}'
        self.assertEqual(clean_spaces(content), clean_spaces(expected))
        
        # Clean up
        if os.path.exists(test_filename):
            os.remove(test_filename)

    def test_read_file_with_data(self) -> None:
        """Test read_file with sample data"""
        # Create a test file
        test_content = "Line 1\nLine 2\n\nLine 4\n  Line 5 with spaces  \n"
        test_filename = "test_grader_input.txt"
        
        with open(test_filename, "w") as f:
            f.write(test_content)
        
        result = doc_file_view.read_file(test_filename)
        expected = ("Line 1", "Line 2", "Line 4", "Line 5 with spaces")
        
        self.assertEqual(result, expected)
        
        # Clean up
        if os.path.exists(test_filename):
            os.remove(test_filename)

    def test_read_file_empty(self) -> None:
        """Test read_file with empty file"""
        test_filename = "test_grader_empty.txt"
        
        with open(test_filename, "w") as f:
            pass  # Create empty file
        
        result = doc_file_view.read_file(test_filename)
        expected = ()
        
        self.assertEqual(result, expected)
        
        # Clean up
        if os.path.exists(test_filename):
            os.remove(test_filename)


if __name__ == "__main__":
    unittest.main()