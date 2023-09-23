from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


received_data = []


@app.route("/receive_data", methods=["POST"])
def receive_data():
    data = request.json
    received_data.append(data)
    return jsonify({"success": True})


@app.route("/")
def index():
    return render_template("index.html", data=received_data)

if __name__ == "__main__":
    app.run(port=8002)  
