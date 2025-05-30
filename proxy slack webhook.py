import requests
from flask import Flask, request

app = Flask(__name__)

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

@app.route("/", methods=["POST"])
def proxy():
    data = request.get_json()
    resp = requests.post(SLACK_WEBHOOK_URL, json=data)
    return ("", resp.status_code)
