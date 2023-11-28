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
message = {
    "roomId": roomid,  # 訊息接收者的用戶名
    "command": "auto-reply",
    "params": "disable"
}
# 發送請求
response = requests.post(f"{server_url}/api/v1/commands.run", json=message, headers=headers)


# ## Send message to user
# # 接收者的用戶名
# recipient_username = "@user_name"
# # 要發送的訊息內容
# message = {
#     "channel": recipient_username,  # 訊息接收者的用戶名
#     "text": "/hide"
# }
# # 發送請求
# response = requests.post(f"{server_url}/api/v1/chat.postMessage", json=message, headers=headers)

# ## Send message to Channel
# # 要發送的訊息內容
# message = {
#     "channel": "#your-channel",
#     "text": "/hide"
# }
# # 發送請求
# response = requests.post(f"{server_url}/api/v1/chat.postMessage", json=message, headers=headers)


# 輸出結果
print(response.json())
