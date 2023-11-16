import heapq

def dijkstra(gph, st, dis, prev_edge):
    pri_queue = [(0, st)]
    while pri_queue:
        cur_dist, cur_node = heapq.heappop(pri_queue)
        if cur_dist > dis[cur_node]:
            continue
        for neighbor in gph[cur_node]:
            dist = cur_dist + gph[cur_node][neighbor]
            if dist < dis[neighbor]:
                dis[neighbor] = dist
                prev_edge[neighbor] = cur_node
                heapq.heappush(pri_queue, (dist, neighbor))

def create_routing_table(gph, st):
    dis = {node: float('infinity') for node in gph}
    dis[st] = 0
    prev_node = {node: None for node in gph}
    dijkstra(gph, st, dis, prev_node)
    route_table = {}
    for node in gph:
        path = []
        cur_node = node
        while cur_node is not None:
            path.insert(0, cur_node)
            cur_node = prev_node[cur_node]
        route_table[node] = {'path': path, 'cost': dis[node]}
    return route_table

# Example usage:
network = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
routing_table = create_routing_table(network, start_node)
for node, data in routing_table.items():
    print(f"Optimal path from {start_node} to {node}: {data['path']}, Cost: {data['cost']}")
