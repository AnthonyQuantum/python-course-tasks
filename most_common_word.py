dict = {}
words = ''

with open('input.txt', 'r') as input_file:
    for line in input_file:
        words += line.strip() + ' '
words_orig = words
words = words.split()

print('orig', words_orig)

for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

arr = []

max_count = max(dict.values())
for key in dict.keys():
    if dict[key] == max_count:
        arr.append(key)
arr.sort()

with open('output.txt', 'w') as output_file:
    for i in range(len(words)):
        if words[i] == arr[0]:
            output_file.write(words_orig.split()[i] + ' ' + str(max_count))
            break