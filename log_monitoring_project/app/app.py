from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Log Monitoring Project"}

@app.route("/hello")
def hello():
    return {"message": "Hello DevOps"}

@app.route("/status")
def status():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
