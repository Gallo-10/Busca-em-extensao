grafo = {
    'Oradea': ['Zerind', 'Sibiu'],
    'Zerind': ['Oradea', 'Arad'],
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Sibiu': ['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}


def busca(grafo, inicio, objetivo):

    # define a fila de busca
    fila_busca = [inicio]

    # define os nós visitados e passa inicio como a primeira posição já que a cidade de inicio é a cidade de origem
    visitados = [inicio]

    # define o caminho a percorrer
    vizinhos = {}

    # enquanto a fila não estiver vazia
    while fila_busca:

        # remove sempre a primeira posição da fila
        no = fila_busca.pop(0)

        # se o no em que a fila se encontra for o objetivo, caminho o recebe e adiciona ao array
        if no == objetivo:
            caminho = [objetivo]

            while objetivo != inicio:  # enquanto objetivo não for o unico elemento restante na fila
                caminho.insert(0, vizinhos[objetivo])
                objetivo = vizinhos[objetivo]
            return caminho

        #verifica todos as cidades vizinhas no grafo
        for vizinho in grafo[no]:
            #caso a ciadde não tenha sido vizitada ela é adicionada a fila para que seja visitada
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila_busca.append(vizinho)
                vizinhos[vizinho] = no
    return False


print("Qual a cidade de partida? : ")
partida = input()
print("Qual a cidade de destino? : ")
destino = input()

if busca(grafo, partida, destino) == False:
    print("Caminho não encontrado, ou cidade escrita incorretamente!")
else:
    print("Caminho: ", busca(grafo, partida, destino))
