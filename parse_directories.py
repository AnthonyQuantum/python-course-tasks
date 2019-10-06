import os

dir_list = []

for current_dir, dirs, files in os.walk("./main"):
    files = list(filter(lambda file: len(file) > 3 and file[-3:] == ".py", files))
    if len(files) > 0:
        dir_list.append(current_dir)

dir_list.sort()
with open("output.txt", "w") as output_file:
    for dir in dir_list:
        output_file.writelines(dir[2:] + "\n")