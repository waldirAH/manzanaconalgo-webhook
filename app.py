from flask import Flask, request

app = Flask(__name__)
VERIFY_TOKEN = "manzana_verify_123"

@app.get("/")
def home():
    return "OK", 200

@app.get("/webhook/meta")
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Forbidden", 403

@app.post("/webhook/meta")
def receive():
    data = request.get_json(silent=True) or {}
    print("MESSENGER IN:", data)
    return "OK", 200
