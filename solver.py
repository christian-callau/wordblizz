class Node:
    def __init__(self, val, coord):
        self.val = val
        self.coord = coord
        self.visited = False
        self.nei = []

    def addNei(self, node):
        self.nei.append(node)


class PermsSolver:
    def __init__(self, dic, data, dim):
        self.dic = dic

        if len(data) != dim ** 2:
            raise Exception('Incorrect string length')

        matrix = [data[i:i+dim] for i in range(0, len(data), dim)]

        self.nodes = []

        for i in range(dim):
            aux = []
            for j in range(dim):
                aux.append(Node(matrix[i][j], [i, j]))
            self.nodes.append(aux)

        for y in range(dim):
            for x in range(dim):
                node = self.nodes[y][x]
                offsets = [
                    [0,  1], [0, -1], [1,  0], [-1,  0],
                    [1,  1], [1, -1], [-1,  1], [-1, -1]
                ]
                for offset in offsets:
                    y0 = y + offset[0]
                    x0 = x + offset[1]
                    if 0 <= y0 < dim and 0 <= x0 < dim:
                        node.addNei(self.nodes[y0][x0])

    def nodesToWord(self, nodes):
        return ''.join([node.val for node in nodes])

    def nodesToCoords(self, nodes):
        return [node.coord for node in nodes]

    def getWords(self):
        perms = []
        for row in self.nodes:
            for node in row:
                node.visited = True
                self.auxx(node, [node], perms)
                node.visited = False
        # perms = list(set(perms))

        words = []
        clean_perms = []

        for nodes in perms:
            word = self.nodesToWord(nodes)
            if word not in words:
                words.append(word)
                clean_perms.append(nodes)

        perms = clean_perms

        perms.sort(key=lambda s: len(self.nodesToWord(s)), reverse=True)
        return perms

    def auxx(self, node, nodes, perms):
        for nei in node.nei:
            if not nei.visited:
                nei.visited = True
                new_nodes = nodes + [nei]
                result = self.dic.has(self.nodesToWord(new_nodes))
                if result:
                    perms.append(new_nodes)
                if result or result == None:
                    self.auxx(nei, new_nodes, perms)
                nei.visited = False
