#https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

#https://www.python.org/doc/essays/graphs/

graph=[
           [0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

from abhiqueue import *

def findNeigh(vertex):
    global graph
    l = graph[vertex]
    neigh = [i for i in range(len(l)) if l[i] > 0]
    return neigh

#################################################################################
source = 0
destn = 4
highCost = 500
#################################################################################
q = AbhiQueue()  #queue
visitedNodes = []
costArray= [ highCost for i in range(len(graph[0])) ] # all 500s
costArray[source] = graph[source][source] #doing it in painful way ; could have just said 0 as destn from node to node
#################################################################################
#Bootstrap 1st  node; find neighbours; costfunc
visitedNodes.append(source)
source_neigh = findNeigh(source)

# Add neighbors to queue; not in visitedList
for e in source_neigh:
    if not e in visitedNodes:
        q.enqueue(e)
    #Update cost array
    costArray[e] = graph[source][e]


#################################################################################
#while(q.isPresent(destn)):
while(q.size()):
    vertex_dequed = q.dequeue()

    #add vertex to visitedList; do not repeat
    if not vertex_dequed in visitedNodes:
        visitedNodes.append(vertex_dequed)

    #Find neigh
    neigh = findNeigh(vertex_dequed)

    #Add neighbors to queue; not in visitedList
    for e in neigh:
        if not e in visitedNodes:
            q.enqueue(e)

    #Cost function upated for all
    for e in neigh:
        #update the cost array if smaller than current
        current_cost = graph[vertex_dequed][e] + costArray[vertex_dequed]
        if current_cost <= costArray[e]:
            costArray[e] = current_cost

print(costArray)
print("Program done")