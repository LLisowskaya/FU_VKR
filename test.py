import requests, json
url = "https://api.serphouse.com/serp/live"
payload = json.dumps({
    "data": {
        "domain": "google.com",
        "lang": "en",
        "q": "Coffee",
        "loc": "Texas,United States",
        "device": "desktop",
        "serp_type": "web"
    }
})
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': "Bearer DI9KP8vzXklO0XhQutJ8B2FebVYgn9CcyO2oBXJBHohOe7ji59tjegwhzXUV"
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)

