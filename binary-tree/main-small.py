from dataclasses import dataclass
from typing import Self, Deque
from collections import deque


@dataclass
class Node:
    value: int | None = None
    left: Self | None = None
    right: Self | None = None


def serialize(base_node: Node) -> str:
    output: list[int] = []

    def dfs(node: Node | None):
        if node is None:
            output.append(None)
            return

        output.append(node.value)
        dfs(node.left)
        dfs(node.right)

    dfs(base_node)
    return ",".join([str(i) for i in output])


def unserialize(s: str) -> Node:
    queue: Deque[int | None] = deque(
        [int(i) if i != "None" else None for i in s.split(",")]
    )

    def dfs() -> Node:
        value = queue.popleft()
        if value is None:
            return

        left = dfs()
        right = dfs()
        return Node(value, left, right)

    return dfs()


if __name__ == "__main__":
    node_1 = Node(10)
    node_2 = Node(12)
    node_3 = Node(14, node_1, node_2)
    node_4 = Node(16, None, node_3)

    print(serialize(node_4))
    print(serialize(node_3))
    print(serialize(node_1))

    s = serialize(node_4)
    print(s)

    n = unserialize(s)
    print(serialize(n))
    print(node_4)
    print(n)
