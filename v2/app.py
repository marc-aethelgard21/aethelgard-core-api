from flask import Flask, jsonify, request

app = Flask(__name__)

SECRET_KEY = "@ncai2w5/&ltaI"

@app.route("/status")
def status():
    return jsonify({"status": "running v2"})

@app.route("/get_secret")
def get_secret():
    key = request.args.get("key")
    if key == "open_sesame_v2":
        return jsonify({"secret": SECRET_KEY})
    return jsonify({"error": "invalid key"}), 403

if __name__ == "__main__":
    app.run(debug=True)
