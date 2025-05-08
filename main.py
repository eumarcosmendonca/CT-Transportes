import heapq
import osmnx as ox
import networkx as nx

# 1. Defina a cidade e pontos turísticos
cidade = "Maceió, Brasil"
lugares = [
    "Teatro Gustavo Leite, Maceió, Brasil",
    "Praia de Ponta Verde, Maceió, Brasil",
    "Mirante São Gonçalo, Maceió, Brasil",
    "Praia do Francês, Marechal Deodoro, Brasil"
]

# 2. Geocodifica os locais
coordenadas = [ox.geocode(lugar) for lugar in lugares]

# 3. Baixa o grafo da cidade
grafo = ox.graph_from_place(cidade, network_type='walk')

# 4. Encontra os nós mais próximos no grafo
nos = [ox.distance.nearest_nodes(grafo, lon, lat) for lat, lon in coordenadas]

# 5. Função Dijkstra que retorna distâncias a partir de um nó
def dijkstra(grafo, origem):
    distancia = {n: float('inf') for n in grafo.nodes}
    distancia[origem] = 0
    visitado = set()
    fila = [(0, origem)]

    while fila:
        dist_atual, atual = heapq.heappop(fila)
        if atual in visitado:
            continue
        visitado.add(atual)

        for vizinho in grafo.neighbors(atual):
            peso = grafo[atual][vizinho][0].get('length', 1)
            if distancia[vizinho] > dist_atual + peso:
                distancia[vizinho] = dist_atual + peso
                heapq.heappush(fila, (distancia[vizinho], vizinho))

    return distancia

# 6. Gera o roteiro otimizando os próximos destinos com base na menor distância
visitados = [0]  # Começa pelo primeiro lugar
roteiro = [lugares[0]]  # Lista com a ordem do passeio
total_distancia = 0

while len(visitados) < len(lugares):
    atual = visitados[-1]
    distancias = dijkstra(grafo, nos[atual])

    # Encontra o próximo ponto mais próximo que ainda não foi visitado
    menor_dist = float('inf')
    proximo = None
    for i in range(len(lugares)):
        if i not in visitados:
            if distancias[nos[i]] < menor_dist:
                menor_dist = distancias[nos[i]]
                proximo = i

    visitados.append(proximo)
    roteiro.append(lugares[proximo])
    total_distancia += menor_dist
    print(f"De '{lugares[atual]}' até '{lugares[proximo]}': {menor_dist/1000:.2f} km")

print("\nRoteiro final:")
for lugar in roteiro:
    print("-", lugar)

print(f"\nDistância total percorrida: {total_distancia/1000:.2f} km")
