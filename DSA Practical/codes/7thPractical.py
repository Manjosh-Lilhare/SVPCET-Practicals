def dijkstra(graph, source):
    n = len(graph)
    visited = [False] * n
    distance = [float('inf')] * n
    distance[source] = 0

    for _ in range(n):
        min_dist = float('inf')
        min_node = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_node = i

        if min_node == -1:
            break

        visited[min_node] = True

        for neighbor in range(n):
            if graph[min_node][neighbor] != 0 and not visited[neighbor]:
                new_dist = distance[min_node] + graph[min_node][neighbor]
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist

    print(f"\nShortest distances from node {source}:")
    for i in range(n):
        if distance[i] == float('inf'):
            print(f"Node {i}: Unreachable")
        else:
            print(f"Node {i}: {distance[i]}")

graph = [
    # A  B  C  D  E  F  G  H  I
    [ 0, 5, 0, 0, 0, 0, 9,18, 1],  # A
    [ 5, 0, 7, 0, 0, 0, 0, 0, 0],  # B
    [ 0, 7, 0, 8,11, 0, 0, 0, 6],  # C
    [ 0, 0, 8, 0,20, 0, 0, 0, 0],  # D
    [ 0, 0,11,20, 0, 4, 0, 0, 2],  # E
    [ 0, 0, 0, 0, 4, 0, 1, 0, 0],  # F
    [ 9, 0, 0, 0, 0, 1, 0, 2, 3],  # G
    [18, 0, 0, 0, 0, 0, 2, 0, 0],  # H
    [ 1, 0, 6, 0, 2, 0, 3, 0, 0],  # I
]


def main():
    print("Graph has 9 nodes (0 to 8)")
    source = int(input("Enter the source node: "))
    dijkstra(graph, source)

if __name__ == "__main__":
    main()


