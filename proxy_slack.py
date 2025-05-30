import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
SLACK_WEBHOOK_URL = os.environ.get("https://hooks.slack.com/services/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")

@app.route("/", methods=["POST"])
def proxy_to_slack():
    data = request.get_json(force=True)
    headers = {"Content-Type": "application/json"}
    response = requests.post(SLACK_WEBHOOK_URL, json=data, headers=headers)
    return ("", response.status_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

