from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def home():
    count = redis_client.incr("visits")
    return f"""
    <h1>Docker Compose Demo</h1>
    <p>Hello from the Flask container! Updated via CI/CD.</p>
    <p>This page has been visited <strong>{count}</strong> times.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)