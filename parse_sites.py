import requests
import re

sites = set()

link = input().strip()
html = requests.get(link, stream=True).text
links = re.findall(r"<a.+href=[\"\'](.+?://)?([^./].+?)(:.+?)?/?[\"\'].*?", html)
for link in links:
    link = link[1]
    sites.add(link)

sites = list(sites)
sites.sort()
for site in sites:
    print(site)