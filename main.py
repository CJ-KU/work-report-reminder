from flask import Flask, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

LINE_TOKEN = os.getenv("LINE_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

def send_message(text):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Authorization': f'Bearer ' + LINE_TOKEN,
        'Content-Type': 'application/json'
    }
    payload = {
        'to': GROUP_ID,
        'messages': [{'type': 'text', 'text': text}]
    }
    res = requests.post(url, headers=headers, json=payload)
    print("發送結果：", res.status_code, res.text)

@app.route("/")
def index():
    return "Bot is running."

@app.route("/work-reminder", methods=["GET"])
def work_reminder():
    send_message("🕔【下班提醒】記得回報今天的工作進度！📋")
    return "Work reminder sent."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
