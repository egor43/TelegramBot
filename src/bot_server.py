# Import Flask work modules
from flask import Flask, Response
from flask import request

# Import Telegram classes
from TelegramObjects import update

# Constants
TELEGRAM_API = "https://api.telegram.org/"
BOT_TOKEN = ""

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    input_update = update.Update(request.data)
    return "OK"

if __name__ == '__main__':
    app.run()