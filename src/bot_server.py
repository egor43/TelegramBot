# Import Flask work modules
from flask import Flask, Response
from flask import request

# Import auxiliary modules
import json

# Constants
TELEGRAM_API = "ttps://api.telegram.org/"
BOT_TOKEN = ""

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    data = json.loads(request.data.decode())
    print(data)
    return "OK"

if __name__ == '__main__':
    app.run()