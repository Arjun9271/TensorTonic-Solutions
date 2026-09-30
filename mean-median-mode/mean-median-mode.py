from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
   x = np.array(x)
   mean_val = np.mean(x)

   dici = Counter(x)
   high_freq = dici.most_common(1)[0][1]
   mode_vals = [item for item,cnt in dici.items() if cnt == high_freq]
   mode_vals = min(mode_vals)
    
   median_val = np.median(x)

   return {"mean":float(mean_val),"median":float(median_val),"mode":float(mode_vals)}

  
   
    
   
   

