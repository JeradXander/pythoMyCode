
import urllib.request
import json


URL = "https://api.thedogapi.com/v1/images/search"

webobj = urllib.request.urlopen(URL)

content = webobj.read()

content = content.decode("utf-8")


atlast = json.loads(content)
print(atlast)

print(atlast[0]["url"])
