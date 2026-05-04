from typing import List, Dict, Tuple, Optional, Union
import numpy as np

# Without type hints — hard to read
def process_data(data, threshold, return_indices):
    pass

# With type hints — professional, self-documenting
def process_data(
    data: np.ndarray,
    threshold: float = 0.5,
    return_indices: bool = False
) -> Union[np.ndarray, Tuple[np.ndarray, np.ndarray]]:
    """
    Filter array values above threshold.
    
    Args:
        data: Input array of shape (n,) or (n, m)
        threshold: Minimum value to keep
        return_indices: If True, also return indices of kept values
        
    Returns:
        Filtered array, or (filtered array, indices) if return_indices=True
    """
    mask = data > threshold
    filtered = data[mask]
    if return_indices:
        indices = np.where(mask)[0]
        return filtered, indices
    return filtered

# Test it
arr = np.array([0.1, 0.7, 0.3, 0.9, 0.4, 0.8])
result = process_data(arr, threshold=0.5)
result_with_idx = process_data(arr, threshold=0.5, return_indices=True)
print(result)
print(result_with_idx)