import json

with open('blog.json', 'r', encoding = 'utf-8') as file:
	data = json.load(file)

	for index in data:
		title = index.get('title')

		print(title)
	    
	