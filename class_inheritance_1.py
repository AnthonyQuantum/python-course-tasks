parents = {}
is_connected = False

def DFS(parent, child):
    global is_connected, parents
    if is_connected:
        return
    if parent == child:
        is_connected = True
        return
    if child in parents and parent in parents[child]:
        is_connected = True
        return
    if child in parents:
        for new_child in parents[child]:
            DFS(parent, new_child)

n = int(input())
for i in range(n):
    inp = input().split()
    if len(inp) == 1:
        parents[inp[0]] = []
    else:
        parents[inp[0]] = inp[2:]
q = int(input())
for i in range(q):
    parent, child = input().split()
    is_connected = False
    DFS(parent, child)
    print((is_connected if 'Yes' else 'No'))