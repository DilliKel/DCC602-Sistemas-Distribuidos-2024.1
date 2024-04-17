# Atividade 1

## Autores
- Kelvin Araújo Ferreira - 2019037653 - [DilliKel](https://github.com/DilliKel)
- Mateus Moraes de Moura - 2019027100 - [mateusmoraes99](https://github.com/mateusmoraes99)

### Objetivo
Implementação de um chat cliente e servidor TCP em Python, com suporte a multiusuários e com um recurso de segurança, criptografia na comunicação aos programas cliente e servidor para garantir a confidencialidade das informações
trocadas com a biblioteca base64.

### Imports utilizados
    sys
    socket
    base64
    threading

### Teste da comunicação
![teste_chat.png] (Atividade Prática 01 - ClienteServidorPython/teste_chat.png)

#### Utilizado o comando 
      sudo tcpdump -i any 'port 5000'
Para capturar e analisar pacotes de outras comunicações na rede
