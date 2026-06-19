# %%
# pip install grpcio grpcio-tools click

# %%
# Conteúdo do arquivo remote_control.proto (gerado via %%writefile no notebook):
#
# syntax = "proto3";
#
# package remote_control;
#
# service RemoteControl {
#     rpc ExecuteCommand (CommandRequest) returns (CommandResponse);
# }
#
# message CommandRequest {
#     string command = 1;
# }
#
# message CommandResponse {
#     string result = 1;
#     int32 status_code = 2;
# }

# %%
# python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. remote_control.proto

# %%
import grpc
from concurrent import futures
import subprocess
import remote_control_pb2_grpc
import remote_control_pb2

class RemoteControlServicer(remote_control_pb2_grpc.RemoteControlServicer):
    def ExecuteCommand(self, request, context):
        try:
            result = subprocess.run(request.command, shell=True, capture_output=True, text=True)
            return remote_control_pb2.CommandResponse(result=result.stdout, status_code=result.returncode)
        except Exception as e:
            return remote_control_pb2.CommandResponse(result=str(e), status_code=-1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    remote_control_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControlServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051")
    server.wait_for_termination()

# Execute o servidor em segundo plano
import threading
server_thread = threading.Thread(target=serve)
server_thread.start()

# %%
import grpc
import remote_control_pb2_grpc
import remote_control_pb2

def execute_command(command):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = remote_control_pb2_grpc.RemoteControlStub(channel)
        response = stub.ExecuteCommand(remote_control_pb2.CommandRequest(command=command))
        return response.result, response.status_code

# Teste o cliente enviando um comando
resultado, status_code = execute_command('ls -l')
print(f"Resultado:\n{resultado}")
print(f"Código de Status: {status_code}")

# %%
# Enviar um comando para listar os arquivos no diretório atual
resultado, status_code = execute_command('ls -l')
print(f"Resultado:\n{resultado}")
print(f"Código de Status: {status_code}")

# %%
# Enviar um comando para verificar o espaço em disco
resultado, status_code = execute_command('df -h')
print(f"Resultado:\n{resultado}")
print(f"Código de Status: {status_code}")
