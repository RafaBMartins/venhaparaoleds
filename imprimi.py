"""
Módulo para interação com menus e listagem de dados relacionados a candidatos e concursos.

Este módulo fornece funcionalidades para:
1. Exibir um menu interativo para o usuário.
2. Listar concursos compatíveis com o perfil de um candidato.
3. Listar candidatos compatíveis com as vagas de um concurso.
"""
def imprimir_menu():
    """
    Exibe o menu de opções para o usuário interagir com o programa.

    O menu oferece as seguintes opções:
    1. Buscar Concursos Por Candidato
    2. Buscar Candidatos Por Concurso
    3. Encerrar o Programa

    O usuário deve escolher uma opção digitando o número correspondente.
    """
    print("----------------------------------")
    print("1. Buscar Concursos Por Candidato")
    print("2. Buscar Candidatos Por Concurso")
    print("3. Encerrar Progama")
    print("Digite o Número da Opção Desejada")
    print("----------------------------------")

def listar_concursos_compativeis_com_candidato(candidato, concursos):
    """
    Exibe os concursos que se encaixam no perfil de um candidato.

    A função compara as profissões do candidato com as vagas dos concursos e exibe os concursos
    que possuem alguma profissão compatível com o perfil do candidato.

    Args:
        candidato (list): [nome, data_de_nascimento, [profissoes]].
        concursos (dict): concursos[codigo] = {orgao, edital, [vagas]}.
    """
    flag = True
    print("Concursos que se encaixam no perfil do candidato:")
    for codigo in concursos:
        if set(candidato[2]) & set(concursos.get(codigo)[2]):
            orgao = concursos.get(codigo)[0]
            edital = concursos.get(codigo)[1]
            print(f"Orgão: {orgao} | Código: {codigo} | Edital: {edital}")
            flag = False
    if flag:
        print("Não foi encontrado nenhum concurso que se encaixe no perfil!")

def listar_candidatos_compativeis_com_concurso(concurso, candidatos):
    """
    Exibe os candidatos que se encaixam nas vagas de um concurso.

    A função compara as profissões exigidas no concurso com as profissões dos candidatos
    e exibe os candidatos cujas profissões coincidem com as vagas do concurso.

    Args:
        concurso (list): [orgao, edital, [vagas]].
        candidatos (dict): candidatos[cpf] = {nome, data_de_nascimento, [profissoes]}
    """
    flag = True
    print("Candidatos que se encaixam nas vagas do concurso:")
    for cpf in candidatos:
        if set(concurso[2]) & set(candidatos.get(cpf)[2]):
            nome = candidatos.get(cpf)[0]
            data_nascimento = candidatos.get(cpf)[1]
            print(f"Nome: {nome} | CPF: {cpf} | Data: {data_nascimento}")
            flag = False
    if flag:
        print("Não foi encontrado nenhum candidato que se encaixe nas vagas do concurso!")
