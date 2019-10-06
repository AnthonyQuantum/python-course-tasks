import csv

primary_types = {}

with open("Crimes.csv") as inp_file:
    reader = csv.reader(inp_file)
    for crime_data in reader:
        primary_type = crime_data[5]
        if primary_type not in primary_types:
            primary_types[primary_type] = 1
        else:
            primary_types[primary_type] += 1

max_count = -10000
max_type = ""
for crime_type in primary_types.keys():
    if primary_types[crime_type] > max_count:
        max_count = primary_types[crime_type]
        max_type = crime_type

print(max_type)
