"""
Este módulo utiliza funções do arquivo 'functions.py' para processar e listar
informações sobre candidatos e concursos.
"""
from leitura import *
from imprimi import *

def main():
    """
    Iniciar os dicionarios e menu

    Args:
        candidatos (dict): dicionario dos candidatos com cpf de chave
        concursos (dict): dicionario dos concursos com código de chave
    """
    candidatos = {}
    ler_candidatos_do_arquivo(candidatos)
    concursos = {}
    ler_concursos_do_arquivo(concursos)

    while True:
        imprimir_menu()
        opcao = input("-->")

        match opcao:
            case "1":
                cpf = input("Digite o número do CPF do candidato: ")
                if candidatos.get(cpf) is None:
                    print("CPF ínvalido ou Não cadastrado!")
                    break
                candidato = candidatos.get(cpf)
                listar_concursos_compativeis_com_candidato(candidato, concursos)
            case "2":
                codigo_concurso = input("Digite o código do concurso: ")
                if concursos.get(codigo_concurso) is None:
                    print("Código ínvalido ou Não cadastrado!")
                    break
                concurso = concursos.get(codigo_concurso)
                listar_candidatos_compativeis_com_concurso(concurso, candidatos)
            case "3":
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
