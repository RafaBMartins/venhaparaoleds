"""
Módulo para leitura e processamento de dados de candidatos e concursos a partir de arquivos.

Este módulo contém funções que leem os dados dos arquivos `candidatos.txt` e `concursos.txt`, 
processam as informações usando expressões regulares, e armazenam os dados em dicionários.

Arquivos esperados:
1. `candidatos.txt`:
    - Formato de cada linha:
      Nome Sobrenome DD/MM/AAAA CPF [profissao1, profissao2, ...]
    - Exemplo:
      João Silva 15/08/1990 12345678901 [Engenheiro, Professor]

2. `concursos.txt`:
    - Formato de cada linha:
      Órgão Edital Código [vagas1, vagas2, ...]
    - Exemplo:
      Prefeitura 01/2024 12345 [Engenheiro, Médico, Professor]

Dependências:
- `re` (módulo para trabalhar com expressões regulares).
"""
import re

def ler_candidatos_do_arquivo(candidatos):
    """
    Lê os dados dos candidatos a partir do arquivo 'candidatos.txt' e os armazena em um dicionário.

    O arquivo 'candidatos.txt' deve seguir o formato:
    Nome Sobrenome DD/MM/AAAA CPF [profissao1, profissao2, ...]

    Cada linha é processada com uma expressão regular para extrair:
    - Nome do candidato
    - Data de nascimento
    - CPF
    - Lista de profissões

    Os dados são armazenados no dicionário 'candidatos' e o valor é uma lista contendo:
    - Nome (str)
    - Data de nascimento (str)
    - Lista de profissões (lista de str)

    Args:
        candidatos (dict): Dicionário vazio para ser preenchido, usando o CPF como chave.
    """
    with open("candidatos.txt", "r", encoding="utf-8") as candidatos_file:
        for linha in candidatos_file:
            linha = linha.strip()
            regex = re.compile(r"""
            ^
            (?P<nome>[A-Za-z\s']+)
            \s
            (?P<data>\d{2}/\d{2}/\d{4})
            \s
            (?P<cpf>\d{3}\.\d{3}\.\d{3}-\d{2})
            \s
            \[(?P<profissoes>.+)\]
            $
            """, re.VERBOSE)
            candidato = re.match(regex, linha)
            cpf = candidato.group("cpf").replace(".","").replace("-","")
            profissoes = candidato.group("profissoes").split(", ")
            nome = candidato.group("nome")
            data_nascimento = candidato.group("data")
            candidatos[cpf] = [nome,data_nascimento,profissoes]

def ler_concursos_do_arquivo(concursos):
    """
    Lê os dados dos concursos a partir do arquivo 'concursos.txt' e os armazena em um dicionário.

    O arquivo 'concursos.txt' deve seguir o formato:
    Órgão Edital Código [vagas1, vagas2, ...]

    Cada linha é processada com uma expressão regular para extrair:
    - Órgão (identificação do órgão)
    - Edital (número e data no formato DD/YYYY)
    - Código (código único do concurso)
    - Lista de vagas (vagas separadas por vírgulas dentro de colchetes)

    Os dados extraídos são armazenados no dicionário 'concursos' e o valor é uma lista contendo:
    - Órgão (str)
    - Edital (str)
    - Lista de vagas (list de str)

    Args:
        concursos (dict): Dicionário vazio para ser preenchido, usando o código como chave.
    """
    with open("concursos.txt", "r", encoding="utf-8") as concursos_file:
        for linha in concursos_file:
            linha = linha.strip()
            regex = re.compile(r"""
            ^
            (?P<orgao>\w+)
            \s
            (?P<edital>\d{1,2}/\d{4})
            \s
            (?P<codigo>\d+)
            \s
            \[(?P<vagas>.+)\]
            $
            """, re.VERBOSE)
            concurso = re.match(regex, linha)
            codigo = concurso.group("codigo")
            orgao = concurso.group("orgao")
            edital = concurso.group("edital")
            vagas = concurso.group("vagas").split(", ")
            concursos[codigo] = [orgao,edital,vagas]
