# Teste da Fase 3 do Projeto Integrador (T E S T  E !)
import time
import pymysql as psql

# Conexão com Banco de Dados
conexao = psql.connect(host='us-cdbr-east-06.cleardb.net', user='b1596403d7ceee', password='54a5695b', database='heroku_89484ac0f73b769',
                       cursorclass=psql.cursors.DictCursor, autocommit=True)


# Inicializar Sistema

# Tela de Entrada
# ------------------------------------ #
# --------------SQCA------------------ #
# ------------------------------------ #
# --------------LOGIN----------------- #
# --------------SIGN UP--------------- #
# ------------------------------------ #

# Criar Conta
def criar_conta(username):
    with conexao.cursor() as c:
        criar = f"INSERT INTO users (username) VALUES ('{username}')"
        try:
            c.execute(criar)
        except Exception as e:
            print(e)
        else:
            print(f'Criado! Seu usuário é: {username}')
            checar('users')


def checar(tabela):
    with conexao.cursor() as c:
        checa = f"SELECT * FROM {tabela}"
        try:
            c.execute(checa)
        except Exception as e:
            print(e)
        else:
            print(c.fetchall())


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


