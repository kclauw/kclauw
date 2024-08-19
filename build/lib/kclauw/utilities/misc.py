import numpy as np 
import random 

from omegaconf import OmegaConf
import json
import hashlib


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
    
def create_hash_from_config_list(cfg_list):
    """
    Create a SHA-256 hash from a list of Hydra config items.
    
    Args:
        cfg_list (list): A list of Hydra config items to hash.
    
    Returns:
        str: The resulting SHA-256 hash as a hexadecimal string.
    """
    
    # Combine all dictionaries into a single dictionary
    combined_dict = {}
    for i, cfg_item in enumerate(cfg_list):
        cfg_dict = OmegaConf.to_container(cfg_item, resolve=True)
        combined_dict[f'config_{i}'] = cfg_dict
    
    # Convert the combined dictionary to a JSON string
    combined_str = json.dumps(combined_dict, sort_keys=True)
    
    # Create a SHA-256 hash of the combined string
    sha256 = hashlib.sha256()
    sha256.update(combined_str.encode('utf-8'))
    combined_hash_hex = sha256.hexdigest()
    
    return combined_hash_hex