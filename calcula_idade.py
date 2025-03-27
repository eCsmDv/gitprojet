import datetime

# Solicita a data de nascimento
data_nasc = input("Digite sua data de nascimento (dd/mm/yyyy): ")

# Converte a string em um objeto datetime, usando o formato correto
nascimento = datetime.datetime.strptime(data_nasc, "%d/%m/%Y")

# Obtém a data atual
hoje = datetime.datetime.today()

# Calcula a idade
idade = hoje.year - nascimento.year

# Ajuste para garantir que a pessoa já fez aniversário este ano
if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
    idade -= 1

# Exibe a idade
print(f"Tu tem {idade} anos.")