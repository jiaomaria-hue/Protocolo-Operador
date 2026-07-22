# Define o limite e o valor da multa por km
limite = 80
valor_por_km = 7.0

# Solicita a velocidade do veículo
try:
    velocidade = float(input("Digite a velocidade do veículo (km/h): "))

    # Verifica se ultrapassou o limite usando o operador maior que (>)
    if velocidade > limite:
        # Calcula quantos km foram ultrapassados
        excedente = velocidade - limite
        
        # Calcula o valor total da multa
        multa = excedente * valor_por_km
        
        print(f"⚠️  Você ultrapassou o limite em {excedente:.1f} km/h!")
        print(f"💰 Valor da multa: R$ {multa:.2f}")
    else:
        print("✅ Velocidade dentro do limite. Dirija com segurança!")

except ValueError:
    print("❌ Por favor, digite um número válido para a velocidade.")   