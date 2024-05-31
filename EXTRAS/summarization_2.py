import requests

url = "https://chatgpt-42.p.rapidapi.com/chatgpt"

payload = {
	"messages": [
		{
			"role": "user",
			"content": "hello"
		}
	],
	"web_access": False
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "6acc5d7cdamshf1edd0e67e96471p1b0458jsn2da602e20937",
	"X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())