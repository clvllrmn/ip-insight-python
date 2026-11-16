import tempfile
import unittest
from pathlib import Path

from report_export import build_report, save_report


class TestReportExport(unittest.TestCase):

    def setUp(self):
        self.sample = {
            "ipv4": "8.8.8.8",
            "ipv6": None,
            "details": {
                "country_name": "United States",
                "city": "Mountain View"
            }
        }

    # TC-01: Validate IPv4 output
    def test_report_includes_ipv4(self):
        report = build_report(self.sample)
        self.assertIn("8.8.8.8", report)

    # TC-02: Missing IPv6
    def test_missing_ipv6_is_readable(self):
        report = build_report(self.sample)
        self.assertIn("IPv6       : Not available", report)

    # TC-03: Validate location
    def test_report_includes_location(self):
        report = build_report(self.sample)
        self.assertIn("Mountain View", report)

    # TC-04: Export TXT file
    def test_save_creates_file(self):
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "report.txt"
            path = save_report(self.sample, filename)

            self.assertTrue(path.exists())
            content = path.read_text(encoding="utf-8")
            self.assertIn("8.8.8.8", content)

    # TC-05: Missing optional information
    def test_save_handles_missing_details(self):
        data = {
            "ipv4": None,
            "ipv6": None,
            "details": {}
        }

        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "report.txt"
            path = save_report(data, filename)

            content = path.read_text(encoding="utf-8")
            self.assertIn("Not available", content)


if __name__ == "__main__":
    unittest.main()
