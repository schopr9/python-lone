def cmp(o1, o2):
    """
    return 1 if o1 comes before o2
    return -1 if o2 comes before o1
    return 0 if o1 equals o2 or order doesn't matter
    """
    o1 = str(o1)
    o2 = str(o2)
    a = o1 + o2
    b = o2 + o1
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1    

def main(input_list):
    output_list = sorted(input_list, cmp=cmp, reverse=True)
    return "".join(map(lambda x: str(x), output_list))

print main([9, 99, 94, 4, 23])    