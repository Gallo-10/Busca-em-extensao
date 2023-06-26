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

def dfs(grafo, origem,destino, visitado=None, caminho=None):
  if visitado is None:
    visitado = set()
  if caminho is None:
    caminho = []

  visitado.add(origem)
  caminho.append(origem)

  if origem ==  destino:
    return caminho
  
  for vizinho in grafo[origem]:
    if vizinho not in visitado:
      novo_caminho = dfs(grafo, vizinho, destino, visitado, caminho.copy())
      if novo_caminho is not None: 
        return novo_caminho

  return None


caminho = dfs(grafo,'Iasi', 'Pitesti')

if caminho is not None: 
    print("Menor caminho encontrado:", ' -> '.join(caminho))
else:
    print("Caminho não encontrado.")
 
