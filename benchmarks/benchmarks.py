import os
import sys

sys.path.append("/app")
from pyopera.opera.opera import easy_opera


class EasyOperaBenchmarks:
    """Memory, and time benchmarks"""

    timeout = 999.0

    def setup(self):
        """Common code between benchmarks"""
        root_dir = os.path.split(os.path.dirname(__file__))[0]
        self.smi_file = os.path.join(root_dir, "tests", "test_files", "Sample_50.smi")
        self.output_file = os.path.join(
            root_dir, "tests", "test_files", "Pred_Sample_50.csv"
        )
        self.endpoints = ["logp", "mp"]

    def time_easy_opera(self):
        """Times the function"""
        easy_opera(self.smi_file, self.output_file, self.endpoints)

    def mem_easy_opera(self):
        """Gathers memory data on the function"""
        return easy_opera(self.smi_file, self.output_file, self.endpoints)
