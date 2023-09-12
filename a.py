import json

f = open('config.txt', 'r').readlines()

x = []
for i in f:
    url = i.strip()
    data = {
        "id": url.replace('https://raw.githubusercontent.com/', ''),
        "url": url,
        "method": "GET",
        "parser": {
            "txt": {},
        }
    }
    x.append(data)


print(json.dumps(x, indent=4))