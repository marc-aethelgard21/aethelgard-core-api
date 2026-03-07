from flask import Flask, jsonify, request

app = Flask(__name__)

SECRET_KEY = "QmEwYmFiMTIzIw=="

@app.route("/status")
def status():
    return jsonify({"status": "running"})

@app.route("/get_secret")
def get_secret():
    key = request.args.get("key")
    if key == "open_sesame":
        return jsonify({"secret": SECRET_KEY})
    return jsonify({"error": "invalid key"}), 403

if __name__ == "__main__":
    app.run(debug=True)
