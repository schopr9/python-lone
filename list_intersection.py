"""
Intersection of two arrays
time complexity m + n
"""
def list_intersection(input_array_1=None, input_array_2=None):
    """
    :param input_array_1:
    :param input_array_2:
    :return:
    :rtype: array
    """
    input_array_1 = [1, 3, 5, 7, 2]
    input_array_2 = [2, 5, 10, 11, 4]
    # initialize the dict with first array
    output = {ele: 0 for ele in input_array_1}
    # find the element from second array in the hash
    intersection = [ele for ele in input_array_2 if ele in output]

    return intersection

print list_intersection()
