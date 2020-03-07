# Find the longest palindromic contiguous substring in a word.

test1 = "bananas"
test2 = "aabcdcb"

"""
def check_palindrome(s):
    return s == s[::-1]

def longest_palindrome(s): # O(n³) time
    max_word = ""
    n = len(s)
    for i in range(n):
        for j in range(i, n+1):
            if check_palindrome(s[i:j]) and len(max_word) < len(s[i:j]):
                max_word = s[i:j]
    return max_word

"""
def longest_palindrome(s): # Dynamic Programming bottom-up approach O(n²) time and space 
    n = len(s)
    max_word = s[0]
    # A[i][j] is True if s[i:j] is a palindrome
    A = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        A[i][i] = True
        A[i][i+1] = True 
    A[-1][-1] = True

    for j in range(2, n):
        for i in range(j-1):
            A[i][j] = A[i+1][j-1] and s[i] == s[j] 
            if A[i][j] and j-i > len(max_word):
                max_word = s[i:j+1]

    return max_word

    
print(longest_palindrome(test1))
print(longest_palindrome(test2))


