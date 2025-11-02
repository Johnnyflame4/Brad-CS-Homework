import unittest
import sys
import re
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Homework 08 ')))


import doc_stats # type: ignore


clean_spaces = lambda string: re.sub(r"\s+", "", string)


class TestDocStats(unittest.TestCase):

    def get_input_file(self) -> None:
        """Tests the -f filename option for get_input_file"""
        filename = "tests/test_files/test_file.txt"
        result = doc_stats.get_input_file(["-f", filename])
        self.assertEqual(result, filename)
        result = doc_stats.get_input_file(["hello", "-o", "-f", filename])
        self.assertEqual(result, filename)

    def test_get_output_file(self) -> None:
        """Tests the -o filename option for get_output_file"""
        filename = "test_file.txt"
        result = doc_stats.get_output_file(["-o", filename])
        self.assertEqual(result, filename)
        result = doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", filename])
        self.assertEqual(result, filename)

    def test_get_input_file_exception(self)-> None:
        """Test to make sure -f nothing -f - properly raises ValueError"""
        with self.assertRaises(ValueError):
            doc_stats.get_input_file(["-f"])
            doc_stats.get_input_file(["-f", "-"])

    def test_output_file_not_provided(self) -> None:
        """Tests that the -o nothing default is out.txt"""
        result = doc_stats.get_output_file(["-o"])
        self.assertEqual(result, "out.txt")
        result = doc_stats.get_output_file(["-o", "-f", "hello.txt"])
        self.assertEqual(result, "out.txt")



if __name__ == "__main__":
    unittest.main()
