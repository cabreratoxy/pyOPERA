"""Test format_endpoints_input"""
from pyopera.opera.helpers.opera_helpers import format_endpoints_input


class TestFormatEndpointsInput:
    """For format_endpoints_input()"""

    def test_converts_input_correctly(self):
        """Tests that format_endpoints_input formats endpoints correctly"""
        endpoints = ["logp", "mp"]
        endpoints_list = format_endpoints_input(endpoints)
        print(endpoints_list)
        assert isinstance(endpoints_list, str)
        assert "-logp" in endpoints_list
