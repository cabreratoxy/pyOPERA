import libOPERA_Py as OPERA
opera = OPERA.initialize()
opera.OPERA('-s','Sample_50.smi','-o','Pred_Sample_50.csv','-logp','-v',1) # function in question