print("first program")





# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
 
 
 
import numpy as np
 
# Create an array with even numbers between 0 and 20 (inclusive)
even_numbers = np.arange(10)
 
# Print the array
print(even_numbers)
print(even_numbers.shape)
 
import numpy as np
 
# Create an array of 5 zeros
zeros_array = np.zeros(5)
 
# Create an array of 5 ones
ones_array = np.ones(5)
 
print("Zeros Array:", zeros_array)
print("Ones Array:", ones_array)
 
import numpy as np
 
# Create a 2x5 array filled with the value 7
arr = np.full((2, 5), 7)
 
print("Array filled with 7s:")
print(arr)
 
 
import numpy as np
 
# Create a 3x3 array filled with the value 3.14 (float)
arr = np.full((3, 3), 3.14, dtype=float)
 
print("Array filled with 3.14 (dtype=float):")
print(arr)
 
 
 
import numpy as np
 
# Create a 2x3 array filled with the value 8, stored in column-major order
arr = np.full((2, 3), 8, order='F')
 
print("Array filled with 8s (column-major order):")
print(arr)
 
 
import numpy as np
 
# Create a 4x4 array for demonstration
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
 
print("Original Array:")
print(arr)
 
# Apply the slicing operation [1:3, :3]
result = arr[1:3, :4]
 
print("\nSliced Array [1:3, :3]:")
print(result)
 
 
 
import numpy as np
 
# Define two arrays
array1 = np.array([[4, 5, 7], [2, 9, 6], [7, 13, 19]])
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
 
 
 
print("print array1:")
print(array1)
 
# Add the two arrays
sum_array = array1 + array2
print("Sum of the two arrays:")
print(sum_array)
 
# Transpose the resulting matrix
transpose_matrix = np.transpose(sum_array)
print("\nTranspose of the resulting matrix:")
print(transpose_matrix)
 
 
 
 
 
import numpy as np
 
# Create an array
arr = np.array([1, 2, 3, 4, 5])
 
# Compute the cumulative sum
cumulative_sum = np.cumsum(arr)
 
print("Original Array:", arr)
print("Cumulative Sum:", cumulative_sum)
 
 
import numpy as np
 
# Correct array initialization
a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
 
# Assign a1 to a2
a2 = a1  # Use copy() to avoid modifying a1 when a2 is changed
 
# Modify the first element of a2
a2[0][0] = 12
 
# Print the modified array
print("Modified a2:")
print(a2)
 
# Reshape the array
a2.shape= 4, -1
 
# Print the reshaped array
print("shaped a2:")
print(a2)
 
 
 
 
# List of fruits
fruits = ["apple", "banana", "cherry", "date"]
 
# Loop through the list and print each fruit
for fruit in fruits:
    print(fruit)
