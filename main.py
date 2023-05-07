from password import API_KEY
import requests
import json

link = "https://api.openai.com/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
id_model = "gpt-3.5-turbo"

body_message = {
    "model": id_model,
    "messages": [{"role": "user", "content": "Faça um tcc de odontologia cirúrgica"}]
}
body_message = json.dumps(body_message)

request = requests.post(link, headers=headers, data=body_message)
print(request)
response = request.json()
message = response["choices"][0]["message"]["content"]
print(message)