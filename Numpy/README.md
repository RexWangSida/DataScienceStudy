# Numpy
- PyData Ecosystem rely on Numpy as one of their main building blocks.
- Numpy is **fast** since is has bindings to C libraries.
## Numpy Arrays
```python
import numpy as np
```
```python
my_list = [1, 2, 3]
my_arr = np.array(my_list)
```
The output is `array([1, 2, 3])`
```python
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_arr = np.array(my_mat)
```
The output is `array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])`
