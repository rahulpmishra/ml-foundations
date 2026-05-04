import numpy as np
from typing import Optional

class DataValidationError(Exception):
    """Raised when input data fails validation checks."""
    pass

class ModelPredictionError(Exception):
    """Raised when model prediction fails."""
    pass

def validate_input_array(
    data: np.ndarray,
    expected_features: int,
    name: str = "input"
) -> None:
    """Validate that input array has correct shape and no NaN/inf values."""
    
    if not isinstance(data, np.ndarray):
        raise DataValidationError(
            f"{name} must be a numpy array, got {type(data).__name__}"
        )
    
    if data.ndim != 2:
        raise DataValidationError(
            f"{name} must be 2D array of shape (n_samples, {expected_features}), "
            f"got shape {data.shape}"
        )
    
    if data.shape[1] != expected_features:
        raise DataValidationError(
            f"{name} must have {expected_features} features, "
            f"got {data.shape[1]}"
        )
    
    if np.any(np.isnan(data)):
        nan_count = np.isnan(data).sum()
        raise DataValidationError(
            f"{name} contains {nan_count} NaN values. Clean data before prediction."
        )
    
    if np.any(np.isinf(data)):
        raise DataValidationError(
            f"{name} contains infinite values."
        )

# Test the validation
try:
    good_data = np.random.randn(10, 5)
    validate_input_array(good_data, expected_features=5)
    print("Good data passed validation")
    
    bad_data = np.array([[1, 2, np.nan], [4, 5, 6]])
    validate_input_array(bad_data, expected_features=3)
    
except DataValidationError as e:
    print(f"Validation failed: {e}")