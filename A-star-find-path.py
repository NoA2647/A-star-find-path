from colorama import Fore


class Node:
    def __init__(self, i=0, j=0, value=0, gCost=0, hCost=0, check=False, parent=None):
        self.i = i
        self.j = j
        self.value = value
        self.gCost = gCost
        self.hCost = hCost
        self.check = check
        self.parent = parent


cost = 1
matrix = [[Node() for i in range(10)] for j in range(10)]
neighbors = []


def readMap():
    with open('Map.txt', 'r') as f:
        i = 0
        for line in f.readlines():
            j = 0
            for value in line.split(','):
                matrix[i][j].value = int(value)
                matrix[i][j].i = i
                matrix[i][j].j = j
                j += 1
            i += 1


def calculateHCost(i, j, nodeEnd):
    detI = abs(int(i) - int(nodeEnd.i))
    detJ = abs(int(j) - int(nodeEnd.j))
    return (detI + detJ) * cost


def up(node, nodeEnd):
    if node.i > 0:
        nodeUp = matrix[node.i - 1][node.j]
        if nodeUp.value == 0 and not nodeUp.check:
            nodeUp.gCost = node.gCost + cost
            nodeUp.hCost = calculateHCost(nodeUp.i, nodeUp.j, nodeEnd)
            nodeUp.parent = node
            neighbors.append(nodeUp)


def down(node, nodeEnd):
    if node.i < 9:
        nodeDown = matrix[node.i + 1][node.j]
        if nodeDown.value == 0 and not nodeDown.check:
            nodeDown.gCost = node.gCost + cost
            nodeDown.hCost = calculateHCost(nodeDown.i, nodeDown.j, nodeEnd)
            nodeDown.parent = node
            neighbors.append(nodeDown)


def right(node, nodeEnd):
    if node.j < 9:
        nodeRight = matrix[node.i][node.j + 1]
        if nodeRight.value == 0 and not nodeRight.check:
            nodeRight.gCost = node.gCost + cost
            nodeRight.hCost = calculateHCost(nodeRight.i, nodeRight.j, nodeEnd)
            nodeRight.parent = node
            neighbors.append(nodeRight)


def left(node, nodeEnd):
    if node.j > 0:
        nodeLeft = matrix[node.i][node.j - 1]
        if nodeLeft.value == 0 and not nodeLeft.check:
            nodeLeft.gCost = node.gCost + cost
            nodeLeft.hCost = calculateHCost(nodeLeft.i, nodeLeft.j, nodeEnd)
            nodeLeft.parent = node
            neighbors.append(nodeLeft)


def aStar(nodeStart, nodeEnd):
    order = 0
    while True:
        order += 1
        if nodeStart.i == nodeEnd.i and nodeStart.j == nodeEnd.j:
            return nodeStart, order
        up(nodeStart, nodeEnd)
        down(nodeStart, nodeEnd)
        right(nodeStart, nodeEnd)
        left(nodeStart, nodeEnd)
        if len(neighbors) == 0:
            return False
        nodeStart.check = True
        minFCost = float('inf')
        for node in neighbors:
            if minFCost > (node.gCost + node.hCost):
                minFCost = node.gCost + node.hCost
                nodeStart = node
                neighbors.remove(node)


def start():
    startI = int(input("Enter I index of start: "))
    startJ = int(input("Enter J index of start: "))
    endI = int(input("Enter I index of end: "))
    endJ = int(input("Enter J index of end: "))
    readMap()
    nodeStart = matrix[startI][startJ]
    nodeEnd = matrix[endI][endJ]
    nodeStart.hCost = calculateHCost(nodeStart.i, nodeStart.j, nodeEnd)
    node, order = aStar(nodeStart, nodeEnd)
    steps = 0
    path = list()
    if node:
        while node is not None:
            steps += 1
            path.append((node.i, node.j))
            node = node.parent
        print("order:", order)
        print("steps:", steps)
        for i in range(10):
            for j in range(10):
                if path.count((i, j)) == 0:
                    print(Fore.RESET, matrix[i][j].value, end=" ")
                else:
                    print(Fore.GREEN, matrix[i][j].value, end=" ")
            print("\n")
    else:
        print(Fore.RED + "no solution")
    pass


start()
