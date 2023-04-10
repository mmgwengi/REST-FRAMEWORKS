import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Engine Size(L)':4, 'Cylinders':5 ,'Fuel Consumption Comb (L/100 km)':10})

print(r.json())