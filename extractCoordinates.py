import json

data = None
with open('data/props_1.json',encoding='utf-8') as file:
    # data = file.read()
    data = json.load(file)
restaurant_data = data['props']['initialReduxState']['pageRestaurantsV2']['entities']['restaurantList']
# # print(type`(restaurant_data))
# restaurants = []
# for key,restaurant in restaurant_data.keys():
#     print(restaurant)
#     details = {
#         'name': restaurant['name'],
#         'latitude': restaurant['latitude'],
#         'longitude': restaurant['longitude']
#     }
#     restaurants.append(details)

with open('cleaned.json','w',encoding='utf-8') as file:
    data = json.dump(restaurant_data,file,indent=2)
