with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    output_file.write("\n".join(map(lambda line: line.strip(), list(input_file)[::-1])))