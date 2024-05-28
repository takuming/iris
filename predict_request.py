import requests

# APIエンドポイントのURL
url = "http://localhost:8000/predict"

# 送信するデータ
data = {
    "sepal_length": 6.1,
    "sepal_width": 2.5,
    "petal_length": 3.4,
    "petal_width": 1.2
}

# POSTリクエストの送信
response = requests.post(url, json=data)

# レスポンスの表示
print("Response Status Code:", response.status_code)
print("Response Data:", response.json())