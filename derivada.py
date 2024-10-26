import sympy as sp

def calcular_derivada(expressao, variavel):
    # Converte a entrada para uma expressão simbólica
    funcao = sp.sympify(expressao)
    var = sp.symbols(variavel)
    
    # Calcula a derivada da expressão em relação à variável fornecida
    derivada = sp.diff(funcao, var)
    derivada_simplificada = sp.simplify(derivada)
    
    return derivada_simplificada

def main():
    print("=== Programa para Calcular Derivadas ===")
    expressao = input("Digite a expressão a ser derivada: ")
    variavel = input("Digite a variável de derivação (ex: x, theta, etc.): ")
    
    try:
        resultado = calcular_derivada(expressao, variavel)
        print(f"\nA derivada de {expressao} em relação a {variavel} é: {resultado}")
    except Exception as e:
        print(f"Erro ao calcular a derivada: {e}")

if __name__ == "__main__":
    main()