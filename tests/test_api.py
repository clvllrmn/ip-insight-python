import unittest
from unittest.mock import patch, Mock


from api import get_public_ip, get_ip_details




class TestIPInsight(unittest.TestCase):


    @patch("api.requests.get")
    def test_ipv4(self, mock_get):
        response = Mock()
        response.json.return_value = {"ip": "8.8.8.8"}
        mock_get.return_value = response


        self.assertEqual(get_public_ip(4), "8.8.8.8")


    @patch("api.requests.get")
    def test_ipv6(self, mock_get):
        response = Mock()
        response.json.return_value = {"ip": "2001:4860:4860::8888"}
        mock_get.return_value = response


        self.assertEqual(
            get_public_ip(6), "2001:4860:4860::8888"
        )


    @patch("api.requests.get")
    def test_wrong_ip_version(self, mock_get):
        response = Mock()
        response.json.return_value = {"ip": "8.8.8.8"}
        mock_get.return_value = response


        self.assertIsNone(get_public_ip(6))


    @patch("api.requests.get")
    def test_api_error(self, mock_get):
        response = Mock()
        response.json.return_value = {"error": True}
        mock_get.return_value = response


        self.assertEqual(get_ip_details("8.8.8.8"), {})


    @patch("api.requests.get")
    def test_connection_failure(self, mock_get):
        import requests
        mock_get.side_effect = requests.ConnectionError()


        self.assertIsNone(get_public_ip(4))




if __name__ == "__main__":
    unittest.main()
