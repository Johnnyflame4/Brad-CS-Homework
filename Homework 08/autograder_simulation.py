#!/usr/bin/env python3
"""
Mimics autograder test structure to verify module imports work
"""

import sys
import os

print("=== Autograder Import Simulation ===")
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path[:3]}...")  # Show first 3 entries

# Test 1: Try importing like autograder would
print("\n1. Testing direct imports (like autograder):")
try:
    import doc_file_view
    print("✓ doc_file_view import successful")
    
    # Test a function
    result = doc_file_view.stats_to_json((1, 2, 3, 4, 5))
    expected = '{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'
    if result == expected:
        print("✓ doc_file_view.stats_to_json works correctly")
    else:
        print(f"✗ doc_file_view.stats_to_json returned: {result}")
        
except ImportError as e:
    print(f"✗ doc_file_view import failed: {e}")
except Exception as e:
    print(f"✗ doc_file_view error: {e}")

try:
    import doc_stats
    print("✓ doc_stats import successful")
    
    # Test a function
    result = doc_stats.get_input_file(['python', 'doc_stats.py', '-f', 'test.txt'])
    if result == 'test.txt':
        print("✓ doc_stats.get_input_file works correctly")
    else:
        print(f"✗ doc_stats.get_input_file returned: {result}")
        
except ImportError as e:
    print(f"✗ doc_stats import failed: {e}")
except Exception as e:
    print(f"✗ doc_stats error: {e}")

# Test 2: Check if files exist in expected locations
print("\n2. Checking file locations:")
files_to_check = [
    'doc_file_view.py',
    'doc_stats.py', 
    'doc_stats_builder.py',
    'doc_view.py',
    'word_lib.py'
]

for filename in files_to_check:
    if os.path.exists(filename):
        print(f"✓ {filename} exists in current directory")
    else:
        print(f"✗ {filename} missing from current directory")

# Test 3: Check dependencies
print("\n3. Testing dependencies:")
try:
    import doc_stats_builder
    print("✓ doc_stats_builder import successful")
except ImportError as e:
    print(f"✗ doc_stats_builder import failed: {e}")

try:
    import word_lib
    print("✓ word_lib import successful")
except ImportError as e:
    print(f"✗ word_lib import failed: {e}")

try:
    import doc_view
    print("✓ doc_view import successful")
except ImportError as e:
    print(f"✗ doc_view import failed: {e}")

print("\n=== Simulation complete ===")
print("If all imports show ✓, then autograder should work!")