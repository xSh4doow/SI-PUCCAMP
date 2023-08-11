Curso = [{"Codigo": 123, "Nome": "Sistemas de Informação", "Duracao": 4},
         {"Codigo": 213, "Nome": "Ciência de Dados e IA", "Duracao": 4},
         {"Codigo": 321, "Nome": "Engenharia Biomédica", "Duracao": 5}]

Curriculo = [{"Id": 123654, "CodigoCurso": 123, "AnoImplantacao": 2020, "SemestreImplantacao": 1},
             {"Id": 123655, "CodigoCurso": 213, "AnoImplantacao": 2021, "SemestreImplantacao": 1},
             {"Id": 123656, "CodigoCurso": 321, "AnoImplantacao": 2022, "SemestreImplantacao": 1}]

Disciplina = [{"Codigo": 12345, "Nome": "Calculo I", "Creditos": 6},
              {"Codigo": 12121, "Nome": "Álgebra Linear", "Creditos": 4},
              {"Codigo": 11211, "Nome": "Engenharia de Software", "Creditos": 2}]

Componente = [{"IdCurriculo": 123656, "CodigoDisciplina": [11211]},
              {"IdCurriculo": 123655, "CodigoDisciplina": [11211]},
              {"IdCurriculo": 123654, "CodigoDisciplina": [12121]}]

Aluno = [{"RA": 22334455, "Nome": "José da Silva", "Telefone": 19991919191},
         {"RA": 21918171, "Nome": "Maria da Silva", "Telefone": 11991223344},
         {"RA": 20202020, "Nome": "João de Souza", "Telefone": 21993456789}]

Ingresso = [{"IdCurriculo": 123654, "Semestre": 2, "Ano": 2022, "RaAluno": [22334455]},
            {"IdCurriculo": 123655, "Semestre": 2, "Ano": 2022, "RaAluno": [21918171]},
            {"IdCurriculo": 123656, "Semestre": 1, "Ano": 2023, "RaAluno": [20202020]}]

Professor = [{"Matricula": 94949494, "Nome": "André Carvalho"},
             {"Matricula": 99123321, "Nome": "Mário Lima"},
             {"Matricula": 98765432, "Nome": "Daniele Almeida"}]

Turma = [{"Id": 123123, "Ano": 2022, "Semestre": 2, "Letra": "A", "CodigoDisciplina": 12345, "MatriculaProfessor": 99123321},
         {"Id": 123124, "Ano": 2022, "Semestre": 1, "Letra": "B", "CodigoDisciplina": 12345, "MatriculaProfessor": 98765432},
         {"Id": 123125, "Ano": 2022, "Semestre": 1, "Letra": "A", "CodigoDisciplina": 11211, "MatriculaProfessor": 99123321},
         {"Id": 123456, "Ano": 2023, "Semestre": 1, "Letra": "A", "CodigoDisciplina": 12345, "MatriculaProfessor": 99123321},
         {"Id": 123457, "Ano": 2023, "Semestre": 1, "Letra": "B", "CodigoDisciplina": 12345, "MatriculaProfessor": 98765432},
         {"Id": 123458, "Ano": 2023, "Semestre": 1, "Letra": "A", "CodigoDisciplina": 11211, "MatriculaProfessor": 99123321}]

Matricula = [{"IdTurma": 123456, "RaAluno": [22334455]},
             {"IdTurma": 123458, "RaAluno": [22334455]},
             {"IdTurma": 123457, "RaAluno": [21918171]}]

Resultado = [{"RaAluno": 20202020, "IdTurma": 123123, "Nota": 7.5, "Frequencia": 8},
             {"RaAluno": 22334455, "IdTurma": 123125, "Nota": 3.5, "Frequencia": 65},
             {"RaAluno": 21918171, "IdTurma": 123123, "Nota": 6.0, "Frequencia": 32}]


# 1
def duracao_curso(nomeCurso, listaCurso):
    for curso in listaCurso:
        if curso['Nome'] == nomeCurso:
            return f'A duração do curso: {nomeCurso} é de: {curso["Duracao"]} anos!'
    return None


# 2
def curriculo_tupla(idCurriculo, listaCurriculos):
    for curriculo in listaCurriculos:
        if curriculo['Id'] == idCurriculo:
            return curriculo['AnoImplantacao'], curriculo['SemestreImplantacao']
    return None


# 3
def qntdCreditos(codDisc, listaDisc):
    for disc in listaDisc:
        if disc['Codigo'] == codDisc:
            return f'A quantidade de créditos da disciplina: {disc["Nome"]} é de {disc["Creditos"]}.'
    return None


# 4
def verificarDisc(idCurr, codDisc, listaComp):
    for componente in listaComp:
        if componente['IdCurriculo'] == idCurr and codDisc in componente['CodigoDisciplina']:
            return True
    return False


# 5
def pegarTelefone(raAluno, listaAlunos):
    for aluno in listaAlunos:
        if raAluno == aluno['RA']:
            return aluno['Telefone']
    return None


# 6
def pegarAlunos(idCurr, Semestre, anoIngresso, listaIngressos, listaAlunos):
    RAs = 0
    alunos = []
    for ingresso in listaIngressos:
        if idCurr == ingresso['IdCurriculo'] and Semestre == ingresso['Semestre'] and anoIngresso == ingresso['Ano']:
            RAs = ingresso['RaAluno']

    def _pegarNomeAluno(ra, _aluno):
        for ra in ra:
            if _aluno['RA'] == ra:
                return _aluno['Nome']
            else:
                return None

    for aluno in listaAlunos:
        _hold = _pegarNomeAluno(RAs, aluno)
        if _hold is not None:
            alunos.append(_hold)

    return alunos


# 7
def nomeProf(matriculaProf, listaProf):
    for prof in listaProf:
        if prof['Matricula'] == matriculaProf:
            return prof['Nome']
    return None


# 8
def profAula(idTurma, listaTurmas):
    matricula_p = 0
    for turma in listaTurmas:
        if turma['Id'] == idTurma:
            matricula_p = turma['MatriculaProfessor']

    return nomeProf(matricula_p, Professor)


# 9
def alunosMatriculados(idTurma, listaMatriculas, listaAluno):
    raaluno = []
    matriculados = []
    for matricula in listaMatriculas:
        if matricula['IdTurma'] == idTurma:
            raaluno = matricula['RaAluno']

    for ra in raaluno:
        for aluno in listaAluno:
            if aluno['RA'] == ra:
                matriculados.append(aluno['Nome'])

    if matriculados:
        return matriculados
    else:
        return None


# 10
def pegarStats(idTurma, raAluno, listaResultados):
    for resultado in listaResultados:
        if resultado['IdTurma'] == idTurma and resultado['RaAluno'] == raAluno:
            return resultado['Nota'], resultado['Frequencia']
