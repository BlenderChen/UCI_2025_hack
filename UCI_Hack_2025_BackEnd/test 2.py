from flask import Flask, Response
from flask_cors import CORS
import datetime
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Real-Time Clock Running with SSE"

@app.route('/time')
def stream_time():
    def generate_time():
        while True:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield f"data: {now}\n\n"  # SSE format
            time.sleep(1)  # Send updates every second
    return Response(generate_time(), content_type="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True)
