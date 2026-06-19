# %%
# Kelvin Araújo Ferreira - 2019037653
# Mateus Moraes de Moura - 2019027100

# %%
import socket
import threading

# Função para lidar com a conexão do cliente
def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")

    connected = True
    while connected:
        msg = conn.recv(1024).decode()
        if msg:
            if msg.lower() == "quit":
                connected = False
            else:
                reversed_msg = msg[::-1]
                conn.sendall(reversed_msg.encode())
                print(f"[{addr}] Mensagem original: {msg} | Mensagem invertida: {reversed_msg}")

    conn.close()
    print(f"[DESCONECTADO] {addr} desconectado.")

# Função para iniciar o servidor
def start_server():
    host = "localhost"
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[ESPERANDO CONEXÕES] Servidor está ouvindo em {host}:{port}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[CONEXÕES ATIVAS] {threading.activeCount() - 1}")

# Iniciando o servidor em uma thread separada para não bloquear o notebook
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# %%
import socket
import threading

# Função para enviar mensagem ao servidor
def send_message(msg, host="localhost", port=12345):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.sendall(msg.encode())
    response = client.recv(1024).decode()
    print(f"Mensagem enviada: {msg} | Resposta do servidor: {response}")
    client.close()

# Função para iniciar o cliente
def start_client():
    host = "localhost"
    port = 12345

    while True:
        msg = input("Digite a mensagem a ser enviada (ou 'quit' para sair): ")
        if msg.lower() == "quit":
            break
        thread = threading.Thread(target=send_message, args=(msg, host, port))
        thread.start()

# Iniciar o cliente em uma thread separada
client_thread = threading.Thread(target=start_client)
client_thread.start()

# %%
import time
import psutil
import matplotlib.pyplot as plt

# Função para simular um ataque DoS enviando múltiplas requisições
def mass_request_test(num_requests, message_size):
    host = "localhost"
    port = 12345
    message = "x" * message_size  # Mensagem de tamanho específico

    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_message, args=(message, host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Função para monitorar o uso de recursos
def monitor_performance(duration=10):
    cpu_usage = []
    memory_usage = []
    network_usage = []

    for _ in range(duration):
        cpu_usage.append(psutil.cpu_percent(interval=1))
        memory_usage.append(psutil.virtual_memory().percent)
        network_usage.append(psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv)

    return cpu_usage, memory_usage, network_usage

# Iniciar o monitoramento de desempenho
cpu_usage, memory_usage, network_usage = monitor_performance(duration=30)

# Simular um teste de 1000 requisições com mensagens de 512 bytes
mass_request_test(num_requests=1000, message_size=512)

# Plotar os resultados
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(cpu_usage, label='CPU Usage (%)')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(memory_usage, label='Memory Usage (%)')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(network_usage, label='Network Usage (Bytes)')
plt.legend()

plt.tight_layout()
plt.show()
