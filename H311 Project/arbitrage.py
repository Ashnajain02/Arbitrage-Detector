import math
from string import ascii_lowercase

dataset = dict()
with open("data.txt", "r") as file:
    firstLine = True
    currencies = []
    for line in file: 
        if firstLine:
            currencies = line.split()
            firstLine = False
        else:
            line = line.split()
            fromNode = line[0]
            toValues = line[1:]
            dataset[fromNode] = dict()
        
            index = 0
            for c in currencies:
                dataset[fromNode][c] = -math.log10(float(toValues[index]))
                index += 1
            
#print(dataset)

def initialize(graph, source):
    d = {}  #destination array
    p = {}  #predecessor array
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return d, p

def relax(node, neighbour, graph, d, p):
    if d[node] + graph[node][neighbour] < d[neighbour]:
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node

def find_negative_vertices(p, start):
    result = [start]
    next_node = start
    while True:
        next_node = p[next_node]
        if next_node not in result:
            result.append(next_node)
        else:
            result.append(next_node)
            result = result[result.index(next_node):]
            return result

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]: 
                relax(u, v, graph, d, p) 
    
    for u in graph:
        for v in graph[u]:
            if d[u] + graph[u][v] < d[v]:
                return find_negative_vertices(p, u)
    return None

def test():
    result = bellman_ford(dataset, 'USD')
    print("result: ", result)
    total = 0
    for i in range(len(result)-1, 0, -1):
        fromNode = result[i]
        toNode = result[i-1]
        total += dataset[fromNode][toNode]
    final = math.pow(10, -total)
    print("final: ", final)
    
if __name__ == '__main__': 
    test()