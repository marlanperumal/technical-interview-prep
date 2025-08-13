from dataclasses import dataclass
from typing import ClassVar, Deque
from collections import deque
import json


@dataclass
class Node:
    value: int | None = None
    left: "Node" | None = None
    right: "Node" | None = None
    next_id: ClassVar[int] = 0
    id: int | None = None

    def __post_init__(self):
        if self.id is None:
            self.id = Node.next_id
            Node.next_id += 1


def serialize(base_node: Node | None) -> str:
    nodes: list[dict] = []
    unvisited: Deque[Node] = deque([base_node])

    while len(unvisited) > 0:
        node = unvisited.pop()
        left_id = None
        right_id = None
        if node.left is not None:
            unvisited.append(node.left)
            left_id = node.left.id
        if node.right is not None:
            unvisited.append(node.right)
            right_id = node.right.id

        nodes.append(
            {
                "id": node.id,
                "value": node.value,
                "left_id": left_id,
                "right_id": right_id,
            }
        )
    return json.dumps(nodes)


def unserialize(stree: str) -> Node:
    tree: list[dict[str, int | None]] = json.loads(stree)
    node_dict: dict[int, Node] = {
        node["id"]: Node(id=node["id"], value=node["value"]) for node in tree
    }
    for node in tree:
        if node["left_id"] is not None:
            node_dict[node["id"]].left = node_dict[node["left_id"]]
        if node["right_id"] is not None:
            node_dict[node["id"]].right = node_dict[node["right_id"]]

    return node_dict[tree[0]["id"]]


if __name__ == "__main__":
    node_1 = Node(10)
    node_2 = Node(12)
    node_3 = Node(14, node_1, node_2)
    node_4 = Node(16, None, node_3)

    print(serialize(node_4))
    print(serialize(node_3))
    print(serialize(node_1))

    s = serialize(node_4)
    print(unserialize(s))
    print(node_4)
