
def second_largest(input_array):
    """
    To find the largest second number in the array
    """

    max_1 = input_array[0]
    max_2 = input_array[1]

    for i in range(1, len(input_array)):
        if input_array[i] > max_1:
            max_2 = max_1
            max_1 = input_array[i]
        elif input_array[i] > max_2 and input_array[i] != max_1:
            max_2 = input_array[i]
        elif max_1 == max_2:
            max_2 = input_array[i]

    return max_2


print second_largest([1, 3, 2, 5, 3, 3])
