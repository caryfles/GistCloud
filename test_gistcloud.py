# test_gistcloud.py
"""
Tests for GistCloud module.
"""

import unittest
from gistcloud import GistCloud

class TestGistCloud(unittest.TestCase):
    """Test cases for GistCloud class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GistCloud()
        self.assertIsInstance(instance, GistCloud)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GistCloud()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
