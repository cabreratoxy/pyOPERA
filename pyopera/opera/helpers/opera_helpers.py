"""Helpers for the easy_opera wrapper"""


def format_endpoints_input(endpoints: list) -> str:
    """Converts list of input endpoints into command line inputs.

    Args:
        endpoints (list): list of endpoints requested

    Returns:
        str: endpoints with dashes that could be used on a CLI
    """
    dashed_endpoints = [f"-{endpoint}" for endpoint in endpoints]
    return ",".join(dashed_endpoints)
