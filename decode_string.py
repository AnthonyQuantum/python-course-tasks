import re

input_file = open('input.txt', 'r')
line = input_file.readline()
input_file.close()

output_file = open('output.txt', 'w')
regex = re.compile(r'([a-zA-Z])([0-9]+)')
pairs = regex.findall(line)
res_string = ''
for pair in pairs:
    res_string += pair[0] * int(pair[1])
output_file.write(res_string)
output_file.close()