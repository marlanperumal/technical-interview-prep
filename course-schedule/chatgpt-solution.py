from collections import defaultdict, deque


def can_finish_bfs(numCourses, prerequisites):
    # Build adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    # Initialize queue with courses that have zero prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    processed = 0

    while queue:
        course = queue.popleft()
        processed += 1

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we processed all courses, no cycle exists
    return processed == numCourses
