# Search methods

import search

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

for i in p:
    print("Amplitud" + " -> " + nombresc[t])
    node4, gen4, vis4, cost4 = search.breadth_first_graph_search(i)


    print("Generados:", gen4)
    print("Visitados:", vis4)
    print("Costo total:", cost4)
    print("Ruta:", node4.path())
    print("   ")

    print("      ")

    print("Profundidad" + " -> " + nombresc[t])
    node0, gen0, vis0, cost0 = search.depth_first_graph_search(i)


    print("Generados:", gen0)
    print("Visitados:", vis0)
    print("Costo total:", cost0)
    print("Ruta:", node0.path())
    print("   ")

    print("      ")

    print("Búsqueda de Ramificación y Acotación" + " -> " + nombresc[t])

    node, gen, vis = search.branch_and_bound_search(i)


    print("Generados:", gen)
    print("Visitados:", vis)
    print("Costo total:", node.path_cost)
    print("Ruta:", node.path())
    print("   ")

    print("Búsqueda de Ramificación y Acotación con subestimación" + " -> " + nombresc[t])

    node2, gen2, vis2 = search.branch_and_bound_with_heuristic_search(i)


    print("Generados:", gen2)
    print("Visitados:", vis2)
    print("Costo total:", node2.path_cost)
    print("Ruta:", node2.path())
    print("")

    t = t+1
