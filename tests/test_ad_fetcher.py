import unittest
from unittest.mock import patch

from pydivar import AdFetcher

class TestAdFetcher(unittest.TestCase):

    @patch('pydivar.AdFetcher.get_ads')
    def test_get_ads(self, mock_get_ads):
        """Test retrieving ads with filters"""
        category = "light"
        sort = "sort_date" 
        cities = [16, 5]
        filters = {"body_status": ["some-scratches", "paintless-dent-removal"]}
        
        ads = AdFetcher.get_ads(
            category=category,
            sort=sort,
            cities=cities,
            filters=filters
        )
        
        mock_get_ads.assert_called_with(
            category=category,
            sort=sort, 
            cities=cities,
            filters=filters
        )

    def test_get_ads_default_params(self):
        """Test retrieving ads with default parameters"""
        ads = AdFetcher.get_ads(category="light")
        
        self.assertIsNotNone(ads)
        


if __name__ == '__main__':
    unittest.main()