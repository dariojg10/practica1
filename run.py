# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
dn = search.GPSProblem('D', 'N', search.romania)
cl = search.GPSProblem('C', 'L', search.romania)
mo = search.GPSProblem('M', 'O', search.romania)
tg = search.GPSProblem('T', 'G', search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

print("De A a B: ")
print(search.cost_first_graph_search(ab).path())
print(search.heuristic_first_graph_search(ab).path())
print()
print("De D a N: ")
print(search.cost_first_graph_search(dn).path())
print(search.heuristic_first_graph_search(dn).path())
print()
print("De S a L: ")
print(search.cost_first_graph_search(cl).path())
print(search.heuristic_first_graph_search(cl).path())
print()
print("De M a O: ")
print(search.cost_first_graph_search(mo).path())
print(search.heuristic_first_graph_search(mo).path())
print()
print("De T a G: ")
print(search.cost_first_graph_search(tg).path())
print(search.heuristic_first_graph_search(tg).path())
print()
