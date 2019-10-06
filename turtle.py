n = int(input())
x = 0
y = 0

for i in range(n):
    inp = input().split()
    dir = inp[0]
    val = int(inp[1])
    if dir == 'север':
        y += val
    elif dir == 'юг':
        y -= val
    elif dir == 'запад':
        x -= val
    elif dir == 'восток':
        x += val

print(x, y)