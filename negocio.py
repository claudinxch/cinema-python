from dados import *

contador_sessao = 1

def criar_filme(nome, duracao):
    if not nome or not duracao:
        return "Dados inválidos"

    if buscar_filme(nome):
        return "Filme já cadastrado"

    filme = {
        "nome": nome,
        "duracao": duracao
    }

    adicionar_filme(filme)
    return "Filme cadastrado com sucesso"


def criar_sessao(nome_filme, horario, capacidade):
    global contador_sessao

    filme = buscar_filme(nome_filme)
    if not filme:
        return "Filme não encontrado"

    sessao = {
        "id": contador_sessao,
        "filme": nome_filme,
        "horario": horario,
        "capacidade": capacidade,
        "reservas": 0
    }

    adicionar_sessao(sessao)
    contador_sessao += 1

    return f"Sessão criada com ID {sessao['id']}"


def reservar_assento(id_sessao):
    sessao = buscar_sessao(id_sessao)

    if not sessao:
        return "Sessão não encontrada"

    if sessao["reservas"] >= sessao["capacidade"]:
        return "Sessão lotada"

    sessao["reservas"] += 1
    return "Reserva realizada com sucesso"


def listar_sessoes_formatado():
    sessoes = listar_sessoes()

    if not sessoes:
        return ["Nenhuma sessão cadastrada"]

    resultado = []
    for s in sessoes:
        resultado.append(
            f"ID: {s['id']} | Filme: {s['filme']} | Horário: {s['horario']} | "
            f"Vagas: {s['capacidade'] - s['reservas']}"
        )

    return resultado