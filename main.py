from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

# Retrieve environment variables
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YourCannelAccessToken"]
YOUR_CHANNEL_SECRET = os.environ["YourChannelSecret"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # Extract X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Extract request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Process webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Reply with the same text received
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    # Start the Flask application
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
