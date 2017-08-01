def my_function(arg):
    list_of_string = list(arg)
    print list_of_string
    list_of_string.reverse()
    print list_of_string
    arg = ''.join(list_of_string)
    # write the body of your function here
    return 'running with %s' % arg

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function('test input')



import re

text = 'fdwaw4helloworldvcdv1c3xcv3xcz1sda21f2sd1ahelloworldgafgfa4564534321fadghelloworld'
largest = ''
i = 1

while 1:
    m = re.search("(" + ("\w" * i) + ").*\\1.*\\1", text)
    if not m:
        break
    largest = m.group(1)
    i += 1

print largest    # helloworld    

def guess_seq_len(seq):
    s2 = (seq + seq)[1:-1]
    return s2.find(seq) != -1

def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) / 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            guess = x

    return guess

def longest_repeated_sequence(inp):
    list_of_char = [ord(c) for c in inp]
    guess_seq_len(list_of_char)
    


longest_repeated_sequence("helloworldciusdicujnshelloworld")

daily_balances = [107.92, 108.67, 109.86, 110.15]
daily_balances.reverse()
a = []
for i in xrange(len(daily_balances) - 1):
    a.append([daily_balances[i], daily_balances[i + 1]])

print a    