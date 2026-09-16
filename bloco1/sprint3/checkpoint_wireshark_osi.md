# Checkpoint Wireshark — OSI Identification

## Pacote Capturado: IPv6 + UDP + Data

### Camada 3 (Rede) — Internet Protocol Version 6
- Protocolo: IPv6
- Source: 2800:3f0:4001:80a::200e (Google)
- Destination: 2804:16cc:b48:b00:e590:8af:cc2c:6d5e (Sua máquina)
- Função: Roteamento entre dois endereços IP globais

### Camada 4 (Transporte) — User Datagram Protocol
- Protocolo: UDP
- Source Port: 443 (HTTPS)
- Destination Port: 60649 (porta local)
- Length: 650 bytes
- Função: Entrega de dados sem garantia, com portas identificadas

### Camada 7 (Aplicação) — Data
- Payload: 642 bytes
- Tipo: Dados encriptados (QUIC/DNS ou similar)
- Função: Conteúdo que o usuário/aplicação consome

## Aprendizado
As 3 camadas trabalham juntas:
1. IPv6 decide o caminho até o destino (Camada 3)
2. UDP encapsula em portas (Camada 4)
3. Os dados dentro são a aplicação (Camada 7)

Sem uma, as outras não funcionam.