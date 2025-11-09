import requests
from threading import Thread
import random  # Import necesario para seleccionar servidor aleatorio

# Lista de servidores disponibles
SERVERS = ["http://127.0.0.1:5000", "http://127.0.0.1:5001"]

# Función que simula un cliente
def cliente_simulado(id_cliente, nuevo_mensaje):
    # Seleccionar servidor aleatorio para balanceo de carga
    server = random.choice(SERVERS)
    
    # GET inicial
    response = requests.get(f"{server}/get")
    print(f"Cliente {id_cliente} GET desde {server}:", response.json())
    
    # POST con mensaje propio
    response = requests.post(f"{server}/post", json={"message": nuevo_mensaje})
    print(f"Cliente {id_cliente} POST hacia {server}:", response.json())

# Crear múltiples clientes concurrentes
numero_clientes = 5  # puedes cambiar la cantidad
hilos = []

for i in range(numero_clientes):
    hilo = Thread(target=cliente_simulado, args=(i+1, f"Mensaje desde cliente {i+1}"))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()
