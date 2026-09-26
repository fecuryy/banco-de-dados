"""
Atividade SQL - Tabelas TURMA e ALUNO (versao Python)
Usa o modulo sqlite3 da biblioteca padrao - nao precisa instalar nada.
So apertar o botao "Run" (ou F5) no VS Code que ja executa tudo.
"""

import sqlite3

# Conecta (cria o arquivo atividade2.db se ele nao existir)
conexao = sqlite3.connect("atividade2.db")
cursor = conexao.cursor()

# ---------------------------------------------------
# CRIA AS TABELAS (apaga antes se ja existirem)
# ---------------------------------------------------
cursor.execute("DROP TABLE IF EXISTS aluno")
cursor.execute("DROP TABLE IF EXISTS turma")

cursor.execute("""
CREATE TABLE turma (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    turno TEXT,
    sala INTEGER
)
""")

cursor.execute("""
CREATE TABLE aluno (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER,
    turma_id INTEGER,
    FOREIGN KEY (turma_id) REFERENCES turma(id)
)
""")

# ---------------------------------------------------
# POPULA TURMA (30 registros)
# ---------------------------------------------------
turmas = [
    (1,  'Banco de Dados I', 'Noite', 101),
    (2,  'Programacao Orientada a Objetos', 'Noite', 102),
    (3,  'Estrutura de Dados', 'Manha', 201),
    (4,  'Redes de Computadores', 'Manha', 202),
    (5,  'Engenharia de Software', 'Tarde', 301),
    (6,  'Sistemas Operacionais', 'Tarde', 302),
    (7,  'Calculo I', 'Manha', 103),
    (8,  'Calculo II', 'Manha', 104),
    (9,  'Algoritmos', 'Noite', 105),
    (10, 'Logica de Programacao', 'Noite', 106),
    (11, 'Arquitetura de Computadores', 'Tarde', 203),
    (12, 'Inteligencia Artificial', 'Noite', 204),
    (13, 'Compiladores', 'Manha', 205),
    (14, 'Seguranca da Informacao', 'Tarde', 303),
    (15, 'Desenvolvimento Web', 'Noite', 107),
    (16, 'Desenvolvimento Mobile', 'Noite', 108),
    (17, 'Banco de Dados II', 'Manha', 206),
    (18, 'Sistemas Distribuidos', 'Tarde', 304),
    (19, 'Estatistica', 'Manha', 109),
    (20, 'Matematica Discreta', 'Manha', 110),
    (21, 'Gerencia de Projetos', 'Tarde', 305),
    (22, 'Interface Humano-Computador', 'Noite', 111),
    (23, 'Metodologia Cientifica', 'Manha', 207),
    (24, 'Etica Profissional', 'Tarde', 306),
    (25, 'Empreendedorismo', 'Noite', 112),
    (26, 'Programacao Funcional', 'Noite', 113),
    (27, 'DevOps', 'Tarde', 307),
    (28, 'Testes de Software', 'Manha', 208),
    (29, 'Computacao em Nuvem', 'Noite', 114),
    (30, 'Trabalho de Conclusao de Curso', 'Manha', 209),
]
cursor.executemany("INSERT INTO turma (id, nome, turno, sala) VALUES (?, ?, ?, ?)", turmas)

# ---------------------------------------------------
# POPULA ALUNO (32 registros) - id = matricula
# ---------------------------------------------------
alunos = [
    (1001, 'Pedro Almeida', 20, 1),
    (1002, 'Sandro Martins', 22, 2),
    (1003, 'Ana Beatriz', 19, 1),
    (1004, 'Paulo Ricardo', 24, 3),
    (1005, 'Patricia Souza', 21, 2),
    (1006, 'Rafael Costa', 23, 4),
    (1007, 'Renata Lima', 20, 5),
    (1008, 'Carlos Eduardo', 25, 6),
    (1009, 'Camila Rocha', 19, 1),
    (1010, 'Priscila Nunes', 22, 7),
    (1011, 'Paula Fernandes', 20, 8),
    (1012, 'Lucas Pereira', 21, 9),
    (1013, 'Larissa Gomes', 23, 10),
    (1014, 'Mateus Ribeiro', 24, 11),
    (1015, 'Mariana Alves', 20, 12),
    (1016, 'Pietro Barbosa', 19, 13),
    (1017, 'Fernanda Dias', 22, 14),
    (1018, 'Gustavo Teixeira', 21, 15),
    (1019, 'Sabrina Castro', 20, 16),
    (1020, 'Vinicius Moura', 25, 17),
    (1021, 'Beatriz Cardoso', 23, 18),
    (1022, 'Diego Freitas', 22, 19),
    (1023, 'Isabela Correia', 20, 20),
    (1024, 'Samuel Vieira', 21, 21),
    (1025, 'Pamela Duarte', 19, 22),
    (1026, 'Thiago Monteiro', 24, 23),
    (1027, 'Julia Farias', 20, 24),
    (1028, 'Eduardo Pinto', 23, 25),
    (1029, 'Sophia Azevedo', 21, 26),
    (1030, 'Bruno Cavalcante', 22, 27),
    (1031, 'Amanda Xavier', 19, 28),
    (1032, 'Rodrigo Sales', 26, 29),
]
cursor.executemany("INSERT INTO aluno (id, nome, idade, turma_id) VALUES (?, ?, ?, ?)", alunos)

conexao.commit()


def mostrar(titulo, comando):
    """Executa um comando SQL e imprime o resultado formatado."""
    print(f"\n=== {titulo} ===")
    cursor.execute(comando)
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)
    print(f"({len(resultados)} linha(s))")


# ---------------------------------------------------
# 5 COMANDOS ESCOLHIDOS DA LISTA DE SQL (cheat sheet)
# ---------------------------------------------------

mostrar(
    "1) Alunos com idade acima de 21",
    "SELECT nome FROM aluno WHERE idade > 21"
)

mostrar(
    "2) Alunos cujo nome comeca com 'P'",
    "SELECT nome FROM aluno WHERE nome LIKE 'P%'"
)

mostrar(
    "3) INNER JOIN: aluno + turma correspondente",
    """
    SELECT aluno.nome, turma.nome
    FROM aluno
    INNER JOIN turma ON aluno.turma_id = turma.id
    """
)

mostrar(
    "4) LEFT JOIN: todos os alunos, mesmo sem turma",
    """
    SELECT aluno.nome, turma.nome
    FROM aluno
    LEFT JOIN turma ON aluno.turma_id = turma.id
    """
)

mostrar(
    "5) Nomes ordenados pela idade (decrescente)",
    "SELECT nome FROM aluno ORDER BY idade DESC"
)

conexao.close()
print("\nArquivo atividade2.db criado/atualizado com sucesso na pasta atual.")
