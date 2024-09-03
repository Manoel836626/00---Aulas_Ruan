
import os

# Limpa a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lista de alunos
alunos = []

# Função para criar um aluno
def criar_aluno(nome, turma):
    return {"nome": nome, "turma": turma, "notas": [], "faltas": 0}

# Menu Principal
def menu_principal():
    while True:
        limpar_tela()
        print("Menu Principal")
        print("1. Cadastrar Aluno")
        print("2. Mostrar Alunos")
        print("3. Remover Aluno")
        print("4. Página do Aluno")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_aluno()
        elif escolha == '2':
            mostrar_alunos()
        elif escolha == '3':
            remover_aluno()
        elif escolha == '4':
            pagina_do_aluno()
        elif escolha == '5':
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

def cadastrar_aluno():
    limpar_tela()
    nome = input("Nome do aluno: ")
    turma = int(input("Turma: "))
    aluno = criar_aluno(nome, turma)
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")
    input("Pressione Enter para continuar...")

def mostrar_alunos():
    limpar_tela()
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for idx, aluno in enumerate(alunos):
            print(f"{idx + 1} | {aluno['nome']}")
    input("Pressione Enter para continuar...")

def remover_aluno():
    limpar_tela()
    mostrar_alunos()
    if not alunos:
        return
    idx = int(input("Digite o índice do aluno a remover: ")) - 1
    if 0 <= idx < len(alunos):
        aluno_removido = alunos.pop(idx)
        print(f"Aluno {aluno_removido['nome']} removido com sucesso!")
    else:
        print("Índice inválido.")
    input("Pressione Enter para continuar...")

def pagina_do_aluno():
    limpar_tela()
    mostrar_alunos()
    if not alunos:
        return
    idx = int(input("Digite o índice do aluno: ")) - 1
    if 0 <= idx < len(alunos):
        aluno = alunos[idx]
        while True:
            limpar_tela()
            print(f"Página do Aluno: {aluno['nome']}")
            print("1. Editar Nome")
            print("2. Editar Turma")
            print("3. Adicionar Nota")
            print("4. Adicionar Falta")
            print("5. Mostrar Média")
            print("6. Mostrar Notas")
            print("7. Mostrar Faltas")
            print("8. Voltar")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                editar_nome(aluno)
            elif escolha == '2':
                editar_turma(aluno)
            elif escolha == '3':
                adicionar_nota(aluno)
            elif escolha == '4':
                adicionar_falta(aluno)
            elif escolha == '5':
                mostrar_media(aluno)
            elif escolha == '6':
                mostrar_notas(aluno)
            elif escolha == '7':
                mostrar_faltas(aluno)
            elif escolha == '8':
                break
            else:
                print("Opção inválida!")
                input("Pressione Enter para continuar...")
    else:
        print("Índice inválido.")
        input("Pressione Enter para continuar...")

def editar_nome(aluno):
    limpar_tela()
    novo_nome = input("Novo nome: ")
    aluno['nome'] = novo_nome
    print(f"Nome alterado para {novo_nome} com sucesso!")
    input("Pressione Enter para continuar...")

def editar_turma(aluno):
    limpar_tela()
    nova_turma = int(input("Nova turma: "))
    aluno['turma'] = nova_turma
    print(f"Turma alterada para {nova_turma} com sucesso!")
    input("Pressione Enter para continuar...")

def adicionar_nota(aluno):
    limpar_tela()
    nota = float(input("Nota: "))
    aluno['notas'].append(nota)
    print(f"Nota {nota} adicionada com sucesso!")
    input("Pressione Enter para continuar...")

def adicionar_falta(aluno):
    limpar_tela()
    falta = int(input("Quantidade de faltas a adicionar: "))
    aluno['faltas'] += falta
    print(f"{falta} faltas adicionadas com sucesso!")
    input("Pressione Enter para continuar...")

def mostrar_media(aluno):
    limpar_tela()
    if not aluno['notas']:
        print("Nenhuma nota registrada.")
    else:
        media = sum(aluno['notas']) / len(aluno['notas'])
        print(f"Média do aluno {aluno['nome']}: {media:.2f}")
    input("Pressione Enter para continuar...")

def mostrar_notas(aluno):
    limpar_tela()
    if not aluno['notas']:
        print("Nenhuma nota registrada.")
    else:
        for nota in aluno['notas']:
            print(f"Nota: {nota}")
    input("Pressione Enter para continuar...")

def mostrar_faltas(aluno):
    limpar_tela()
    print(f"Faltas do aluno {aluno['nome']}: {aluno['faltas']}")
    input("Pressione Enter para continuar...")

if (name == "_main_"):
    limpar_tela()
    menu_principal()

