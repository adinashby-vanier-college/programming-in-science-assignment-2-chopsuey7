# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) == 0:
        return ()  # Return an empty tuple if the list is empty
    elif len(numbers) == 1:
        return numbers[0]  # Return the single number if the list has only one element
    else:
        largest = max(numbers[0], numbers[1])
        second_largest = min(numbers[0], numbers[1])

        for number in numbers[2:]:
            if number > largest:
                second_largest = largest
                largest = number
            elif number > second_largest:
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
    return []

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [[]]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return []

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    return 0

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    return [[0, 0], [0, 0]]