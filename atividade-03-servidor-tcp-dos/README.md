# Atividade 03 — Servidor TCP com Simulação de Ataque DoS

| | |
|---|---|
| 📚 Disciplina | DCC602 — Sistemas Distribuídos |
| 👨‍🏫 Professor | Leandro N. Balico |
| 🏛️ Universidade | Universidade Federal de Roraima (UFRR) |
| 📅 Semestre | 2024.1 |
| 👥 Equipe | Kelvin Araújo Ferreira, Mateus Moraes |

## O que é

Servidor TCP de inversão de strings com simulação de ataque DoS e monitoramento de desempenho em tempo real. O notebook implementa servidor, cliente e um teste de carga com 1.000 requisições simultâneas, coletando métricas de CPU, memória e rede com geração de gráficos.

## Tecnologias

- Python 3
- `socket` — comunicação TCP
- `threading` — concorrência no servidor
- `psutil` — monitoramento de CPU e memória
- `matplotlib` — geração de gráficos de desempenho

## Como executar

```bash
# Instalar dependências
pip install psutil matplotlib

# Abrir o notebook
jupyter notebook atividade_3_sistemas_distribuidos_.ipynb
```

## Funcionalidades

- Servidor TCP em `localhost:12345` com thread por cliente
- Inversão de strings recebidas dos clientes
- Simulação de ataque DoS com 1.000 conexões simultâneas (512 bytes cada)
- Monitoramento de CPU, memória e rede durante o ataque
- Geração de gráficos comparativos de desempenho

## Conceitos praticados

- Protocolo TCP/IP
- Concorrência com threads
- Simulação e análise de ataques DoS
- Monitoramento de desempenho de servidores
