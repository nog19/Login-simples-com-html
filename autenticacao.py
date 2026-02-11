import hashlib

user_db = 'adm'
pass_db = '1234'

def autenticar_usuario():
    username = input('Digite o nome de usuário: ')
    password = input('Digite a senha: ')

    # Hash da senha digitada
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Hash da senha armazenada
    hashed_pass_db = hashlib.sha256(pass_db.encode()).hexdigest()

    if username == user_db and hashed_password == hashed_pass_db:
        print('Autenticação bem-sucedida!')
    else:
        print('Nome de usuário ou senha incorretos.')

if __name__ == "__main__":
    autenticar_usuario()