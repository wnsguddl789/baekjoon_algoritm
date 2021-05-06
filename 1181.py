import sys

N = int(sys.stdin.readline())
words_list = []

for _ in range(N):
    word = str(sys.stdin.readline().rstrip())
    word_count = len(word)
    words_list.append((word,word_count))
words_list = list(set(words_list))

words_list.sort(key= lambda word:(word[1],word[0]))

for word in words_list:
    print(word[0])