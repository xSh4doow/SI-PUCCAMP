# Teste da Fase 3 do Projeto Integrador (T E S T  E !)
import time
import pymysql as psql

# Conexão com Banco de Dados
conexao = psql.connect(host='us-cdbr-east-06.cleardb.net', user='b1596403d7ceee', password='54a5695b', database='heroku_89484ac0f73b769',
                       cursorclass=psql.cursors.DictCursor, autocommit=True)


def criar_conta(username):
    with conexao.cursor() as c:
        criar = f"INSERT INTO users (username) VALUES ('{username}')"
        try:
            c.execute(criar)
        except Exception as e:
            igual = f'''(1062, "Duplicate entry '{username}' for key 'username_UNIQUE'")'''
            if str(e) == igual:
                return f'O ar {username} já existe, escolha outro nome!'
        else:
            return f'O ar {username} foi criado com sucesso!'


def usuarios(tabela):
    with conexao.cursor() as c:
        checa = f"SELECT * FROM {tabela} ORDER BY username"
        try:
            c.execute(checa)
        except Exception as e:
            return e
        else:
            users = c.fetchall()
            user_list = []
            for user in users:
                a = user.get('username')
                user_list.append(a.title())
            return user_list


def login(username):
    with conexao.cursor() as c:
        login_sql = f"SELECT * FROM users WHERE username='{username}'"
        try:
            c.execute(login_sql)
            resp = c.fetchall()
            if resp != ():
                print(f'Logado! Seu usuário é: {username}')
            else:
                print('Username Inválido')
        except Exception as e:
            print(e)


def clean(tabela):
    clean = f"DELETE FROM {tabela}"
    with conexao.cursor() as c:
        try:
            c.execute(clean)
        except Exception as e:
            return e
        else:
            return 'limpo'
