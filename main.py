from flask import Flask, request, jsonify
import os
# You would usually use the 'openai' library here, but this is a mock example
import requests

app = Flask(__name__)

MY_GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    # 1. Get data from Roblox
    data = request.json
    user_message = data.get('message')
    
    # 2. Send to AI (e.g., OpenAI)
    # (This is pseudo-code for the AI call)
    ai_response = call_ai_service(user_message) 
    
    # 3. Send answer back to Roblox
    return jsonify({'reply': ai_response})

def call_ai_service(text):
    # Here you would actually call OpenAI/Groq API
    return "AI says: " + text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
