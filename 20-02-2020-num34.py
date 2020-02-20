# Given a word, return the smallest palindrome possible
# by adding letters to this word. If there are multiple options to choose from,
# return the first in lexicographic order.

test1 = "race"
test2 = "google"
# Scalability:
test3 = "marro"

"""
def is_palindrome(s):
    reverse = [s[i] for i in range(len(s)-1, -1, -1)]
    return s == ''.join(reverse)
"""
def is_palindrome(s):
    return s == s[::-1]

def get_different_letters(s):
    letters = []
    for c in s:
        if c not in letters: letters.append(c)
    return letters

def get_right_palindrome(l):
    index = 0
    for k in range(1, len(l)):
        if len(l[k]) == len(l[index]):
            if l[k] < l[index]: # Check for lexicographic order
                index = k
        elif len(l[k]) < len(l[index]):
            index = k
            min_length = len(l[k])
    return l[index]

cache = {}
# Recursive, naive approach. DOES NOT SCALE UP
def find_palindrome(s, letters, found):

    if is_palindrome(s):
         found.append(s)
         return
    if len(letters) == 0: return # There will always be a palindrome shorter or
    for c in letters:            # of length 2*len(words) - 1
        for k in range(len(s)): 
            if s[k] != c: # Prevent double
                new_s = s[:k] + c + s[k:]
                new_letters = letters.copy()
                new_letters.remove(c)
                find_palindrome(new_s, new_letters, found)

list = []
find_palindrome_it(test3, get_different_letters(test3), list)
print(get_right_palindrome(list))
