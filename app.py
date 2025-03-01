from flask import Flask  # ✅ Add this line

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! Running on K3s 🎉", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)