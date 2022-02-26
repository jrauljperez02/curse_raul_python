import requests
#https://www.latlong.net/Show-Latitude-Longitude.html

response = requests.get(url='http://api.open-notify.org/iss-now.json')
if response.status_code == 404:
    raise Exception('That resource does not exist')
elif response.status_code == 401:
    raise Exception('You are not authorised to access to data ')

#Other way to do the same is...
response.raise_for_status()
data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)

print(iss_position)