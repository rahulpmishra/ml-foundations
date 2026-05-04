import numpy as np
from typing import Optional, Tuple
import time

class DataProcessor:
    """
    A simple data processor for numerical arrays.
    Demonstrates: class design, type hints, error handling, docstrings.
    
    This is the pattern you will use in every ML project.
    """
    
    def __init__(self, n_features: int, normalize: bool = True):
        self.n_features = n_features
        self.normalize = normalize
        self._mean: Optional[np.ndarray] = None  # underscore = internal attribute
        self._std: Optional[np.ndarray] = None
        self._is_fitted = False
    
    def fit(self, data: np.ndarray) -> 'DataProcessor':
        """
        Learn normalization parameters from training data.
        Returns self to allow method chaining: processor.fit(X).transform(X)
        """
        if data.shape[1] != self.n_features:
            raise ValueError(
                f"Expected {self.n_features} features, got {data.shape[1]}"
            )
        
        if self.normalize:
            self._mean = data.mean(axis=0)    # shape (n_features,)
            self._std = data.std(axis=0)
            # Handle zero std (constant features)
            self._std[self._std == 0] = 1.0
        
        self._is_fitted = True
        return self  # enables method chaining
    
    def transform(self, data: np.ndarray) -> np.ndarray:
        """Apply learned normalization to new data."""
        if not self._is_fitted:
            raise RuntimeError("Call fit() before transform()")
        
        if self.normalize:
            return (data - self._mean) / self._std
        return data.copy()
    
    def fit_transform(self, data: np.ndarray) -> np.ndarray:
        """Fit and transform in one step."""
        return self.fit(data).transform(data)
    
    @property
    def is_fitted(self) -> bool:
        """Read-only property — cannot be set externally."""
        return self._is_fitted
    
    def __repr__(self) -> str:
        return (f"DataProcessor(n_features={self.n_features}, "
                f"normalize={self.normalize}, "
                f"fitted={self._is_fitted})")


# Test it
if __name__ == "__main__":
    # Create sample data
    train_data = np.random.randn(100, 5) * 10 + 50  # not normalized
    test_data = np.random.randn(20, 5) * 10 + 50
    
    processor = DataProcessor(n_features=5, normalize=True)
    print(processor)  # __repr__ in action
    
    # Fit on training data only
    train_normalized = processor.fit_transform(train_data)
    print(f"\nTrain - Mean: {train_normalized.mean(axis=0).round(3)}")
    print(f"Train - Std:  {train_normalized.std(axis=0).round(3)}")
    
    # Transform test data using training parameters
    test_normalized = processor.transform(test_data)
    print(f"\nTest - Mean: {test_normalized.mean(axis=0).round(3)}")
    print(f"Processor: {processor}")
    
    # Test error handling
    try:
        processor.transform(np.random.randn(5, 10))  # wrong number of features
    except ValueError as e:
        print(f"\nCorrect error caught: {e}")