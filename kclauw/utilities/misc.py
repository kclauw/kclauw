import numpy as np 
import random 

def seed_everything(seed : int, torch : bool = True):
    
    if torch:
        # set seeds for determinism
        torch.manual_seed(seed)
        #torch.set_default_dtype(dtype)
        
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
            torch.backends.cudnn.deterministic = True

    np.random.seed(seed)
    random.seed(seed)