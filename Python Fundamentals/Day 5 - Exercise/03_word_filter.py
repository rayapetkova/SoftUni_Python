def word_filter(words):
    for i in words:
        if len(i) % 2 == 0:
            return i


current_words = input().split()
print(word_filter(current_words))





#2
#
# [print(word) for word in input().split() if len(word) % 2 == 0]