from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

API_KEY = "suive la video pour voire comment implementer l'api_key pour votre projet"

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"
chat = client.chats.create(model=MODEL)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_api():
    try:
        data = request.get_json()
        user_msg = data.get("message")

        if not user_msg:
            return jsonify({"reply": "Message vide"}), 400

        response = chat.send_message(user_msg)

        reply = response.text.strip() if hasattr(response, 'text') else "Réponse vide"

        return jsonify({"reply": reply})

    except Exception as e:
        print(f"ERREUR GEMINI : {str(e)}")
        return jsonify({"reply": f"Erreur : {str(e)}"}), 500

if __name__ == "__main__":

    app.run(debug=True)

