SAMUEL DÍAZ GONZÁLEZ TP2

<img width="1271" height="715" alt="image" src="https://github.com/user-attachments/assets/72c37bc0-f182-474f-bfc2-d77d52bb7114" />

🔍 Estrategias de búsqueda implementadas

En esta práctica se han implementado dos estrategias de búsqueda informada sobre grafos, aplicadas al problema de navegación en el mapa de Rumanía.

🔹 Ramificación y Acotación

La búsqueda de Ramificación y Acotación explora el espacio de estados ordenando la lista de nodos abiertos según el coste acumulado desde el estado inicial hasta cada nodo. En cada iteración se selecciona el nodo con menor coste y se comprueba si es un estado objetivo. Si no lo es, el nodo se expande generando sus sucesores, que se insertan de nuevo en la lista abierta manteniendo el orden por coste.

Esta estrategia garantiza encontrar el camino de coste mínimo siempre que los costes de las aristas sean no negativos. No utiliza información heurística, por lo que puede generar y visitar un número elevado de nodos.

🔹 Ramificación y Acotación con Subestimación

La búsqueda de Ramificación y Acotación con Subestimación extiende la estrategia anterior incorporando una función heurística admisible, que estima el coste restante hasta el objetivo. En este caso, se utiliza la distancia euclídea entre ciudades. La lista de nodos abiertos se ordena según la suma del coste acumulado y la heurística (g + h).

Gracias al uso de la heurística, esta estrategia reduce el número de nodos generados y visitados, manteniendo la optimalidad de la solución. El camino obtenido es el mismo que el de Ramificación y Acotación, pero con un rendimiento superior.

📌 Comparación

Ambas estrategias garantizan la obtención del camino óptimo.

La versión con subestimación es más eficiente, ya que explora menos nodos.
