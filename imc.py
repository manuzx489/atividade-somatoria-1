print("IMC (ídice de Massa Corporal)")
usu = input("Nome do Usuário: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
input(F"Seu IMC é:{imc:.2f}")




print("|------------------------------------------------------|")
print("| Faixa de IMC        | Classificação                  |")
print("|---------------------|--------------------------------|")
print("| < 18.5              | Abaixo do peso                 |")
print("| 18.5  – 24.9         | Peso normal                   |")
print("| 25.0 – 29.9         | Sobrepeso                      |")
print("| 30.0 – 34.9         | Obesidade Grau I               |")
print("| 35.0 – 39.9         | Obesidade Grau II              |")
print("| ≥ 40.0              | Obesidade Grau III (mórbida)   |")
print("|------------------------------------------------------|")



if imc <18.5 :
    print("Abaixo do peso,Foco em se alimentar de forma saudável,Você é mais do que seu peso!")

elif imc <= 24.9 :
    print("Peso normal,Você está fazendo um ótimo trabalho em manter um peso saudável!")

elif imc <= 29.9 :
    print("Sobrepeso,Você pode fazer mudanças saudáveis para melhorar sua saúde!")

elif imc <= 34.9 :
    print("Obesidade Grau I,Você não está sozinho nessa jornada!Busque apoio de profissionais")

elif imc <= 39.9 :
    print("Obesidade Grau II,Você é forte e capaz de superar desafios!Busque apoio de profissionais")

else:
    print("Obesidade Grau III,Você merece cuidado e apoio!Busque ajuda de profissionais")






