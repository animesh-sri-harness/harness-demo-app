import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "dev")


@app.route("/")
def index():
    return jsonify({"status": "ok", "version": VERSION})


@app.route("/health")
def health():
    return "healthy", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
