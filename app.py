import os
from flask import Flask, request, abort
import requests

app = Flask(__name__)

API_KEY = os.environ.get('API_KEY')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Check if the API key is valid
    api_key = request.headers.get('Authorization')
    if api_key != API_KEY:
        abort(401)
    
    # Get the message and chat_id from the POST request
    message = request.form['message']
    chat_id = request.form['chat_id']
    
    # Set the token for the Telegram bot
    bot_token = os.environ.get('BOT_TOKEN')
    
    # Set the URL for the Telegram Bot API
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    
    # Set the payload for the HTTP POST request
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    
    # Send the HTTP POST request using the requests library
    response = requests.post(url, data=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        return 'Message sent successfully!'
    else:
        return 'Error sending message:', response.text

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG'))
