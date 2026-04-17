import os
from flask import Flask, request, send_file, jsonify
from gradio_client import Client, handle_file

app = Flask(__name__)

hf_client = None

def get_client():
    global hf_client
    if hf_client is None:
        token = os.getenv("HF_TOKEN")
        hf_client = Client("Qwen/Qwen3-TTS", hf_token=token)
    return hf_client

@app.route('/')
def home():
    return "AstraToonix Voice Engine is Online!"

@app.route('/generate-voice', methods=['POST'])
def generate():
    try:
        data = request.json
        target_text = data.get('text')
        
        if not target_text:
            return jsonify({"error": "No text provided"}), 400

        client = get_client()
        
        # Yahan tumhari exact file aur exact text daal diya hai!
        result = client.predict(
            ref_audio=handle_file('Me_voice_sample.mp3'), 
            ref_text="Hi mera naam hai Raj dev mein Lumding Assam se hoon Main ek developer hu main telegram bahut AI vagaira mein Ruchi rakhta hun mujhe project banana coding karna bahut achcha lagta hai",
            target_text=target_text,
            language="Auto",
            use_xvector_only=False,
            model_size="1.7B",
            api_name="/generate_voice_clone"
        )
        
        return send_file(result[0], mimetype="audio/wav")

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    
