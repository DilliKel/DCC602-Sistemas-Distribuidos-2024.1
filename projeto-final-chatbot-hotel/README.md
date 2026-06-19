# Projeto Final — Chatbot de Check-in Hoteleiro

| | |
|---|---|
| 📚 Disciplina | DCC602 — Sistemas Distribuídos |
| 👨‍🏫 Professor | Leandro N. Balico |
| 🏛️ Universidade | Universidade Federal de Roraima (UFRR) |
| 📅 Semestre | 2024.1 |
| 👥 Autor | Kelvin Araújo Ferreira |
| 📌 Status | ✅ Concluído e apresentado |

## O que é

Chatbot de check-in hoteleiro via Telegram, multithreaded e containerizado com Docker. O bot coleta nome do hóspede, número de reserva e horário de chegada, suportando múltiplos hóspedes simultaneamente via threads.

## Tecnologias

- Python 3
- `Flask` — servidor web
- `telebot` — integração com Telegram Bot API
- `SQLite` / `MySQL` — persistência de dados
- `Docker` + `Docker Compose` — containerização
- `Apache JMeter` — testes de carga

## Como executar

```bash
# Instalar dependências
pip install flask pyTelegramBotAPI

# Abrir o notebook
jupyter notebook Untitled0.ipynb
```

## Funcionalidades

- Coleta de dados do hóspede via Telegram (nome, reserva, horário)
- Suporte a múltiplos hóspedes simultâneos com threads
- Persistência dos dados de check-in
- Containerização completa com Docker Compose
- Testes de carga com Apache JMeter

## Conceitos praticados

- Sistemas distribuídos com mensageria
- Concorrência e multithreading
- Containerização com Docker
- Bots e integração com APIs externas
- Testes de carga e desempenho
