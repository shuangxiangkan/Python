graph={}
graph["start"]={}
graph["start"]["a"]=6
graph["start"]["b"]=2
graph["a"]={}
graph["a"]["fin"]=1
graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5
graph["fin"]={}


infinity=float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity

parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None

searched = []
# return the node in costs with lowest cost
def find_lowest_cost_node():
    lowest_cost=infinity
    lowest_cost_node=None
    for node in costs:
        if node not in searched and costs[node]<lowest_cost:
            lowest_cost_node=node
            lowest_cost=costs[node]

    return lowest_cost_node



def dijkstra_algorithm():
    # add the "start" node to searches list
    searched.append("start")
    # find the lowest cost node in costs
    node = find_lowest_cost_node()
    # print(graph[node].keys())
    while node is not None:
        searched.append(node)
        # all of nodes adjacent to the node
        neighbors=graph[node].keys()
        # go through all the neighbors of this node
        for neighbor in neighbors:
            new_cost = costs[node] + graph[node][neighbor]
            if costs[neighbor]>new_cost:
                # update cost
                costs[neighbor]=new_cost
                # set the node as the new parent of the neighbor
                parents[neighbor]=node

        node=find_lowest_cost_node()

dijkstra_algorithm()
print(costs)