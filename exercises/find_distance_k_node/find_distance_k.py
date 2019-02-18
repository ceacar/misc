class Node():
    def __init__(self, value, left_node = None, right_node = None):
        self.left_node = left_node
        self.right_node = right_node
        self.value = value

    def set_left(self,node):
        self.left_node = node

    def set_right(self,node):
        self.right_node = node



def find_distant_k_node(root, k):

    if k == 0:
        return [root]

    res = []
    left_nodes = find_distant_k_node(root.left_node, k-1)
    right_nodes = find_distant_k_node(root.right_node, k-1)

    if left_nodes:
        res.extend(left_nodes)
    if right_nodes:
        res.extend(right_nodes)

    return res

if __name__ == '__main__':
    """
    tree like:
    5------
    |      |
    3-     8--
    | |    |  |
    2 4    7  9--
    |            |
    1            10
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node5.set_left(node3)
    node5.set_right(node8)
    node3.set_left(node2)
    node3.set_right(node4)
    node2.set_left(node1)
    node8.set_left(node7)
    node8.set_right(node9)
    node9.set_right(node10)

    for node in find_distant_k_node(node5, 2):
        print(node.value)
