# Atividade 04 — Chamada de Procedimento Remoto (RPC) com gRPC

| | |
|---|---|
| 📚 Disciplina | DCC602 — Sistemas Distribuídos |
| 👨‍🏫 Professor | Leandro N. Balico |
| 🏛️ Universidade | Universidade Federal de Roraima (UFRR) |
| 📅 Semestre | 2024.1 |
| 👥 Equipe | Kelvin Araújo Ferreira, Mateus Moraes |

## O que é

Serviço gRPC para execução remota de comandos shell. Define um contrato via Protocol Buffers (`.proto`), sobe um servidor com `ThreadPoolExecutor` e um cliente que envia comandos como `ls -l` e `df -h` para execução remota.

## Tecnologias

- Python 3
- `grpcio` e `grpcio-tools` — framework gRPC
- `protobuf` — serialização via Protocol Buffers
- `subprocess` — execução de comandos shell no servidor

## Como executar

```bash
# Instalar dependências
pip install grpcio grpcio-tools protobuf

# Abrir o notebook
jupyter notebook Atividade4.ipynb
```

## Funcionalidades

- Definição de serviço RPC via Protocol Buffers inline
- Servidor gRPC em `localhost:50051` com pool de threads
- Cliente que envia comandos shell e recebe a saída remotamente
- Método `ExecuteCommand` no serviço `RemoteControl`

## Conceitos praticados

- Remote Procedure Call (RPC)
- Protocol Buffers e contratos de interface
- gRPC e comunicação HTTP/2
- Execução remota de comandos

## Observação

Esta implementação usa `grpc.insecure_channel()` — adequado para ambiente acadêmico. Em produção, utilize TLS com `grpc.secure_channel()`.
