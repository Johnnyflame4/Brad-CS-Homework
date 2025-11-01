"""
Auto-grader test file for doc_stats.py
This file contains tests that the autograder expects to find.
"""

import unittest
import sys
import os

import doc_stats  # type: ignore


class TestGraderDocStats(unittest.TestCase):
    """Test cases for doc_stats.py functions"""

    def test_get_input_file_basic(self) -> None:
        """Test get_input_file with basic input"""
        args = ['python', 'doc_stats.py', '-f', 'test.txt']
        result = doc_stats.get_input_file(args)
        self.assertEqual(result, 'test.txt')

    def test_get_input_file_no_flag(self) -> None:
        """Test get_input_file with no -f flag"""
        args = ['python', 'doc_stats.py']
        result = doc_stats.get_input_file(args)
        self.assertEqual(result, '')

    def test_get_input_file_mixed_args(self) -> None:
        """Test get_input_file with mixed arguments"""
        args = ['python', 'doc_stats.py', '-o', 'output.txt', '-f', 'input.txt']
        result = doc_stats.get_input_file(args)
        self.assertEqual(result, 'input.txt')

    def test_get_input_file_exception_no_filename(self) -> None:
        """Test get_input_file raises exception when no filename provided"""
        args = ['python', 'doc_stats.py', '-f']
        with self.assertRaises(ValueError):
            doc_stats.get_input_file(args)

    def test_get_input_file_exception_flag_as_filename(self) -> None:
        """Test get_input_file raises exception when flag provided as filename"""
        args = ['python', 'doc_stats.py', '-f', '-o']
        with self.assertRaises(ValueError):
            doc_stats.get_input_file(args)

    def test_get_output_file_basic(self) -> None:
        """Test get_output_file with basic input"""
        args = ['python', 'doc_stats.py', '-o', 'output.json']
        result = doc_stats.get_output_file(args)
        self.assertEqual(result, 'output.json')

    def test_get_output_file_no_flag(self) -> None:
        """Test get_output_file with no -o flag"""
        args = ['python', 'doc_stats.py']
        result = doc_stats.get_output_file(args)
        self.assertEqual(result, '')

    def test_get_output_file_default(self) -> None:
        """Test get_output_file returns default when no filename provided"""
        args = ['python', 'doc_stats.py', '-o']
        result = doc_stats.get_output_file(args)
        self.assertEqual(result, 'out.txt')

    def test_get_output_file_default_with_flag(self) -> None:
        """Test get_output_file returns default when followed by another flag"""
        args = ['python', 'doc_stats.py', '-o', '-f', 'test.txt']
        result = doc_stats.get_output_file(args)
        self.assertEqual(result, 'out.txt')

    def test_check_args_for_help_no_help(self) -> None:
        """Test check_args_for_help returns False when no help flag"""
        args = ['python', 'doc_stats.py', '-f', 'test.txt']
        result = doc_stats.check_args_for_help(args)
        self.assertFalse(result)

    def test_check_args_for_help_short_flag(self) -> None:
        """Test check_args_for_help returns True with -h flag"""
        args = ['python', 'doc_stats.py', '-h']
        # Capture output to avoid printing during tests
        import io
        from contextlib import redirect_stdout
        with redirect_stdout(io.StringIO()):
            result = doc_stats.check_args_for_help(args)
        self.assertTrue(result)

    def test_check_args_for_help_long_flag(self) -> None:
        """Test check_args_for_help returns True with --help flag"""
        args = ['python', 'doc_stats.py', '--help']
        # Capture output to avoid printing during tests
        import io
        from contextlib import redirect_stdout
        with redirect_stdout(io.StringIO()):
            result = doc_stats.check_args_for_help(args)
        self.assertTrue(result)

    def test_get_stats_block_basic(self) -> None:
        """Test get_stats_block function"""
        test_doc = ("Hello world", "This is a test")
        result = doc_stats.get_stats_block(test_doc)
        
        # Should return a tuple with 5 elements
        self.assertEqual(len(result), 5)
        self.assertIsInstance(result, tuple)
        
        # All elements should be integers
        for stat in result:
            self.assertIsInstance(stat, int)


if __name__ == "__main__":
    unittest.main()