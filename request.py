import requests

url = 'http://localhost:5000/predict_api' 
r = requests.post(url,json={'profile pic
':0, 'nums/length username
':10 , 'fullname words
':2, 'nums/length fullname
':0, 'name==username
':0, 'description length
':44, 'external URL
':0, 'private':0, '#posts
':13, '#followers
':30,'#follows
':955
 })

print(r.json())


