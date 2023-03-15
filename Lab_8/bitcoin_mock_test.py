import unittest
from unittest.mock import patch
from bitcoin import convert_bitcoin_to_dollars

class TestBitcoinProgram(unittest.TestCase):
    @patch('bitcoin_program.get_bitcoin_data')
    def test_convert_bitcoin_to_dollars(self, mock_get_bitcoin_data):
        mock_get_bitcoin_data.return_value = {
            "time": {
                "updated": "Mar 14, 2023 00:00:00 UTC",
                "updatedISO": "2023-03-14T00:00:00+00:00"
            },
            "bpi": {
                "USD": {
                    "code": "USD",
                    "symbol": "&#36;",
                    "rate": "50,000.00",
                    "description": "United States Dollar",
                    "rate_float": 50000.00
                }
            }
        }
        
        bitcoin = 1.0
        dollars = convert_bitcoin_to_dollars(bitcoin)
        expected_dollars = 50000.00
        
        self.assertEqual(dollars, expected_dollars)

if __name__ == '__main__':
    unittest.main()