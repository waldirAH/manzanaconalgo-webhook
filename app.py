from flask import Flask, request, send_file
import os

app = Flask(__name__)

# ====== META (Messenger) verify token ======
VERIFY_TOKEN = "manzana_verify_123"

# ====== TikTok verify file (el .txt que creaste en GitHub) ======
TIKTOK_VERIFY_FILE = "tiktok0cpl6QNkcRDdlhAdbTqh8ALvOuO20OrE.txt"


@app.get("/")
def home():
    return "OK", 200


# ====== TikTok: servir archivo en la raíz ======
@app.get(f"/{TIKTOK_VERIFY_FILE}")
def tiktok_verify():
    # El archivo está en la raíz del proyecto (mismo nivel que app.py)
    file_path = os.path.join(os.path.dirname(__file__), TIKTOK_VERIFY_FILE)
    return send_file(file_path, mimetype="text/plain")


# ====== Páginas requeridas por TikTok ======
@app.get("/terminos")
def terminos():
    return """
    <h1>Términos de servicio</h1>
    <p>Manzanaconalgo es una plataforma web para ayudar a negocios a gestionar interacciones y automatizar respuestas con reglas e IA, según permisos autorizados.</p>
    <p>El usuario es responsable del contenido que publica y puede desconectar la integración cuando quiera.</p>
    <p>Contacto: waldiralvaradoherrera@gmail.com</p>
    """, 200


@app.get("/privacidad")
def privacidad():
    return """
    <h1>Política de privacidad</h1>
    <p>Recopilamos únicamente los datos necesarios para la autenticación e integración (por ejemplo, tokens y datos básicos permitidos por los permisos autorizados).</p>
    <p>No vendemos datos. El usuario puede solicitar eliminación de datos escribiendo al correo de contacto.</p>
    <p>Contacto: waldiralvaradoherrera@gmail.com</p>
    """, 200


# ====== Meta Webhook (GET: verificación) ======
@app.get("/webhook/meta")
def verify_meta():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Forbidden", 403


# ====== Meta Webhook (POST: mensajes entrantes) ======
@app.post("/webhook/meta")
def receive_meta():
    data = request.get_json(silent=True) or {}
    print("MESSENGER IN:", data)
    return "OK", 200
