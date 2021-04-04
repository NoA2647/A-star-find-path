class Node:
    def __init__(self, i=None, j=None, value=0, gCost=0, hCost=0, check=False, parent=None):
        self.i = i
        self.j = j
        self.value = value
        self.gCost = gCost
        self.hCost = hCost
        self.check = check
        self.parent = parent


cost = 1
matrix = [[Node() for i in range(10)] for j in range(10)]

with open('Map.txt', 'r') as f:
    i = 0
    for line in f.readlines():
        j = 0
        for value in line.split(','):
            matrix[i][j].value = value
            j += 1
        i += 1

neighbors = []


def calculateHCost(i, j):
    detI = abs(i - end.i)
    detJ = abs(j - end.j)
    return (detI + detJ) * cost


def up(node):
    if node.i > 0:
        nodeUp = matrix[node.i - 1][node.j]
        if nodeUp.value == 0 and not nodeUp.check:
            nodeUp.gCost = node.gCost + cost
            nodeUp.hCost = calculateHCost(nodeUp.i, nodeUp.j)
            nodeUp.parent = node
            neighbors.append(nodeUp)


def down(node):
    if node.i < 9:
        nodeDown = matrix[node.i + 1][node.j]
        if nodeDown.value == 0 and not nodeDown.check:
            nodeDown.gCost = node.gCost + cost
            nodeDown.hCost = calculateHCost(nodeDown.i, nodeDown.j)
            nodeDown.parent = node
            neighbors.append(nodeDown)


def right(node):
    if node.j < 9:
        nodeRight = matrix[node.i][node.j + 1]
        if nodeRight.value == 0 and not nodeRight.check:
            nodeRight.gCost = node.gCost + cost
            nodeRight.hCost = calculateHCost(nodeRight.i, nodeRight.j)
            nodeRight.parent = node
            neighbors.append(nodeRight)


def left(node):
    if node.j > 0:
        nodeLeft = matrix[node.i][node.j - 1]
        if nodeLeft.value == 0 and not nodeLeft.check:
            nodeLeft.gCost = node.gCost + cost
            nodeLeft.hCost = calculateHCost(nodeLeft.i, nodeLeft.j)
            nodeLeft.parent = node
            neighbors.append(nodeLeft)

