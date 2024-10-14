# arquivo: main.py
# Dica de compilação: Caso o run seja feito no vscode, utilizar a opção 'run python file' que se encontra nas opções de run
def calculo(p, a):
    if p <= 0 or p>1000:
        return -1
    if a < 0 or a > 3.5:
        return -1
    return p / (a * a)

def main():
    print("Olá, seja bem-vindo(a). Vamos calcular seu IMC")
    
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return

    imc = calculo(peso, altura)

    if imc != -1:
        print(f"O seu IMC é: {imc:.2f}")
        if imc < 18.5:
            print("O seu IMC é classificado como Magreza")
        elif 18.5 <= imc <= 24.9:
            print("O seu IMC é classificado como Normal")
        elif 25 <= imc <= 29.9:
            print("O seu IMC é classificado como Sobrepeso")
        elif 30 <= imc <= 34.9:
            print("O seu IMC é classificado como Obesidade grau I")
        elif 35 <= imc <= 39.9:
            print("O seu IMC é classificado como Obesidade grau II")
        elif imc >= 40:
            print("O seu IMC é classificado como Obesidade grau III")
    else:
        print("Você infelizmente digitou algo errado, tente de novo por favor")

if __name__ == "__main__":
    main()