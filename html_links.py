import requests

src_url = input()
dest_url = input()

src_html = requests.get(src_url).content
links = src_html.search(r"<a href=(.+)", src_html)
print(links)