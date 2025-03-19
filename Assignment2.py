# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) == 0:
        return ()  # Return an empty tuple if the list is empty
    elif len(numbers) == 1:
        return (numbers[0], None)  # Return a tuple with the element and None
    else:
        # Handle duplicate largest numbers by setting second_largest to -float('inf') initially
        largest = max(numbers[0], numbers[1])
        second_largest = -float('inf') if numbers[0] == numbers[1] else min(numbers[0], numbers[1])

        for number in numbers[2:]:
            if number > largest:
                second_largest = largest
                largest = number
            elif number > second_largest and number != largest:  # Ensure number is not a duplicate of largest
                second_largest = number

        return (largest, second_largest)  
# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique_numbers = list(set(numbers))  # Convert to set to remove duplicates, then back to list
    unique_numbers.sort()  # Sort the list in ascending order

    return unique_numbers

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    cumulative_list = []
    current_sum = 0

    for num in arr:
        current_sum += num
        cumulative_list.append(current_sum)

    return cumulative_list

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = matrix[i][j]

    return transposed
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length for dot product.")

    dot_prod = 0
    for i in range(len(list1)):
        dot_prod += list1[i] * list2[i]

    return dot_prod

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Number of columns in matrix1 must be equal to number of rows in matrix2.")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
