import requests
import json

# Rocket.Chat 伺服器的 URL 和用戶認證資訊
server_url = "http://server_url"
user_token = "user_token"
user_id = "user_id"

# 設定 headers
headers = {
    "X-Auth-Token": user_token,
    "X-User-Id": user_id,
}

# 發送請求以獲取頻道列表
response = requests.get(f"{server_url}/api/v1/rooms.get", headers=headers)

# 將響應的 JSON 內容保存為文件
if response.status_code == 200:
    with open('rooms.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file)
    print("File saved successfully.")
else:
    print("Failed to retrieve data.")