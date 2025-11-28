def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_email(email):
    dominios_validos = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com"]
    if "@" not in email:
        return False
    parte_final = email.split("@")[-1]
    return parte_final in dominios_validos

def validar_telefone(tel):
    tel = tel.replace(" ", "").replace("-", "")
    return tel.isdigit() and len(tel) >= 10 and len(tel) <= 11

def validar_data_nascimento(data):
    try:
        dia, mes, ano = map(int, data.split("/"))
        if ano < 1900 or ano > 2025:
            return False
        if not (1 <= mes <= 12):
            return False
        if not (1 <= dia <= 31):
            return False
        return True
    except:
        return False


print("=== Cadastro Voluntario ===")


while True:
    nome = input("Digite seu nome completo: ")
    if validar_nome(nome):
        break
    print("Nome inválido! Use apenas letras e espaços.")

# CPF
while True:
    cpf = input("Digite seu CPF (somente números): ")
    if validar_cpf(cpf):
        break
    print("CPF inválido! Deve ter exatamente 11 números.")

# E-mail
while True:
    email = input("Digite seu e-mail: ")
    if validar_email(email):
        break
    print("E-mail inválido! Aceito apenas gmail, hotmail, outlook e yahoo.")

# Telefone
while True:
    telefone = input("Digite seu telefone com DDD (ex: 11912345678): ")
    if validar_telefone(telefone):
        break
    print("Telefone inválido!")


while True:
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    if validar_data_nascimento(data):
        break
    print("Data inválida! Verifique o formato e valores.")


while True:
    habilidades = input("Digite suas habilidades (texto curto): ")
    if len(habilidades) <= 100:
        break
    print("Texto muito grande! Digite algo menor.")

print("\nCadastro concluído com sucesso!")
print("Nome:", nome)
print("CPF:", cpf)
print("E-mail:", email)
print("Telefone:", telefone)
print("Data de nascimento:", data)
print("Habilidades:", habilidades)
