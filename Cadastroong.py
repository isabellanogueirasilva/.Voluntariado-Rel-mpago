def validar_texto_simples(txt):
    return txt.replace(" ", "").isalpha()

def validar_cnpj(cnpj):
    return cnpj.isdigit() and len(cnpj) == 14

def validar_email(email):
    dominios_validos = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com"]
    if "@" not in email:
        return False
    dominio = email.split("@")[-1]
    return dominio in dominios_validos

def validar_area(area):
    areas_validas = [
        "educacao", "saude", "meio ambiente",
        "idosos", "criancas", "animais",
        "alimentacao", "culturas"
    ]
    return area.lower() in areas_validas

print("=== Cadastro de ONG ===")

# Nome da ONG
while True:
    nome_ong = input("Nome da organização: ")
    if validar_texto_simples(nome_ong):
        break
    print("Nome inválido! Use apenas letras e espaços.")

# CNPJ
while True:
    cnpj = input("CNPJ (somente números, 14 dígitos): ")
    if validar_cnpj(cnpj):
        break
    print("CNPJ inválido!")

# Nome da responsável
while True:
    responsavel = input("Nome da responsável: ")
    if validar_texto_simples(responsavel):
        break
    print("Nome inválido! Use apenas letras e espaços.")

# Email
while True:
    email = input("E-mail: ")
    if validar_email(email):
        break
    print("E-mail inválido! Aceito: gmail, hotmail, outlook, yahoo.")

# Cidade
while True:
    cidade = input("Cidade da ONG: ")
    if validar_texto_simples(cidade):
        break
    print("Cidade inválida! Digite apenas letras.")

# Área de atuação
print("\nÁreas disponíveis:")
print("educacao, saude, meio ambiente, idosos, criancas, animais, alimentacao, culturas")

while True:
    area = input("Área de atuação: ")
    if validar_area(area):
        break
    print("Área inválida! Escolha uma da lista acima.")

# Senha
while True:
    senha = input("Crie uma senha (mínimo 6 caracteres): ")
    if len(senha) >= 6:
        break
    print("Senha curta demais!")

print("\nCadastro realizado com sucesso!")
print("Organização:", nome_ong)
print("CNPJ:", cnpj)
print("Responsável:", responsavel)
print("Email:", email)
print("Cidade:", cidade)
print("Área de atuação:", area)
