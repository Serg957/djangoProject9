import requests

THE_URL = 'https://binaryjass.us/wp-json/genrenator/v1/genre/'
res =[]

for i in range(10):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)

print(res)