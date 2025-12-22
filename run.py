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

for i in p:
    print(search.breadth_first_graph_search(ab).path())
    print(search.breadth_first_graph_search(ab))
    print(search.depth_first_graph_search(ab).path())

    print("      ")
    print("Búsqueda de Ramificación y Acotación")

    node, gen, vis = search.branch_and_bound_search(i)

    print("Ramificación y Acotación")
    print("Generados:", gen)
    print("Visitados:", vis)
    print("Costo total:", node.path_cost)
    print("Ruta:", node.path())
    print("   ")

    print("Búsqueda de Ramificación y Acotación con subestimación")

    node2, gen2, vis2 = search.branch_and_bound_with_heuristic_search(ab)

    print("Ramificación y Acotación con subestimación")
    print("Generados:", gen)
    print("Visitados:", vis)
    print("Costo total:", node.path_cost)
    print("Ruta:", node.path())
    print("")

