import sys

class Node:
    left = None
    right = None
    left_cost = 0
    right_cost = 0
    def __init__(self, name='',left=None,right=None,left_cost=sys.maxsize,right_cost=sys.maxsize):
        self.left=left
        self.right=right
        self.left_cost = left_cost
        self.name = name
        self.right_cost = right_cost

def find_shortest_path(root, path, target):
    import pdb
    # pdb.set_trace()
    #base case
    if root == target:
        path.append(root.name)
        return path, 0
    if not root.left and not root.right:
        return path, sys.maxsize

    print(root.name,path)
    cost1 = sys.maxsize
    cost2 = sys.maxsize
    cost = sys.maxsize

    path.append(root.name)
    #main recursive
    if root.left:
        path1,cost1 = find_shortest_path(root.left,path,target)
        cost1 += root.left_cost

    if root.right:
        path2,cost2 = find_shortest_path(root.right,path,target)
        cost2+=root.right_cost


    if cost1 and cost2<cost1:
        cost = cost2
    elif cost2 and cost2>cost1:
        cost = cost1

    return path, cost

def run_shortest_path(root,target):
    path = []
    path,cost=find_shortest_path(root, path,target)
    return path,cost


if __name__=='__main__':
    node5=Node(name='node5')
    node3=Node(name='node3')
    node4=Node(name='node4',left=node5, left_cost=1)
    node2=Node(name = 'node2', left=node4,left_cost=3)
    node1=Node(name = 'node1', left=node2,right=node3, left_cost=2)
    cost,path = run_shortest_path(node1,node5)
    print('cost',cost,'path',path)

    print('now short_circut 2->5')
    node2.left=node5
    node2.left_cost=1
    cost,path = run_shortest_path(node1,node5)
    print('cost',cost,'path',path)



