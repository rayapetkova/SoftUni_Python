def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    if word[idx] != word[-idx - 1]:
        return f"{word} is not a palindrome"

    return palindrome(word, idx + 1)


# Test code:

# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))






#2 - solution without recursion

# def palindrome(word, idx=0):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#
#     return f"{word} is not a palindrome"
