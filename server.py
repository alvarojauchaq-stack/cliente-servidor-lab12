from flask import Flask, request, jsonify
import requests  # Import necesario para replicar mensajes

app = Flask(__name__)

# Lista para almacenar mensajes de todos los clientes
data_store = []

# URL del servidor réplica (puerto 5001)
REPLICA_URL = "http://127.0.0.1:5001/post"

# Ruta para obtener todos los mensajes
@app.route('/get', methods=['GET'])
def get_messages():
    return jsonify({"messages": data_store})

# Ruta para enviar un mensaje y replicarlo
@app.route('/post', methods=['POST'])
def post_message():
    content = request.json
    if "message" in content:
        # Guardar mensaje local
        data_store.append(content["message"])
        
        # Intentar replicar el mensaje en el servidor secundario
        try:
            requests.post(REPLICA_URL, json={"message": content["message"]})
        except:
            print("No se pudo replicar el mensaje en server2")

        return jsonify({"status": "success", "messages": data_store})
    
    return jsonify({"status": "error", "message": "No se proporcionó 'message'"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

