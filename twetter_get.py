import json
import config 
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/trends/place.json"

params ={'id' : 23424856} 
res = twitter.get(url, params=params)

if res.status_code == 200:
  world_trends = json.loads(res.text)
else:
  print("Failed: %d" % res.status_code)

world_trends_list = world_trends[0]["trends"]
for s in world_trends_list:
  if s["tweet_volume"] == None:
    s["tweet_volume"] = 0

descending_list = sorted(world_trends_list, key=lambda x: x["tweet_volume"], reverse=True)
for s in descending_list:
  print(s["name"] + " " + str(s["tweet_volume"]))
    