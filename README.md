# Djikstra Shortest Path - US Road Network

Python implementation of Dijkstra’s Shortest Path Algorithm to compute the shortest route between two locations in a large US road network dataset.

The program parses road and place datasets, constructs a graph, and calculates the shortest path between two nodes using a priority queue.

Features
- Implements Dijkstra's algorithm
- Uses binary heap priority queue (heapq)
- Processes a large road network dataset
- Outputs step-by-step route with distance between locations
- Calculates total travel distance and runtime

Technologies
- Python
- Data Structures
- Graph Algorithms
- Priority Queues (heapq)

Dataset

Two files are used to construct the graph:

Place.txt
Maps place IDs to place names.

Road.txt
Represents road segments between locations.

Each line contains:
placeID1, placeID2, distance, road description

These files are parsed to create an undirected graph where each node stores a list of connected edges.

Algorithm

The graph is stored as a Python dictionary where:

graph[node] = list of Edge objects

Each edge contains:
- destination node
- distance
- road description

Dijkstra’s algorithm maintains:
- dist_table → best known distance to each node
- prev → previous node in the shortest path
- priority_queue → nodes prioritized by smallest distance

Worst case time complexity:

O((V + E) log V)

Where:
V = number of places
E = number of roads

How to Run

Clone the repository:

git clone https://github.com/yourusername/dijkstra-road-network

Run the program:

python roadmap_dijkstra.py

Enter source and destination names when prompted.

Example:

Enter the Source Name :
MIKALAMAZOO N

Enter the Destination Name :
MIANN ARBOR N

