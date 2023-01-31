import json
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# datetime object containing current date and time
now = str(datetime.now())

print("now =", now)


# Parsing data from api
def getjson(url):
    response = requests.get(url)
    return json.loads(response.text)


# Parsing metadata from url
def getBanner(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    metas = soup.find_all('meta')  #Get Meta og:image
    for m in metas:
        if m.get('property') == 'og:image':
            banner = m.get('content')
            return banner


# color name to css color code list
colors = getjson(
    'https://raw.githubusercontent.com/ozh/github-colors/master/colors.json')

# all the repos list which i want to show on website
repos_list = [
    "18GRUOHiMhq51oRx4XUVe8fgcn1brYX6Y/edit?usp=share_link&ouid=102269643375653787985&rtpof=true&sd=true"
]

# execuation timer
start_time = time.time()

# empty list variable for repo variable
repos_data = []

# main fuction
for repo in repos_list:
    rdata = getjson(f'https://docs.google.com/document/d/{repo}')
    data = {
        "name": "google",
    }
    repos_data.append(data)
    print(f"{repo} done\t--- {time.time() - start_time} seconds ---")

# Serializing json
json_data = json.dumps(repos_data, indent=4)

# Writing to repos.json
with open("json/repos.json", "w") as outfile:
    outfile.write(json_data)

# Total execuation time
print(f"all done\t--- {time.time() - start_time} seconds ---")