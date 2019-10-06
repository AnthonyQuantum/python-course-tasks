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
        pass
    else:
        parents[inp[0]] = inp[2:]

n = int(input())
catched = []
to_delete = []
for i in range(n):
    exc_name = input()
    is_connected = False
    if len(catched) > 0:
        for catched_exc in catched:
            DFS(catched_exc, exc_name)
        if is_connected:
            to_delete.append(exc_name)
    catched.append(exc_name)

for exc_name in to_delete:
    print(exc_name)