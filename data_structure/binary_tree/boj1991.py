import sys


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node].left)
        preorder(tree[node].right)


def inorder(node):
    if node != '.':
        inorder(tree[node].left)
        print(node, end='')
        inorder(tree[node].right)


def postorder(node):
    if node != '.':
        postorder(tree[node].left)
        postorder(tree[node].right)
        print(node, end='')


n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = sys.stdin.readline().split()
    tree[parent] = Node(left, right)


preorder("A")
print()
inorder("A")
print()
postorder("A")
