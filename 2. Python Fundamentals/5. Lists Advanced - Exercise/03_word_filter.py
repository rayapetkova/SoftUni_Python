def word_filter(words):
    [print(word) for word in words if len(word) % 2 == 0]


current_words = input().split()
word_filter(current_words)




#2
#
# [print(word) for word in input().split() if len(word) % 2 == 0]
