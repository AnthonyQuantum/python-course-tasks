d = int(input())
dict = set()
for i in range(d):
    inp = input().lower()
    dict.add(inp)
mistakes = []
l = int(input())
for i in range(l):
    words = input().split()
    for word in words:
        lowercase = word.lower()
        if lowercase not in dict:
            mistakes.append(word)
for word in mistakes:
    print(word)