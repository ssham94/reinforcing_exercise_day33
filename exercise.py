import requests
import json

res = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')
body = json.loads(res.content)

# Picking country
print(body[84])
print('')

# Getting URL for the politicians in legislature
legislation_url = body[84]['legislatures'][0]['popolo_url']
print(legislation_url)
print('')

hk_res = requests.get('https://cdn.rawgit.com/everypolitician/everypolitician-data/9875798809ee44d7f19344adf8b012d0c92289ca/data/Hong_Kong/Legislative_Council/ep-popolo-v1.0.json')
hk_body = json.loads(hk_res.content)
name = hk_body['persons'][32]['given_name']

# Checking to see if name has been assigned correctly
print(name)

