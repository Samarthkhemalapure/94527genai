import requests
import json
import time

api_key = "dummy-key"

url = "http://127.0.0.1:1234/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

while True:
    user_prompt = input("Ask Anything = ")

    if user_prompt.lower() == "exit":
        break

    req_data = {
        "model": "meta-llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    }

    start_time = time.perf_counter()

    response = requests.post(url, json=req_data, headers=headers)

    end_time = time.perf_counter()

    if response.status_code == 200:
        res = response.json()
        print(res["choices"][0]["message"]["content"])
        print("Time required =", end_time - start_time)
    else:
        print("Error:", response.status_code, response.text)
