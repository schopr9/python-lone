def check_palin(word):
    for i in xrange(len(word)/2):
        if word[i] != word[-1*(i+1)]:
            return False
    return True

def all_palindromes_first(string):

    first = 0
    last = len(string)
    counter = last
    results = []

    while first < last - 1:
        temp = string[first:counter]
        counter -= 1

        #print temp
        if temp[0] == temp[-1]:
            if check_palin(temp):
                results.append(temp)

        if counter < first + 1:
            first += 1
            counter = last

    return len(set(results))

print all_palindromes_first("aabaa")

DEFAULT_TEXT = "aabaa"

def all_palindromes(text=DEFAULT_TEXT):
    """Return list with all palindrome strings within text.

    The base of this algorithm is to start with a given character,
    and then see if the surrounding characters are equal. If they
    are equal then it's a palindrome and is added to results set,
    extend to check if the next character on either side is equal, 
    adding to set if equal, and breaking out of loop if not.

    This needs to be repeated twice, once for palindromes of 
    odd lengths, and once for palindromes of an even length."""

    results = set()
    text_length = len(text)
    for idx, char in enumerate(text):

        # Check for longest odd palindrome(s)
        start, end = idx - 1, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.add(text[start:end+1])
            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = idx, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.add(text[start:end+1])
            start -= 1
            end += 1

    return list(results)

print all_palindromes(text=DEFAULT_TEXT)


def  firstRepeatedWord( s):
    list_of_words = s.split(' ')
    repeat = {}
    for word in list_of_words:
        if word not in repeat:
            repeat[word] = 0
        repeat[word] += 1
        if repeat[word] == 2:
            return word
        

def palindrome(s):

    output = []
    if not s:
        yield []
        return
    for i in range(len(s), 0, -1):
        sub = s[:i]
        if sub == sub[::-1]:
            for rest in palindrome(s[i:]):
                yield [sub] + rest  

print set(sum(list(palindrome('aabaa')), []))


# def palindromeSubStrs(s):
#     m = dict()
#     n = len(s)
 
#     R = [[0 for x in xrange(n+1)] for x in xrange(2)]
 
#     s = "@" + s + "#"
 
#     for j in xrange(2):
#         rp = 0    
#         R[j][0] = 0
 
#         i = 1
#         while i <= n:
 
#             # Attempt to expand palindrome centered at i
#             while s[i - rp - 1] == s[i + j + rp]:
#                 rp += 1 # Incrementing the length of palindromic
#                         # radius as and when we find valid palindrome
 
#             # Assigning the found palindromic length to odd/even
#             # length array
#             R[j][i] = rp
#             k = 1
#             while (R[j][i - k] != rp - k) and (k < rp):
#                 R[j][i+k] = min(R[j][i-k], rp - k)
#                 k += 1
#             rp = max(rp - k, 0)
#             i += k
 
#     # remove guards
#     s = s[1:len(s)-1]
 
#     # Put all obtained palindromes in a hash map to
#     # find only distinct palindrome
#     m[s[0]] = 1
#     for i in xrange(1,n):
#         for j in xrange(2):
#             for rp in xrange(R[j][i],0,-1):
#                 m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
#         m[s[i]] = 1
 
#     return len(m)

# print palindromeSubStrs("aabaa")        