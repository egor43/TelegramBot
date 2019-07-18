# Import Flask work modules
from flask import Flask, Response
from flask import request

# Import additional modules
import json

# Import Telegram classes
from TelegramObjects import update

# Constants
TELEGRAM_API = "https://api.telegram.org/"
BOT_TOKEN = ""

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    update_data = json.loads(request.data.decode())
    input_update = update.Update(update_data)
    return "OK"

if __name__ == '__main__':
    app.run()