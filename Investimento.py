from babel.numbers import format_currency

def obter_numero_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")

def obter_numero_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))  # Substitui vírgula por ponto, se necessário
            return valor
        except ValueError:
            print("Digite um número válido.")

def introdução():
    print("""\nBem-vindo ao programa de cálculo de investimento!\n
Este programa permite calcular o rendimento e o valor final de um investimento com impostos.
Você precisará fornecer informações como o valor do investimento, o número de meses, a taxa de rendimento mensal e a taxa de imposto.
Vamos começar...\n""")
    calcular_investimento()

def calcular_investimento():
    # Variáveis
    investimento = obter_numero_float("Qual valor deseja investir? ")
    meses = obter_numero_inteiro("Por quantos meses deseja investir? ")
    tx_rendimento = obter_numero_float("Qual é a porcentagem da taxa de rendimento mensal? ")
    tx_imposto = obter_numero_float("Qual é a porcentagem da taxa de imposto para investir? ")

    # Conversão dos números
    taxa_rendimento = tx_rendimento / 100
    taxa_imposto = tx_imposto / 100

    # Cálculos
    rendimento_total = investimento * ((1 + taxa_rendimento) ** meses - 1)
    imposto = rendimento_total * taxa_imposto
    valor_final = investimento + rendimento_total - imposto

    # Conversão para moeda brasileira
    rendimento_total_formatado = format_currency(rendimento_total, 'BRL', locale='pt_BR')
    imposto_formatado = format_currency(imposto, 'BRL', locale='pt_BR')
    valor_final_formatado = format_currency(valor_final, 'BRL', locale='pt_BR')

    mensagem_final(rendimento_total_formatado, imposto_formatado, valor_final_formatado, meses)

def mensagem_final(rendimento_total_formatado, imposto_formatado, valor_final_formatado, meses):
    # Mensagem final
    print(f"""\nVocê investindo por {meses} meses.
Terá rendimento total de {rendimento_total_formatado}.
Tendo um desconto de {imposto_formatado}.
Seu valor final será {valor_final_formatado}""")

def perguntar_outro_investimento():
    while True:
        resposta = input("\nDeseja fazer a consulta de outro investimento? (S para Sim, N para Não): ").strip().lower()
        if resposta == 's':
            calcular_investimento()
        elif resposta == 'n':
            print("O programa foi encerrado.")
            break
        else:
            print("Resposta inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")

introdução()
perguntar_outro_investimento()