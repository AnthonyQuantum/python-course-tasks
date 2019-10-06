import requests
import json

CLIENT_ID = '7495109f7369d7095e41'
CLIENT_SECRET = '5acaf9b74385f18ac3da2095edeee7c1'

response = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": CLIENT_ID,
                      "client_secret": CLIENT_SECRET
                  })
res_json = json.loads(response.text)
token = res_json["token"]
headers = {"X-Xapp-Token" : token}

artists = []

with open("input.txt", "r") as input_file:
    for artist_id in input_file:
        response = requests.get("https://api.artsy.net/api/artists/" + artist_id.strip(), headers=headers)
        response.encoding = "utf-8"
        res_json = json.loads(response.text)
        artists.append({
            "name": res_json["sortable_name"],
            "birth_year": res_json["birthday"]
        })

for i in range(0, len(artists)):
    for j in range(i, len(artists)):
        if artists[i]["birth_year"] > artists[j]["birth_year"] or artists[i]["birth_year"] == artists[j]["birth_year"] and "".join(artists[i]["name"]) > "".join(artists[j]["name"].split()):
            artists[i], artists[j] = artists[j], artists[i]

with open("output.txt", "w") as output_file:
    for artist in artists:
        output_file.write(artist["name"])
        output_file.write("\n")