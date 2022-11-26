"""
Contains the various functions to run the OPERA model.
"""
import libOPERA_Py as OPERA


def easy_opera(smi_file: str, output_file: str, endpoints: list) -> dict:
    """Wrapper function to run the OPERA MATLAB model with ease.

    Args:
        smi_file (str - path): .smi file containing molecular structures
        output_file (str - path): output file for prediction results
        endpoints (list): List of endpoints to calculate

    Returns:
        dict: key/value pairs of predictions
    """
    opera = OPERA.initialize()
    return opera.OPERA("-s", smi_file, "-o", output_file, "-logp", "-v", 1)
