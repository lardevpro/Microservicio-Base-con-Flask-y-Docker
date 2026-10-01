0from flask import Flask, jsonify

app = Flask(__name__)
@app.get("/health")
def health():
 return jsonify(status="ok")
@app.get("/")
def home():
 return jsonify(message="Microservicio Docker funcionando correctamente")
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)