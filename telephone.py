def solution(A):
    # write your code in Python 2.7
    sort_array = sorted(A)
    first_filter =  [str(d) for d in sort_array if len(str(d)) == len(str(sort_array[0]))]
    min_length = min([len(set(ele)) for ele in first_filter])
    second_filter = [ele for ele in first_filter if len(set(ele)) == min_length]
    return sorted(second_filter)[0] 

print solution([1233, 1333, 3131, 34126, 11111111])        

