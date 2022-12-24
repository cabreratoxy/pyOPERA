"""Tests for opera.py in pyopera"""
import os

import pytest

from pyopera.opera.opera import easy_opera

from .test_helpers.test_parameters import (
    ALL_ENDPOINTS_PARAMETIZED,
    ENDPOINTS,
    SAMPLE_OF_ENDPOINTS_TOGETHER,
)


@pytest.fixture
def opera_inputs():
    """Generates opera inputs"""
    smi_file = os.path.join(os.getcwd(), "tests", "test_files", "Sample_50.smi")
    output_file = os.path.join(os.getcwd(), "tests", "test_files", "Pred_Sample_50.csv")
    return smi_file, output_file


class TestOpera:
    """Main test class for the easy_opera function."""

    @pytest.mark.parametrize("endpoints", ALL_ENDPOINTS_PARAMETIZED)
    def test_opera_returns_predictions_individual_models(self, endpoints, opera_inputs):
        """easy_opera finishes successfully with each model individually."""
        smi_file, output_file = opera_inputs
        results = easy_opera(smi_file, output_file, endpoints)
        assert len(results) > 0

    def test_opera_returns_predictions_all_models(self, opera_inputs):
        """easy_opera finishes successfully with all models at once."""
        smi_file, output_file = opera_inputs
        results = easy_opera(smi_file, output_file, ENDPOINTS)
        assert len(results) > 0

    def test_opera_returns_predictions_few_models(self, opera_inputs):
        """easy_opera finishes successfully with 5 random models together."""
        smi_file, output_file = opera_inputs
        results = easy_opera(smi_file, output_file, SAMPLE_OF_ENDPOINTS_TOGETHER)
        assert len(results) > 0
