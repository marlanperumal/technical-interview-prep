from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Optional[TreeNode]) -> str:
    """Convert a binary tree to a string representation."""
    vals = []

    def dfs(node):
        if node is None:
            vals.append("null")
            return
        vals.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(vals)


def deserialize(data: str) -> Optional[TreeNode]:
    """Rebuild a binary tree from a string representation."""
    vals = iter(data.split(","))

    def dfs():
        val = next(vals)
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


# --- Example usage ---
if __name__ == "__main__":
    # Construct example tree:
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

    s = serialize(tree)
    print("Serialized:", s)  # e.g., "1,2,null,null,3,4,null,null,5,null,null"

    t2 = deserialize(s)
    print("Re-serialized:", serialize(t2))  # Should match original
