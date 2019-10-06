import requests

API_URL = "http://numbersapi.com/"
API_ENDPOINT = "/math?json=true"

numbers = []

with open("input.txt", "r") as input_file:
    for line in input_file:
        numbers.append(line.strip())

res_json = requests.get(API_URL + ",".join(numbers) + API_ENDPOINT, stream=True).json()

with open("output.txt", "w") as output_file:
    for number in numbers:
        fact = res_json[number]["text"]
        if res_json[number]["found"]:
            output_file.write("Interesting\n")
        else:
            output_file.write("Boring\n")
