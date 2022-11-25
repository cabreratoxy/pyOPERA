from pyOPERA.opera import opera
import os

class TestOpera:
    def test_opera_returns_predictions(self):
        smi_file = os.path.join(os.path.dirname(__file__), 'test_files', 'Sample_50.smi')
        output_file = 'Pred_Sample_50.csv'
        endpoints = ['logp']
        print(smi_file)
        results = opera(smi_file, output_file, endpoints)
        assert len(results) > 0