num_of_students = 0
medians = []
medians_all = [0, 0, 0]

with open('input.txt', 'r') as input_file:
    for line in input_file:
        num_of_students += 1
        grades = [int(i) for i in line.split(';')[1:]]
        for i in range(3):
            medians_all[i] += grades[i]
        medians.append(sum(grades)/3)
medians_all = [i/num_of_students for i in medians_all]

with open('output.txt', 'w+') as output_file:
    print(medians)
    for i in medians:
        output_file.write(str('%.9f' % i) + '\n')
    for i in medians_all:
        output_file.write(str('%.9f' % i) + ' ')