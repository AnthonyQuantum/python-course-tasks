def modify_list(l):
    for i in l[::-1]:
        if i % 2 != 0:
            l.remove(i)
        else:
            l[l.index(i)] = int(l[l.index(i)] / 2)

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]