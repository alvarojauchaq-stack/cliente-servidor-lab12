from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar mensajes de todos los clientes
data_store = []

# Ruta para obtener todos los mensajes
@app.route('/get', methods=['GET'])
def get_messages():
    return jsonify({"messages": data_store})

# Ruta para enviar un mensaje
@app.route('/post', methods=['POST'])
def post_message():
    content = request.json
    if "message" in content:
        data_store.append(content["message"])
        return jsonify({"status": "success", "messages": data_store})
    return jsonify({"status": "error", "message": "No se proporcionó 'message'"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)




