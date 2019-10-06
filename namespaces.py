vars_by_namespace = {}
parent_by_namespace = {}

vars_by_namespace['global'] = []
parent_by_namespace['global'] = None
n = int(input())
for i in range(n):
    command, namespace, arg = input().split()
    if command == 'create':
        # arg = parent
        parent_by_namespace[namespace] = arg
        if namespace not in vars_by_namespace:
            vars_by_namespace[namespace] = []
        if arg not in vars_by_namespace:
            vars_by_namespace[arg] = []
    elif command == 'add':
        # arg = var
        vars_by_namespace[namespace].append(arg)
    elif command == 'get':
        # arg = var
        if namespace not in vars_by_namespace:
            print('None')
        else:
            while namespace != None and arg not in vars_by_namespace[namespace]:
                namespace = parent_by_namespace[namespace]
            print(namespace)