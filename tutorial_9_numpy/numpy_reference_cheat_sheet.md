# Quick cheat sheet  
```python  
# Creation  
np.array([1, 2, 3])              # From list  
np.zeros(5)                       # Array of zeros  
np.ones(5)                        # Array of ones  
np.arange(1, 10)                  # Range  
np.linspace(0, 10, 5)            # Evenly spaced  
  
# Operations  
array + 10                        # Add to all  
array * 2                         # Multiply all  
np.mean(array)                    # Average  
np.sum(array)                     # Sum  
np.max(array)                     # Maximum  
np.min(array)                     # Minimum  
np.std(array)                     # Standard deviation  
  
# Indexing  
array[0]                          # First element  
array[-1]                         # Last element  
array[2:5]                        # Slice  
array[array > 10]                 # Conditional  
  
# 2D Arrays  
array[0, 1]                       # Row 0, Column 1  
array[:, 0]                       # All rows, Column 0  
array[0, :]                       # Row 0, all columns  
np.mean(array, axis=0)           # Column averages  
np.mean(array, axis=1)           # Row averages  
```  
