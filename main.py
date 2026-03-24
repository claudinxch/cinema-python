from negocio import *

def menu():
    while True:
        print("\n🎬 MENU CINEMA")
        print("1 - Cadastrar filme")
        print("2 - Criar sessão")
        print("3 - Listar sessões")
        print("4 - Reservar assento")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome do filme: ")
            duracao = input("Duração (min): ")
            print(criar_filme(nome, duracao))

        elif op == "2":
            nome = input("Filme: ")
            horario = input("Horário (ex: 20:00): ")
            capacidade = int(input("Capacidade: "))
            print(criar_sessao(nome, horario, capacidade))

        elif op == "3":
            for s in listar_sessoes_formatado():
                print(s)

        elif op == "4":
            try:
                id_sessao = int(input("ID da sessão: "))
                print(reservar_assento(id_sessao))
            except:
                print("ID inválido")

        elif op == "0":
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()