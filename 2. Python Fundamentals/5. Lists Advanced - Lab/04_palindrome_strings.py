words = input().split()
palindrome = input()

lst = [i for i in words if i == i[::-1]]
number = lst.count(palindrome)
print(lst)
print(f"Found palindrome {number} times")