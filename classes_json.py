import json

class_children = {}

classes = json.loads(input())
for class_obj in classes:
    if class_obj["name"] not in class_children:
        class_children[class_obj["name"]] = []
    for parent in class_obj["parents"]:
        if parent not in class_children:
            class_children[parent] = []
        class_children[parent].append(class_obj["name"])

print(class_children)


[{"name": "G", "parents": ["F"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "E", "parents": ["D"]}, {"name": "F", "parents": ["D"]}, {"name": "X", "parents": []}, {"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]}, {"name": "V", "parents": ["Z", "Y"]}, {"name": "W", "parents": ["V"]}]

A : 10
B : 5
C : 5
D : 4
E : 1
F : 2
G : 1
V : 2
W : 1
X : 5
Y : 3
Z : 3