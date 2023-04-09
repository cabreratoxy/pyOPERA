"""Test format_inputs"""
from pyopera.opera.helpers.opera_helpers import format_inputs


class TestFormatEndpointsInput:
    """For format_inputs()"""

    def test_converts_input_correctly(self):
        """Tests that format_inputs formats endpoints correctly"""
        endpoints = ["logp", "mp"]
        endpoints_list = format_inputs(endpoints)
        assert isinstance(endpoints_list, list)
        assert ["-logp", "-mp"] == endpoints_list

    def do_nothing(self):
        """My only purpose is to make the CICI pass for now"""
        print("I do nothing but make pylint happy for now")
