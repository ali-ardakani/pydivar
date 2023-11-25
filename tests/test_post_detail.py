import unittest
from unittest.mock import patch

from pydivar import PostDetailService

class TestPostDetailService(unittest.TestCase):
    
    @patch('pydivar.PostDetailService.get_post_details')
    def test_get_post_details(self, mock_get_post_details):
        """Test retrieving post details"""
        token = "some-token"
        
        details = PostDetailService().get_post_details(token)
        
        mock_get_post_details.assert_called_with(token)
        
    def test_get_post_details_default_params(self):
        """Test retrieving post details with default parameters"""
        details = PostDetailService().get_post_details(token="some-token")
        
        self.assertIsNotNone(details)
        
if __name__ == '__main__':
    unittest.main()