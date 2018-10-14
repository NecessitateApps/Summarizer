import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=4447d852b5264e1dab136e3f15d4089c')
response = requests.get(url)
print(response.json())