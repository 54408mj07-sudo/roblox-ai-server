from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# 1. Get the API Key from the Environment (Security)
api_key = os.environ.get("GROQ_API_KEY")

# 2. Initialize the Groq Client
client = Groq(api_key=api_key)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 3. Get the message from Roblox
        data = request.json
        user_message = data.get('message')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # 4. Send the message to Groq
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant in a Roblox game. Keep responses short and kid-friendly."
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="llama3-8b-8192",  # Groq's fast model
        )

        # 5. Get the reply text
        ai_reply = chat_completion.choices[0].message.content

        # 6. Send it back to Roblox
        return jsonify({'reply': ai_reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'reply': 'Sorry, the AI brain is frozen.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
