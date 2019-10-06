import requests

with open('input.txt', 'r') as input_file:
    url = input_file.readline().strip()

url_prefix = 'https://stepic.org/media/attachments/course67/3.6.3/'
response = requests.get(url)
while True:
    print(response.text)
    if response.text[0:2] == 'We':
        with open('output.txt', 'w') as output_file:
            output_file.write(response.text)
        break
    response = requests.get(url_prefix + response.text)