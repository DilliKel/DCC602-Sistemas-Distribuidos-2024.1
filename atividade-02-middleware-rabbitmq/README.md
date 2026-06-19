# Atividade 2: Middleware com RabbitMQ

## Autores
- Kelvin Araújo Ferreira - 2019037653 - [DilliKel](https://github.com/DilliKel)
- Mateus Moraes de Moura - 2019027100 - [mateusmoraes99](https://github.com/mateusmoraes99)

## Atividade: Simulação de uma aplicação de IoT para detecção de incêndio

Objetivo

Desenvolver uma aplicação simples de IoT para simular a detecção de incêndio em um ambiente, utilizando a temperatura da CPU como referência.

### Materiais necessários

    Computador com sistema operacional Windows, Linux ou macOS
    Linguagem de programação Python (versão 3.x)
    Biblioteca de cliente RabbitMQ para Python (pika)
    Biblioteca do python psutil (psutil)
    Biblioteca de cor em python (termcolor)

### Relatório

- Implemente um produtor que publique a temperatura da CPU em um tópico do RabbitMQ. [Producer_temp_cpu.py](Middeware%20RabbitMQ/producer_temp_cpu.py)
- Implemente um consumidor que receba a temperatura da CPU do RabbitMQ e verifique se ela está acima de um determinado limite (por exemplo, 50 graus Celsius). Caso a temperatura esteja acima do limite, o consumidor deve publicar uma mensagem em um novo tópico indicando que foi detectado um incêndio. [Consumer.py](Middeware%20RabbitMQ/consumer.py)
- Implemente um novo consumidor que receba a mensagem do tópico de detecção de incêndio, emite uma mensagem em vermelho e ela também envie uma mensagem para um outro tópico indicando que o sistema de prevenção de incêndio deve ser ativado. [Fire_alarm.py](Middeware%20RabbitMQ/fire_alarm.py)
    
