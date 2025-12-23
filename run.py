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
def formato(gen, vis, ruta, coste):
    return (
        f"G: {gen}\n"
        f"V: {vis}\n"
        f"Ruta: {ruta}\n"
        f"Coste: {coste}"
    )
for i in p:
    print("Amplitud" + " -> " + nombresc[t])
    node4, gen4, vis4, cost4 = search.breadth_first_graph_search(i)

    print("Generados:", gen4)
    print("Visitados:", vis4)
    print("Costo total:", cost4)
    print("Ruta:", node4.path())
    print("   ")

    print("Profundidad" + " -> " + nombresc[t])
    node0, gen0, vis0, cost0 = search.depth_first_graph_search(i)

    print("Generados:", gen0)
    print("Visitados:", vis0)
    print("Costo total:", cost0)
    print("Ruta:", node0.path())
    print("   ")

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

    # -------- GUARDAR RESULTADOS PARA LA TABLA --------
    resultados.append({
        "ID": t + 1,
        "Origen": nombresc[t].split(" - ")[0],
        "Destino": nombresc[t].split(" - ")[1],
        "Amplitud": formato(gen4, vis4, node4.path(), cost4),
        "Profundidad": formato(gen0, vis0, node0.path(), cost0),
        "R&A": formato(gen, vis, node.path(), node.path_cost),
        "R&A + h": formato(gen2, vis2, node2.path(), node2.path_cost)
    })

    t = t + 1


print("\n-------------------------------------------------------------------------------------------------------------------------------------------------")

columnas = ["ID", "Origen", "Destino", "Amplitud", "Profundidad", "R&A", "R&A + h"]
anchos = [3, 10, 12, 25, 25, 25, 25]

# Cabecera
for col, ancho in zip(columnas, anchos):
    print(f"{col:<{ancho}}", end=" | ")
print()
print("-" * (sum(anchos) + 3 * len(anchos)))

# Filas
for r in resultados:
    filas = []
    max_lineas = 1

    for col in columnas:
        lineas = str(r[col]).split("\n")
        filas.append(lineas)
        max_lineas = max(max_lineas, len(lineas))

    for i in range(max_lineas):
        for contenido, ancho in zip(filas, anchos):
            texto = contenido[i] if i < len(contenido) else ""
            print(f"{texto:<{ancho}}", end=" | ")
        print()
    print("-" * (sum(anchos) + 3 * len(anchos)))



