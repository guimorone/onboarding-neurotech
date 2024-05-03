from flask import Flask, Response, jsonify
from src.collector import Collector

app = Flask(__name__)


@app.route('/<code>', methods=['GET'])
def home(code: str) -> Response:
    collector = Collector(code)
    response = collector.collect()
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000)
