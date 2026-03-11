"""Module is design for testing WebService class"""
from unittest import TestCase
from unittest.mock import patch, MagicMock
from assignment_8_testing.web_service import WebService


class WebServiceTest(TestCase):
    """Tests for WebService class."""

    def setUp(self) -> None:
        """Creates WebService instance before each test."""
        self.web_service = WebService()

    @patch("requests.get")
    def test_get_data_successful_response(self, mock_request) -> None:
        """Test get_data for getting successful response."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_request.return_value = mock_response

        self.assertEqual(self.web_service.get_data("https://github.com"), {"data": "test"})

    @patch("requests.get")
    def test_get_data_failed_response(self, mock_request) -> None:
        """Test get_data for getting failed response."""
        mock_response = MagicMock(status_code=403)
        mock_request.return_value = mock_response

        with self.assertRaises(Exception):
            self.web_service.get_data("https://github.com")
