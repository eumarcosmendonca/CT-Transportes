🗺️ Roteiro Turístico Otimizado - Maceió/AL
Este projeto utiliza dados do OpenStreetMap para gerar um roteiro turístico otimizado pela cidade de Maceió (AL), considerando os caminhos reais disponíveis para pedestres. A partir de uma lista de pontos turísticos, o algoritmo calcula o trajeto mais curto entre eles usando Dijkstra, respeitando a malha viária da cidade.

🚀 Funcionalidades
Geocodificação de locais turísticos.

Download do grafo de ruas para pedestres.

Cálculo de distâncias reais entre pontos usando o algoritmo de Dijkstra.

Geração de um roteiro otimizado para caminhar pelos locais definidos.

Exibição da distância entre os pontos e da distância total do percurso.

🧰 Tecnologias Utilizadas
Python 3

OSMnx – para acesso e manipulação de dados do OpenStreetMap

NetworkX – para criação e análise de grafos

heapq – para a implementação da fila de prioridade no Dijkstra

📌 Pré-requisitos
Instale os pacotes necessários com:

bash
Copiar
Editar
pip install osmnx networkx
▶️ Como Executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Execute o script:

bash
Copiar
Editar
python roteiro_turistico.py
O script imprimirá no terminal:

A sequência de locais a serem visitados.

As distâncias entre cada ponto.

A distância total percorrida no roteiro.

🗒️ Exemplo de Saída
rust
Copiar
Editar
De 'Teatro Gustavo Leite' até 'Praia de Ponta Verde': 2.34 km
De 'Praia de Ponta Verde' até 'Mirante São Gonçalo': 3.21 km
De 'Mirante São Gonçalo' até 'Praia do Francês': 22.19 km

Roteiro final:
- Teatro Gustavo Leite
- Praia de Ponta Verde
- Mirante São Gonçalo
- Praia do Francês

Distância total percorrida: 27.74 km
📍 Pontos de Interesse
Os pontos turísticos usados como exemplo são:

Teatro Gustavo Leite

Praia de Ponta Verde

Mirante São Gonçalo

Praia do Francês (Marechal Deodoro)

Você pode personalizar essa lista facilmente no início do script.

📄 Licença
Este projeto está licenciado sob a MIT License.
