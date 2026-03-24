filmes = []
sessoes = []

def adicionar_filme(filme):
    filmes.append(filme)

def listar_filmes():
    return filmes

def buscar_filme(nome):
    for f in filmes:
        if f["nome"].lower() == nome.lower():
            return f
    return None


def adicionar_sessao(sessao):
    sessoes.append(sessao)

def listar_sessoes():
    return sessoes

def buscar_sessao(id_sessao):
    for s in sessoes:
        if s["id"] == id_sessao:
            return s
    return None