import json

data = None
with open('data/props_1.json',encoding='utf-8') as file:
    # data = file.read()
    data = json.load(file)
restaurant_data = data['props']['initialReduxState']['pageRestaurantsV2']['entities']['restaurantList']

with open('cleaned.json','w',encoding='utf-8') as file:
    data = json.dump(restaurant_data,file,indent=2)
