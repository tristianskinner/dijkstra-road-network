import heapq
import time

# Make an edge Class to describe a road
class Edge:
    def __init__(self, to, length, desc):
        self.to = to
        self.length = length
        self.desc = desc

#File places *Must have in same folder*
def places(filename):
    id_to_name = {}
    name_to_id = {}

    with open(filename, "r") as f: 
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",", 1)
            if len(parts) != 2:
                continue
            place_id_str, name = parts
            place_id = int(place_id_str)

            if name != "":
                id_to_name[place_id] = name
            if name:
                name_to_id[name] = place_id

    return id_to_name, name_to_id

#File Roads *Same as above* this is where we will turn our roads into edges on a graph
def roads(filename):
    graph = {} #Create  dict of edges

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",", 3)
            if len(parts) < 3:
                continue

            a_str, b_str, dist_str = parts[:3]
            if len(parts) == 4: 
                desc = parts[3]
            else:
                desc = ""

            a = int(a_str)
            b = int(b_str)
            dist = float(dist_str)

            edge_a = Edge(b, dist, desc)
            edge_b = Edge(a, dist, desc)
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            #Add Edges of both ways to graph since undirected
            graph[a].append(edge_a)
            graph[b].append(edge_b)

    return graph

#Dijkstra Algorithm, Can find a lot of python implementation online for this algo
def dijkstra(graph, source, destination):
    dist_table = {source: 0.0}
    prev = {} #node will hold prev node and edge used
    priority_queue = [(0.0, source)] #distance, node

    while priority_queue:
        dist, current_node = heapq.heappop(priority_queue)

        if current_node == destination:
            return dist, prev

        for edge in graph[current_node]:
            neighbor = edge.to
            new_dist = dist + edge.length
            if new_dist < dist_table.get(neighbor, float("inf")):
                dist_table[neighbor] = new_dist
                prev[neighbor] = (current_node, edge)
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return None, prev

def reconstruct(prev, source, destination):
    path = []
    if destination not in prev and source != destination:
        #There's no path
        return []
    
    curr = destination
    while curr != source:
        prev_node, edge = prev[curr]
        path.append((prev_node, curr, edge.length, edge.desc))
        curr = prev_node

    return list(reversed(path)) #reverse list because of how it is added to see the sequential steps

def place_name_format(place_id, id_to_name):
    name = id_to_name.get(place_id)
    if not name:
        return f"{place_id}(null)"
    return f"{place_id}({name})"

def main():
    start = time.time()
    
    id_to_name, name_to_id = places("Place.txt")
    graph = roads("Road.txt")

    src_name = input("Enter the Source Name : \n").strip()
    dest_name = input("Enter the Destination Name : \n").strip()

    src = name_to_id.get(src_name)
    dest = name_to_id.get(dest_name)

    if src is None or dest is None:
        print("Try again.")
        return
    
    print(f"\nSearching from {place_name_format(src, id_to_name)} to {place_name_format(dest, id_to_name)}\n")

    total, prev = dijkstra(graph, src, dest)

    if total is None:
        print("No Route Found.")
        return
    
    path = reconstruct(prev, src, dest)

    for i, (current_node, neighbor, dist, desc) in enumerate(path, start=1):
        print(f"\t{i}: {place_name_format(current_node, id_to_name)} -> {place_name_format(neighbor, id_to_name)}, {desc}, {dist:.2f} mi.")

    print(f"\nIt takes {total:.2f} miles from {place_name_format(src, id_to_name)} to {place_name_format(dest, id_to_name)}.")
    end = time.time()
    print("Total runtime: ", end - start, "seconds")

if __name__ == "__main__":
    main()
    
         