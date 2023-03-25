# Teste da Fase 3 do Projeto Integrador (T E S T  E !)
import time
import pymysql as psql

# Conexão com Banco de Dados
conexao = psql.connect(host='us-cdbr-east-06.cleardb.net', user='b1596403d7ceee', password='54a5695b', database='heroku_89484ac0f73b769',
                       cursorclass=psql.cursors.DictCursor, autocommit=True)


def criar_conta(username):
    with conexao.cursor() as c:
        criar = f"INSERT INTO ares (ar_name) VALUES ('{username}')"
        try:
            c.execute(criar)
        except Exception as e:
            igual = f'''(1062, "Duplicate entry '{username}' for key 'PRIMARY'")'''
            if str(e) == igual:
                return f'O ar {username} já existe, escolha outro nome!'
        else:
            return f'O ar {username} foi criado com sucesso!'


def usuarios(qual, qual2):
    with conexao.cursor() as c:
        if qual == 'ares':
            checa = f"SELECT * FROM {qual} ORDER BY ar_name"
        elif qual == 'amostras':
            checa = f"SELECT amostra_name FROM {qual} WHERE ar_name = '{qual2}' ORDER BY amostra_name"
        try:
            c.execute(checa)
        except Exception as e:
            return e
        else:
            resposta = c.fetchall()
            resposta_list = []
            for r in resposta:
                if qual == 'ares':
                    r = r.get('ar_name')
                    resposta_list.append(r.title())
                elif qual == 'amostras':
                    r = r.get('amostra_name')
                    resposta_list.append(r.title())
            return resposta_list


def get_amostras(namear, nameam):
    with conexao.cursor() as c:
        get = f"SELECT mp10,mp25,o3,co,no2,so2 FROM amostras WHERE ar_name = '{namear}' AND amostra_name = '{nameam}'"
        try:
            c.execute(get)
        except Exception as e:
            return e
        else:
            resposta = c.fetchall()
            resposta_list = []
            return resposta[0]


def clean(tabela):
    clean = f"DELETE FROM {tabela}"
    with conexao.cursor() as c:
        try:
            c.execute(clean)
        except Exception as e:
            return e
        else:
            return 'limpo'


def inserir(nome_ar, nome_amostra, mp10, mp25, o3, co, no2, so2):
    insercao = f'''INSERT INTO amostras (amostra_name, ar_name, mp10, mp25, o3, co, no2, so2) VALUES ('{nome_amostra}','{nome_ar}',{mp10},{mp25},{o3},
                                                                                                                                  {co},{no2},{so2})'''
    with conexao.cursor() as c:
        try:
            c.execute(insercao)
        except Exception as e:
            _nome_igual = f'''(1062, "Duplicate entry '{nome_amostra}' for key 'amostra_name'")'''
            if str(e) == _nome_igual:
                return f'A amostra {nome_amostra} já existe, escolha outro nome!'
        else:
            return f'A amostra {nome_amostra} foi criada com sucesso!'


def alterar(nome_amostra, mp10, mp25, o3, co, no2, so2):
    alteracao = f'''UPDATE amostras SET mp10 = {mp10},mp25 = {mp25},o3 = {o3},co = {co},no2 = {no2}, so2 = {so2} WHERE amostra_name = '{nome_amostra}';'''
    with conexao.cursor() as c:
        try:
            c.execute(alteracao)
        except Exception as e:
            _nome_igual = f'''(1062, "Duplicate entry '{nome_amostra}' for key 'amostra_name'")'''
            if str(e) == _nome_igual:
                return f'A amostra {nome_amostra} já existe, escolha outro nome!'
            else:
                return str(e)
        else:
            return f'A amostra {nome_amostra} foi alterada com sucesso!'


def deletar(nome_amostra):
    _del = f"DELETE FROM amostras WHERE amostra_name = '{nome_amostra}'"
    with conexao.cursor() as c:
        try:
            c.execute(_del)
        except Exception as e:
            return str(e)
        else:
            return f'A amostra {nome_amostra} foi deletada com sucesso!'
