import os
from flask import Flask, request, send_file, jsonify
from gradio_client import Client, handle_file

app = Flask(__name__)

# Token Environment Variable se uthayega
HF_TOKEN = os.getenv("HF_TOKEN")
# Space ka connection
client = Client("Qwen/Qwen3-TTS", hf_token=HF_TOKEN)

@app.route('/')
def home():
    return "AstraToonix Voice Engine is Running!"

@app.route('/generate-voice', methods=['POST'])
def generate():
    try:
        data = request.json
        target_text = data.get('text')

        if not target_text:
            return jsonify({"error": "No text provided"}), 400

        # AI Voice Cloning Logic
        # Dhyaan rakhna 'my_voice.mp3' file repo mein honi chahiye
        result = client.predict(
            ref_audio=handle_file('my_voice.mp3'),
            ref_text="Hi mera naam hai Raj dev mein Lumding Assam se hoon", # Isko apne audio ke hisaab se change kar lena
            target_text=target_text,
            language="Auto",
            use_xvector_only=False,
            model_size="1.7B",
            api_name="/generate_voice_clone"
        )
        
        # Generated audio file path result[0] mein hota hai
        return send_file(result[0], mimetype="audio/wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Koyeb ke liye port 8080 standard hai
    app.run(host='0.0.0.0', port=8080)
  
