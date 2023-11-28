import requests

# Rocket.Chat 的 URL 和用戶認證資訊
server_url = "http://server_url"
user_token = "user_token"
user_id = "user_id"

# 設定 headers
headers = {
    "X-Auth-Token": user_token,
    "X-User-Id": user_id,
    "Content-type": "application/json"
}

## Send command to channel
# 接收者的用戶名
roomid = "room_id"
# 要發送的訊息內容
context = """enable `[ This is a Auto Reply Message ]`
Hi, Today is good day."""
message = {
    "roomId": roomid,  # 訊息接收者的用戶名
    "command": "auto-reply",
    "params": context
}
# 發送請求
response = requests.post(f"{server_url}/api/v1/commands.run", json=message, headers=headers)

# 輸出結果
print(response.json())
