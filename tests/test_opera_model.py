"""Tests for opera.py in pyopera"""
import os

from pyopera.opera import easy_opera


class TestOpera:
    def test_opera_returns_predictions(self):
        smi_file = os.path.join(
            os.path.dirname(__file__), "test_files", "Sample_50.smi"
        )
        output_file = os.path.join(
            os.path.dirname(__file__), "test_files", "Pred_Sample_50.csv"
        )
        endpoints = ["logp"]
        results = easy_opera(smi_file, output_file, endpoints)
        assert len(results) > 0
