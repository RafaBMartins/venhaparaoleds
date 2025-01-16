# Documentação de Solução para o Sistema de Busca de Concursos e Candidatos

## Visão Geral
O sistema permite a interação entre candidatos e concursos públicos a partir de informações armazenadas em arquivos de texto. Através de um menu no terminal, o usuário pode:
- Buscar concursos compatíveis com o perfil de um candidato, usando o CPF do candidato.
- Buscar candidatos compatíveis com as vagas de um concurso, usando o código do concurso.

## Arquivos de Entrada
O sistema utiliza dois arquivos de texto para armazenar as informações necessárias:

1. **`candidatos.txt`**:
   - Formato: `Nome Sobrenome DD/MM/AAAA CPF [profissao1, profissao2, ...]`.

2. **`concursos.txt`**:
   - Formato: `Órgão Edital Código [vagas1, vagas2, ...]`.

## Funcionamento do Sistema

### 1. Leitura e Processamento dos Dados
O sistema utiliza expressões regulares para processar os arquivos `candidatos.txt` e `concursos.txt`. A função `ler_candidatos_do_arquivo` lê as informações dos candidatos e as armazena em um dicionário, usando o CPF como chave. A função `ler_concursos_do_arquivo` realiza a leitura dos dados dos concursos e os armazena em um dicionário, usando o código do concurso como chave.

### 2. Menu Interativo
O usuário interage com o programa através de um menu de opções:
- **Opção 1**: Buscar Concursos por Candidato.
- **Opção 2**: Buscar Candidatos por Concurso.
- **Opção 3**: Encerrar o Programa.

Dependendo da escolha, o sistema solicita a entrada de dados do usuário (CPF ou código do concurso) e exibe os resultados diretamente no terminal.

### 3. Busca de Concursos Compatíveis com o Candidato
Ao selecionar a opção 1, o programa solicita o CPF do candidato e exibe os concursos cujo perfil de vagas (profissões) seja compatível com as profissões do candidato.

### 4. Busca de Candidatos Compatíveis com o Concurso
Ao selecionar a opção 2, o programa solicita o código do concurso e exibe os candidatos cujo perfil de profissões seja compatível com as vagas do concurso.

## Conclusão

O sistema é uma solução eficiente e simples para realizar buscas entre candidatos e concursos públicos. Ele utiliza arquivos de texto como fonte de dados e apresenta um menu interativo no terminal para facilitar a interação do usuário.