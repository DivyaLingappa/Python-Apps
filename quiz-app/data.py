import requests

# url = "https://opentdb.com/api.php?amount=10&type=boolean"
#url = "https://opentdb.com/api.php?amount=10&category=15&type=boolean"
url = "https://opentdb.com/api.php?amount=10&category=32&type=boolean"
response = requests.get(url)
response.raise_for_status()
data = response.json()
question_data = data["results"]