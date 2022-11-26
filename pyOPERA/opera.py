import libOPERA_Py as OPERA


def opera(smi_file, output_file, endpoints):
    opera = OPERA.initialize()
    return opera.OPERA("-s", smi_file, "-o", output_file, "-logp", "-v", 1)