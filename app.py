from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def send_db():
    database_url = os.environ['DATABASE_URL']
    return jsonify(database_url)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access
    # support
    app.run(threaded=True, port=5000)
    