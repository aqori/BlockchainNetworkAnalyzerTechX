# test_blockchainnetworkanalyzertechx.py
"""
Tests for BlockchainNetworkAnalyzerTechX module.
"""

import unittest
from blockchainnetworkanalyzertechx import BlockchainNetworkAnalyzerTechX

class TestBlockchainNetworkAnalyzerTechX(unittest.TestCase):
    """Test cases for BlockchainNetworkAnalyzerTechX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNetworkAnalyzerTechX()
        self.assertIsInstance(instance, BlockchainNetworkAnalyzerTechX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNetworkAnalyzerTechX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
