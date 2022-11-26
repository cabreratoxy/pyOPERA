"""Tests for opera.py in pyopera"""
import os

from pyopera.opera.opera import easy_opera


class TestOpera:
    """Main test class for the easy_opera function."""

    def test_opera_returns_predictions(self):
        """easy_opera finishes successfully."""
        smi_file = os.path.join(os.getcwd(), "tests", "test_files", "Sample_50.smi")
        output_file = os.path.join(
            os.getcwd(), "tests", "test_files", "Pred_Sample_50.csv"
        )
        print(smi_file)
        endpoints = ["logp"]
        results = easy_opera(smi_file, output_file, endpoints)
        assert len(results) > 0
