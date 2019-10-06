mat = [[0 for i in range(n)] for j in range(n)]
counter = 1
x = 0
y = 0

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dir_num = 0

def next_direction():
    global dir_num
    dir_num += 1
    if dir_num == 4:
        dir_num = 0

n = int(input())

for i in range(n):
    mat[x][y] = counter
    counter += 1
    y += 1
n -= 1
y -= 1

while n > 0:
    next_direction()
    for i in range(n):
        #print('in 1 for ', x, y)
        x += directions[dir_num][0]
        y += directions[dir_num][1]
        mat[x][y] = counter
        counter += 1
    next_direction()
    for i in range(n):
        #print('in 2 for ', x, y)
        x += directions[dir_num][0]
        y += directions[dir_num][1]
        mat[x][y] = counter
        counter += 1
    n -= 1

with open('output.txt', 'w') as output_file:
    for i in range(len(mat)):
        for j in range(len(mat)):
            output_file.write(mat[i][j], end=' ')
        output_file.write('\n', end='')