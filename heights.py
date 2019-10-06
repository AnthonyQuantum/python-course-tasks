heights = [0 for i in range(11)]
counts = [0 for i in range(11)]

with open('input.txt', 'r') as input_file:
    for line in input_file:
        entry = line.split()
        heights[int(entry[0])-1] += int(entry[2])
        counts[int(entry[0])-1] += 1

with open('output.txt', 'w') as output_file:
    for i in range(11):
        output_file.write(str(i+1) + ' ')
        if (counts[i]):
            output_file.write(str(heights[i]/counts[i]))
        else:
            output_file.write('-')
        output_file.write('\n')