def binary_search(arr, item):
    """
    Binary searh
    """
    if len(arr) == 0:
        return False

    if arr[-1] < item and arr[0] > item:
        return False    

    midpoint = len(arr)//2
    if arr[midpoint] == item:
        return True
    else:
        if item < arr[midpoint]:
            return binary_search(arr[:midpoint], item)
        else:
            return binary_search(arr[midpoint:], item)

    return False
        
print binary_search([1, 3, 5, 6, 7, 7, 8], 8)
