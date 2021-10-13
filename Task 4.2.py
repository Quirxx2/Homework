def palindrome(s):
#    b = s[::-1]
#    if b != s: return False
#    return True
    for i in range(len(s)):
         if s[i] != s[len(s) - i - 1]:
            return False
    return True

a = input()

print(palindrome(a))

