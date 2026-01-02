# Search methods

import search


resultados = []

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                       , search.romania)
gz = search.GPSProblem('G', 'Z'
                       , search.romania)
nd = search.GPSProblem('N', 'D'
                       , search.romania)
mf = search.GPSProblem('M', 'F'
                       , search.romania)

p = [ab, oe, gz, nd, mf]
nombresc = ["ARAD - BUCHAREST", "ORADEA - EFORIE", "GIURGIU - ZERIND", "NEAMT - DOBRETA", "MEHADIA - FAGRAS"]
t = 0
f=0

for i in p:
    print("Amplitud" + " -> " + nombresc[t])
    node4, gen4, vis4= search.breadth_first_graph_search(i)

    print("Nodos Generados:", gen4)
    print("Nodos Visitados:", vis4)
    print("Costo total:", node4.path_cost)
    print("Ruta:", node4.path())
    print("   ")

    print("Profundidad" + " -> " + nombresc[t])

    node3, gen3, vis3 = search.depth_first_graph_search(i)

    print("Nodos Generados:", gen3)
    print("Nodos Visitados:", vis3)
    print("Costo total:", node3.path_cost)
    print("Ruta:", node3.path())
    print("   ")

    print("Búsqueda de Ramificación y Acotación" + " -> " + nombresc[t])
    node, gen, vis, exp = search.Branch_and_Bound(i)

    print("Nodos generados:", gen)
    print("Nodos visitados:", vis)
    print("Nodos expandidos:", exp)
    print("Costo total:", node.path_cost)
    print("Ruta:", node.path())
    print("   ")

    print("Búsqueda de Ramificación y Acotación con subestimación" + " -> " + nombresc[t])
    node , gen , vis, exp = search.Subestimación_Branch_and_Bound(i)

    print("Nodos generados:", gen)
    print("Nodos visitados:", vis)
    print("Nodos expandidos:", exp)
    print("Costo total:", node.path_cost)
    print("Ruta:", node.path())
    print("   ")

    t = t + 1




