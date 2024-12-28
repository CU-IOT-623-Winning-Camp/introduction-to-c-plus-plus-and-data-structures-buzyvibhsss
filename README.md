# LINE Bot Application

This application is a simple LINE bot built using Flask and the LINE Messaging API. It receives messages sent to the bot and echoes them back to the sender.

## Features
- Handles incoming messages from LINE users.
- Echoes back the received text messages.
- Implements webhook handling using Flask.

## Prerequisites
- Python 3.x installed.
- LINE Developers account.
- Create a LINE bot and obtain the following credentials:
  - **Channel Access Token**
  - **Channel Secret**

## Environment Variables
Set the following environment variables before running the application:
- `YourCannelAccessToken`: Your LINE Channel Access Token.
- `YourChannelSecret`: Your LINE Channel Secret.
- `PORT`: The port to run the application (default is 5000).

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables.

## Usage
1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Deploy the application to a server or use a tunneling service like `ngrok` to expose it to the internet.
3. Configure the webhook URL in the LINE Developers Console.

## Code Overview
### Main Components
- **Environment Variables**: Loads sensitive data like tokens and secrets.
- **Webhook Handling**: Processes incoming requests from LINE's webhook.
- **Message Handling**: Responds to text messages with the same text received.

### Key Functions
- `callback`: Processes incoming webhook requests and validates signatures.
- `handle_message`: Echoes back the received text messages.

## Deployment
- Deploy the application using services like Heroku, AWS, or any cloud provider.
- Make sure the webhook URL is accessible over HTTPS.

## Dependencies
- Flask
- line-bot-sdk

## License
This project is licensed under the MIT License.
