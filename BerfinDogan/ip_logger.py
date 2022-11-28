import sys
import requests
import json

response = requests.get("http://ip-api.com/json/" +sys.argv[1])
data = response.text
values = json.loads(data)

data = {'IP': values.get('query','Not Available'),
"STATUS":values.get('status','Not Available'),
"COUNTRY":values.get('country','Not Available'),
"COUNTRY CODE":values.get('countryCode','Not Available'),
"REGION":values.get('region','Not Available'),
"CITY":values.get('city','Not Available'),
"ZIP":values.get('zip','Not Available'),
"LAT":str(values.get('lat','Not Available')),
"LON":str(values.get('lon','Not Available')),
"TIMEZONE":values.get('timezone','Not Available'),
"ISP NAME":values.get('isp','Not Available')
}

with open("nosql_data.json","w") as f:
    f.write(json.dumps(data,ensure_ascii=False)+"\n")


