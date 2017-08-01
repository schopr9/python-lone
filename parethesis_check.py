iparens = iter('(){}[]<>')
parens = dict(zip(iparens, iparens))
closing = parens.values()


def parenthesis_checker(input):
    
    if len(input)%2 != 0:
        return False

    if parens[input[0]] != input[-1]:
        return False    
    
    for i in range(1,len(input)/2 ):
        if parens.get(input[i]) != input[-1 * i - 1]:
            return False
    return True            

print parenthesis_checker("(((<>)))")



def balanced(astr):
    stack = []
    for c in astr:
        d = parens.get(c, None)
        if d:
            stack.append(d)
        elif c in closing:
            if not stack or c != stack.pop():
                return False
    return not stack