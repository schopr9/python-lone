# arr1 = [1,4,2,6]

# def intersection(arr_1, arr_2):
#     hash_map = {}
#     count = 1
#     for ele in arr_1:        
#         if ele in hash_map:      
#             hash_map[ele] = hash_map[ele] + count
#         hash_map[ele] = count    
#     #hash_map = { ele: 0 for ele in arr_1}
    
#     intersec = []
    
#     for ele in arr_2:
#         if ele in hash_map and hash_map[ele] > 0:
#             intersec.append(ele)
#             hash_map[ele] = hash_map[ele] - 1
#     return intersec        

# arr1 = [4,2,6]
# arr2 = [4,4,2,7]

# print intersection(arr1, arr2)


# def fibbonacci(n):

#     if n < 0:
#         return None

#     if n == 0:
#         return 0

#     if n == 1:
#         return 1

#     first = 0
#     second = 1

#     for i in range(n - 2):
#         sum = first + second
#         first = second
#         second = sum 
    
#     return sum            


# def palindrome(input):
#     char  = list(input)
#     reverse_char = char[::-1]
#     if input == reverse_char.join(''):
#         return True
#     return False    

# import numpy as np
# def two_dimensional_array(list_of_list):
#     count = 0
#     hash_map = {}
#     found_field = True
#     for row, idx in enumerate(list_of_list):
#         for ele, myidx in enumerate(row):
#             if ele == 'T':
#                 found_field = True
#                 hash_map[(idx,myidx)] = count
#                 if row[myidx - 1] == 'T':
                    
#             found_field = False

#    transpose_list = Transpose(list_of_list)

#     for row, idx in enumerate(transpose_list):
#         for ele, myidx in enumerate(row):
#             if ele == 'T':
#                 hash_map[(idx,myidx)] += count


def anagram(s1, s2):
    list_of_char = list(s1)
    hash_map = {}
    count = 1
    
    for char in list_of_char:
        if char in hash_map:
            hash_map[char] += 1 
            continue
        hash_map[char] = 1    

    for char in list(s2):
        if char in hash_map and hash_map[char] > 0:
            hash_map[char] -= 1
            continue
        else:    
            return False
    return True

print anagram('earth', 'heart9')            